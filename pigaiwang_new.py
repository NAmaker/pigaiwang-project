import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pigaiwang.gui_input import Gui_input
from Pigaiwang.gui_txt import name
from Pigaiwang.gui_txt2 import password
from Pigaiwang.Have_not import have1_or_not2
from Pigaiwang.Gui_choice import which
from Pigaiwang.Gui_choice2 import wh
from Pigaiwang.Gui_trans import Gui_trans


class Act(object):

    def __init__(self, web):
        bro = webdriver.Chrome(executable_path=r"../chromedriver.exe")
        self.bro = bro
        self.bro.get(web)  # 可以更换
        self.bro.maximize_window()

    def locate_html(self, res):
        return self.bro.find_element(By.XPATH, res)

    def js_locate(self, js):
        return self.bro.execute_script(js)

    def send_keys(self, res, key):
        self.locate_html(res).send_keys(key)

    def click_x(self, res):
        self.locate_html(res).click()

    def js_click(self, js):
        self.bro.execute_script(js)

    def clear(self, res):
        self.locate_html(res).clear()

    def close(self):
        self.bro.close()


class Translate(Act):
    ads = '//*[@id="app-guide"]/div/div/div[2]/span'

    def action(self, eassy):
        self.bro.find_element(By.XPATH, self.ads).click()
        self.bro.find_element(By.XPATH, '//*[@id="baidu_translate_input"]').send_keys(eassy)
        self.bro.find_element(By.XPATH, '//*[@id="translate-button"]').click()
        time.sleep(1)
        text = self.bro.find_element(By.XPATH,
                                     '//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]').text
        self.bro.close()
        return text


class Xpath(Act):
    id_x = '//*[@id="username"]'
    password_x = '//*[@id="password"]'
    js = "document.getElementById('ulogin').click();"
    # 已经登录

    already_first = '//*[@id="essayList"]/ul[2]/li[8]/a[2]'  # 已完成的第一个的完善
    already_second = '//*[@id="essayList"]/ul[3]/li[8]/a[2]'
    already_third = '//*[@id="essayList"]/ul[4]/li[8]/a[2]'
    already_fourth = '//*[@id="essayList"]/ul[5]/li[8]/a[2]'
    already_fifth = '//*[@id="essayList"]/ul[6]/li[8]/a[2]'

    have_not_down = '//*[@id="pigaiV4"]/div[1]/ul/li[2]/span/a'  # 未完成按钮
    have_not_down_1 = '//*[@id="essayList"]/ul[2]/li[7]/a'  # 未完成的第一个
    have_not_down_2 = '//*[@id="essayList"]/ul[3]/li[7]/a'
    have_not_down_3 = '//*[@id="essayList"]/ul[4]/li[7]/a'
    have_not_down_4 = '//*[@id="essayList"]/ul[5]/li[7]/a'
    have_not_down_5 = '//*[@id="essayList"]/ul[6]/li[7]/a'

    input = '//*[ @ id = "contents"]'
    clear1 = '//*[@id="contents"]'
    submit = '//*[@id="dafen"]'

    def action(self, have1_or_not2, which, name, password, article):
        self.send_keys(self.id_x, name)
        self.send_keys(self.password_x, password)
        self.js_click(self.js)
        if have1_or_not2 == 1:
            if which == 2:
                self.click_x(self.already_second)  # 完善第二个
            elif which == 1:
                self.click_x(self.already_first)
            elif which == 3:
                self.click_x(self.already_third)
            elif which == 4:
                self.click_x(self.already_fourth)
            elif which == 5:
                self.click_x(self.already_fifth)

        elif have1_or_not2 == 2:
            self.click_x(self.have_not_down)  # 切换到未完善界面
            if which == 1:
                self.click_x(self.have_not_down_1)  # 未完善第1个
            elif which == 2:
                self.click_x(self.have_not_down_2)
            elif which == 3:
                self.click_x(self.have_not_down_3)
            elif which == 4:
                self.click_x(self.have_not_down_4)
            elif which == 5:
                self.click_x(self.have_not_down_5)

        if self.locate_html(self.clear1).text:
            self.clear(self.clear1)
        self.send_keys(self.input, article)
        time.sleep(2)
        self.click_x(self.submit)
        time.sleep(2)
        self.close()


def choice(wh):
    if wh == 0:
        trans = Gui_trans("你输入是作文是英文还是中文？1是英文，2是中文")
        trans = trans.x
        article = Gui_input("输入你的作文")
        article = article.x
        if trans == 2:
            tran = Translate("https://fanyi.baidu.com/")
            article = tran.action(article)
        else:
            pass
    elif wh == 1:
        article = "Energetic youth is not simple to perish. Mistakes cannot stand failure, but reality is not afraid of failure. As long as there is a breath left, one should not give up hope. One's death is either heavier than Mount Tai or lighter than a feather. Laughter is sunshine, it can eliminate the winter color of people's faces.Whoever loses patience loses his soul. The closer you get to the truth, the more fascinated you will find the truth. I can't choose the best. The spring of the river has existed for thousands of years, and youth is gone forever. The famous saying of blood is willing to share weather and woe with the people and pledge to fight for blood to solidify the divine land. The most terrible enemy is that he has no strong faith. Many people pay for their success with the happiness of their youth. For indomitable people, there is no such thing as failure. I can only offer my blood, sweat and tears. The golden age is in front of us, not behind us. If we have accepted the worst, there will be no loss. As long as we can make good use of time, we will never worry about time shortage. If you want to monopolize the truth, the truth will laugh at you.We love our nation, which is the source of our self-confidence. Many people take the happiness of youth as the price of success. For those who are afraid of danger, the world is always dangerous. A failure only proves that our determination to succeed is strong enough. For a beautiful hope, we suffered so much, shed tears and shed blood. Where can I buy youth?Achieving great things does not depend on strength, but on strength."
    elif wh == 2:
        article = "I spent my childhood in a small village. It is a beautiful village, far away from the noise of the city, with a sense of loneliness that belongs here alone. In spring in the countryside, I can hear all kinds of voices. The rugged snow leopard, the plaintive lynx, and the happy rock sheep. The cries of these animal friends bring me unparalleled happiness. In summer, cicadas kept talking, and we played many games on the grass. Following the rhythm of our partners, we whirled and jumped, feeling the emotion of the wind with our eyes closed. How happy! In autumn and winter, though the land withered, it lost its vitality. But everything is quiet, which has a special flavor. We can roll freely in the snow, dance our youth and sweat. How can we say that we are unhappy? There is an image ambassador in my hometown. His name is Pearl Ding Zhen. He is our idol, as dazzling as Gu Ailing. I'm proud that there are such people in my hometown. This is my unique childhood experience. This childhood experience has brought me spiritual wealth throughout my life. Therefore, my soul has a destination. The smell of hometown may be hidden in the sound of animal friends! "
    elif wh == 3:
        article = "With the continuous development of society, civilization is also making continuous progress. From agricultural civilization to industrial civilization, from information society to epoch-making today. Morality has always been an eternal topic.In ancient times, morality was used to restrict people's behavior and provide people with code of conduct. In modern society, after pursuing material civilization, people put morality to a new height. At present, although we govern the country according to law, the role of morality cannot be underestimated. Many times, morality can play a role that law cannot.For example, not littering everywhere is a small moral behavior, but it can greatly reduce the burden of cleaners. Consciously abide by traffic rules and don't run red lights, you can reduce a lot of traffic accidents. For another example, chaining a pet dog can reduce the random bite of a pet dog. And these things, relying on legal constraints alone, often do not necessarily achieve the expected results. Morality restricts people's behavior from the spiritual level, which is very effective.Only by abiding by the code of ethics and not violating your own moral bottom line can you make progress."
    elif wh == 4:
        article = "All kinds of things will happen in one's life, and everything will give us different feelings. Next, I want to introduce an unforgettable experience of myself.When I was still in high school, our class planned to hold an English speech contest. The English teacher asked at least one student in each group to participate. In our group, because I was the team leader, I was naturally elected to participate in the competition. Although I am not very willing to participate, I have no way, because this is something agreed by my team members. So I have to make serious preparations. I make full use of my time outside the classroom to prepare, carefully collect data, revise articles, and ensure that I can speak fluently.On the day of the competition, I also read my manuscript before the competition. I think my preparation has been done well, but I didn't expect that there were problems in my speech. At the end of my speech, I was so complacent that I forgot the following content. At that time, my mind was blank and I didn't know what to do. Although I managed to finish the speech with the encouragement of my teachers and classmates, I still feel very embarrassed when I remember standing on the stage and forgetting my words."
    else:
        print("出错了喔")
    return article


if __name__ == '__main__':
    article = choice(wh)
    new = Xpath("http://www.pigai.org/index.php")
    new.action(have1_or_not2=have1_or_not2, which=which, name=name, password=password, article=article)
    time.sleep(4)
