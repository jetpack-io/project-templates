from jetpack import cron


@cron.repeat(cron.every(10).minutes)
async def cron_job_function():
    ### Code for your cronjob goes here
    print("I run every 10 minutes")
