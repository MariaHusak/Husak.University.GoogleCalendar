from crontab import CronTab

job_scheduler = CronTab(user=True)

command = 'python3 ./manage.py create_reminders'

job = job_scheduler.new(command=command)

job.minute.on(0)
job.hour.on(0)

script_content = f'''
$action = New-ScheduledTaskAction -Execute 'python3' -Argument './manage.py create_reminders'
$trigger = New-ScheduledTaskTrigger -Daily -At "00:00"
Register-ScheduledTask -TaskName "ReminderTask" -Action $action -Trigger $trigger -User "SYSTEM"
'''
script_path = './setup_task.ps1'

with open(script_path, 'w') as file:
    file.write(script_content)

print(f'PowerShell script generated: {script_path}')
