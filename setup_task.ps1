
$action = New-ScheduledTaskAction -Execute 'python3' -Argument './manage.py create_reminders'
$trigger = New-ScheduledTaskTrigger -Daily -At "00:00"
Register-ScheduledTask -TaskName "ReminderTask" -Action $action -Trigger $trigger -User "SYSTEM"
