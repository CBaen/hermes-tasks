---
id: windows-popup-process-containment
name: Windows Popup Process Containment
schema_version: 2.1
profile: governed
level: recipe
maturity: candidate
scope: wardenclyffe recurring console window and scheduled automation containment
currently_true: unknown
last_verified: 2026-05-14
verification_level: 1
evidence_quality: direct
successful_uses: 1
failed_uses: 1
regressions: 0
depends_on: []
used_by: []
tags:
  - wardenclyffe
  - windows
  - scheduled-tasks
  - conhost
  - powershell
  - backblaze
  - accessibility
---

# Windows Popup Process Containment

Use this when `wardenclyffe` shows random black console windows, `conhost.exe`
flashes, or scheduled automations need to run silently.

## Current Verified State

Verified on 2026-05-07, with OpenClaw retirement updated on 2026-05-14:

- Backblaze service `bzserv` is stopped and set to `Manual`.
- Backblaze setting `backup_schedule_type` was changed to
  `only_when_click_backup_now`.
- `bzfilelist.exe` is not running.
- `WardenclyffStartup` is disabled.
- No enabled scheduled task with a repetition interval of 30 minutes or less was
  found.
- The only Backblaze process left after closeout was `bzbuitray.exe`, the tray
  UI. It was not the `bzfilelist.exe` analyzer that spawned `conhost.exe`.
- The OpenClaw gateway keeper/watchdog scheduled tasks were unregistered during
  OpenClaw retirement and should not be recreated.

## Contained Sources

These root scheduled tasks were disabled or confirmed removed during
containment:

- `AI Comply Docs - Regulation Check`
- `Claude Code Zombie Cleanup`
- `Codex Locally Twisted ERPNext Health Watchdog`
- `Codex OpenClaw Gateway Keeper`
- `Codex OpenClaw Gateway Watchdog`
- `Codex Wardenclyffe System Health Heartbeat`
- `Codex-OneDrive-Removal-Guard`
- `Mae Nightly Daemon`
- `qdrant-backup`
- `WardenclyffConversationIndexer`
- `WardenclyffeMorningBrief`
- `WardenclyffStartup`
- `WSL-Idle-Shutdown`

Do not re-enable these tasks without an explicit user request and a no-window
implementation plan.

OpenClaw-specific note: the two OpenClaw gateway tasks were unregistered during
the 2026-05-14 OpenClaw retirement and should not be recreated.

## Root Lessons

- `Hidden=True` on a scheduled task is not enough. Hidden tasks can still create
  `conhost.exe` when they launch PowerShell, `cmd`, Docker, WSL, Python, or app
  helper executables.
- Verify with process-parent evidence, not just Task Scheduler settings.
- Backblaze can spawn `bzfilelist.exe` under `bzserv.exe`, and `bzfilelist.exe`
  can spawn `conhost.exe`.
- `Stop-Process` can fail for protected service children from a non-elevated
  Codex session. Use an elevated PowerShell or the app's own CLI when available.
- If a window flash creates an accessibility/safety risk, containment takes
  priority over keeping convenience automations alive.

## Verification Commands

Check Backblaze:

```powershell
Get-CimInstance Win32_Service -Filter "Name='bzserv'" |
  Select-Object Name,State,StartMode,ProcessId
Get-Process -Name bzfilelist,bzserv -ErrorAction SilentlyContinue
& 'C:\Program Files\Backblaze\bzcli.exe' report -v /settings/backup_schedule_type
```

Check startup task:

```powershell
Get-ScheduledTask -TaskPath "\" -TaskName "WardenclyffStartup"
```

Check frequent scheduled tasks:

```powershell
$threshold = [TimeSpan]::FromMinutes(30)
Get-ScheduledTask | Where-Object { $_.State.ToString() -ne 'Disabled' } |
  ForEach-Object {
    $task = $_
    foreach ($trigger in @($task.Triggers)) {
      $interval = $trigger.Repetition.Interval
      if ($interval) {
        try { $span = [System.Xml.XmlConvert]::ToTimeSpan($interval) } catch { $span = $null }
        if ($span -and $span -le $threshold) {
          [pscustomobject]@{
            TaskName = $task.TaskName
            TaskPath = $task.TaskPath
            State = $task.State.ToString()
            Interval = $interval
            Action = ($task.Actions | ForEach-Object { $_.Execute + ' ' + $_.Arguments }) -join ' | '
          }
        }
      }
    }
  }
```

Check current console-host parents:

```powershell
$procs = Get-CimInstance Win32_Process
$byId = @{}
foreach ($p in $procs) { $byId[[int]$p.ProcessId] = $p }
$procs | Where-Object { $_.Name -eq 'conhost.exe' } | ForEach-Object {
  $parent = $byId[[int]$_.ParentProcessId]
  [pscustomobject]@{
    Pid = $_.ProcessId
    ParentPid = $_.ParentProcessId
    ParentName = $parent.Name
    ParentCommandLine = $parent.CommandLine
    CommandLine = $_.CommandLine
    CreationDate = $_.CreationDate
  }
}
```

## Re-Enable Requirements

Before any disabled automation is re-enabled:

1. Confirm the user explicitly wants that exact automation back.
2. Replace direct `powershell.exe`, `cmd.exe`, `.bat`, Docker, WSL, or Python
   task actions with a verified no-window wrapper.
3. For PowerShell scripts that launch subprocesses, use
   `System.Diagnostics.ProcessStartInfo` with:
   - `UseShellExecute = $false`
   - `CreateNoWindow = $true`
   - `WindowStyle = Hidden`
   - redirected stdout and stderr
4. Run a process watcher for `conhost.exe`, `cmd.exe`, `powershell.exe`,
   `pwsh.exe`, `docker.exe`, `wsl.exe`, `node.exe`, and app-specific helpers
   while the task runs.
5. Record the verification result in the workstream or capability evidence.

## Related Files

- `C:\Users\baenb\.codex\monitoring\wardenclyffe-system-health-report.ps1`
- Retired on 2026-05-14: `C:\Users\baenb\.codex\monitoring\openclaw-gateway-keeper.ps1`
- Retired on 2026-05-14: `C:\Users\baenb\.codex\monitoring\openclaw-gateway-watchdog.ps1`
- `C:\Users\baenb\.codex\monitoring\locally-twisted-health-watchdog.ps1`
- `C:\Program Files\Backblaze\bzcli.exe`
