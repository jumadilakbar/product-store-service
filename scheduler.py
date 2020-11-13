import schedule
import time
# from Service.recomendation_eng import main_rec
# from ..Service.recomendation_eng import main_rec
from Service.recomendation_eng import main_rec
from Service.asosiasirule_eng import main_rule_maining
from Service.tranding_eng import main_tranding

def job():
    print("I'm working...")

schedule.every(10).seconds.do(main_rec)
schedule.every(10).seconds.do(main_rule_maining)
schedule.every(10).seconds.do(main_tranding)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
