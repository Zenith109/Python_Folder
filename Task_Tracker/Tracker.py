import asyncio
from datetime import datetime

async def task_reminder(task_name, interval):
    while True:
        print(f"Reminder: {task_name} - {datetime.now()}")
        await asyncio.sleep(interval)

async def main():
    await asyncio.gather(
        task_reminder("Drink Water", 7200),  # Remind every 2 hours
        task_reminder("Take a Break", 3600)  # Remind every 1 hour
    )

asyncio.run(main())