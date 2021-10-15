# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import inspect, os, platform, time
def bot():
    #필요한 변수 정의
    insta_id = input('인스타그램 아이디 : ')
    insta_pw = input('인스타그램 패스워드 : ')
    insta_tag = input('작업할 해시태그 : ')
    insta_cnt = int(input('작업횟수(숫자만) : '))
    insta_sort = input('0 : 인기게시물, 1 : 최근게시물')
    insta_comm = ['잘 보고 갑니다!소통해요']
    global div


    #크롬드라이버 로딩
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')

    current_folder = os.path.realpath(
                os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))

    if platform.system() == 'Windows':
        driver_path = os.path.join(current_folder, 'chromedriver.exe')
    else:
        driver_path = os.path.join(current_folder, 'chromedriver')

    driver = webdriver.Chrome(driver_path, options=options)
    driver.implicitly_wait(10)

    
    ### 인스타그램 자동 좋아요 작업 ###
    
    # 1. 인스타그램 로그인 페이지로 이동
    driver.get('https://www.instagram.com/?hl=ko')
    print('로그인중....')
    time.sleep(3)

    # 2. 아이디 입력창을 찾아서 위에서 입력받은 아이디(insta_id)값 입력
    id_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label')
    id_input.click() #입력창 클릭
    id_input.send_keys(insta_id) #아이디 입력


    # 2-1. 패스워드 입력창을 찾아서 위에서 입력받은 패스워드(insta_pw)값 입력
    pw_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label')
    pw_input.click()
    pw_input.send_keys(insta_pw)

    # 3. 로그인 버튼 클릭
    login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login_btn.click()


    # 잠시 대기
    time.sleep(3)


    # 4. 작업할 해시태그 검색 결과 페이지로 이동
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(insta_tag))
    time.sleep(5)

    # 5. 인기게시물 혹은 최근게시물 첫번째 피드 선택
    if insta_sort == '0':
        #인기게시물 첫번째 피트 선택
        hot_first_feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        hot_first_feed.click()
    else:
        #최근게시물 첫번째 피드 선택
        new_first_feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]')
        new_first_feed.click()
    
    time.sleep(5)

    # 6. 좋아요 작업 - 입력한 횟수만큼 반복 작업
    for idx in range(insta_cnt):
        #div = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div')
        #div = div.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg/path')
        
        like_btn = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.ltpMr.Slqrh > span.fr66n > button') #좋아요 버튼
        

        btn_svg = like_btn.find_element_by_tag_name('svg')
        svg_txt = btn_svg.get_attribute('aria-label')

        if svg_txt != '좋아요':
            print('이미 좋아요 작업한 피드')
        else:
            like_btn.click() #좋아요 클릭
            print('{}번째 피드 좋아요 작업 완료'.format(idx + 1))

        # 너무 빠르게 작업을 할 경우 많은 양의 작업을 하게 되어 인스타그램측에서 계정 정지나 경고를 할 수 있으니
        # 작업과 다음 작업 사이의 속도를 조절하기 위해 20초 이상을 설정해주세요.
        time.sleep(20)

        #10. 팔로우 기능 추가
        #10-1. 팔로우 버튼 찾기
        #div = driver.find_element_by_xpath('body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button')
        #header = div.find_element_by_tag_name('header')
        follow_btn = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
        follow_btn_txt = follow_btn.text

        #10-2. 버튼의 텍스트가 팔로우인 경우에만 팔로우 버튼 클릭
        if follow_btn_txt == '팔로우':
            time.sleep(2)
            follow_btn.click()

            print('{}번째 피드 팔로우 성공'.format(idx + 1))
            time.sleep(5) #빠른 작업 방지를 위한 대기시간 설정
        elif follow_btn_txt == '팔로잉':
            print('이미 팔로우한 계정입니다.')
            # 7. 좋아요 작업 - 다음 피드로 이동
        
        if idx < insta_cnt:
            try:
                next_feed = driver.find_element_by_link_text('다음')
                next_feed.click()
            except NoSuchElementException as n:
                print('피드 개수 부족으로 작업이 종료됩니다.')
                break
        time.sleep(5)



    print('모든 작업 완료')
    driver.quit()


bot()