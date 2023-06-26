init 10:

    ################
    # Character Definition
    ################

    define yeongwon = Character('영원', image="yeongwon")
    define haneul = Character('하늘', image="haneul")
    define haneullong = Character('하늘', image="haneullong")
    define hanbyeol = Character('한별', image="hanbyeol")
    define hanseol = Character('한설', image="hanseol")
    define yeonwoo = Character('연우', image="yeonwoo")
    define principal = Character('원장', image="principal")
    define overwatch = Character('감시자', image="overwatch")
    define overwatch2 = Character('1반 선생님', image="overwatch2")
    define keibi = Character('경비원', image="keibi")
    define teacher = Character('선생님', image="teacher")
    define mstudent = Character('남학생', image="mstudent")
    define fstudent = Character('여학생', image="fstudent")
    define haneul2 = Character('??')
    define shonen = Character('소년')
    define shojo = Character('소녀')

    define nvle = Character("", kind=nvl, what_text_align=0.5, what_xalign=0.5, what_yalign=0.5)

    ################
    # Character Standing CG Definition
    ################

    image fstudent speaking = "extra/fstudent.png"
    image keibi speaking = "extra/keibi.png"
    image mstudent speaking = "extra/mstudent.png"
    image teacher speaking = "extra/teacher.png"

    image hanbyeol fury speaking = "hanbyeol/fury.png"
    image hanbyeol fury2 speaking = "hanbyeol/fury2.png"
    image hanbyeol happy speaking = "hanbyeol/happy.png"
    image hanbyeol happy2 speaking = "hanbyeol/happy2.png"
    image hanbyeol idle speaking = "hanbyeol/idle.png"
    image hanbyeol idle2 speaking = "hanbyeol/idle2.png"
    image hanbyeol sad speaking = "hanbyeol/sad.png"
    image hanbyeol sad2 speaking = "hanbyeol/sad2.png"
    image hanbyeol serious speaking = "hanbyeol/serious.png"
    image hanbyeol serious2 speaking = "hanbyeol/serious2.png"
    image hanbyeol shock speaking = "hanbyeol/shock.png"
    image hanbyeol shock2 speaking = "hanbyeol/shock2.png"

    image haneul adult speaking = "haneul/adult.png"
    image haneul fury speaking = "haneul/fury.png"
    image haneul happy speaking = "haneul/happy.png"
    image haneul happy2 speaking = "haneul/happy2.png"
    image haneul idle speaking = "haneul/idle.png"
    image haneul sad speaking = "haneul/sad.png"
    image haneul serious speaking = "haneul/serious.png"
    image haneul shock speaking = "haneul/shock.png"

    image haneullong fury speaking = "haneullong/fury.png"
    image haneullong happy speaking = "haneullong/happy.png"
    image haneullong happy2 speaking = "haneullong/happy2.png"
    image haneullong idle speaking = "haneullong/idle.png"
    image haneullong sad speaking = "haneullong/sad.png"
    image haneullong serious speaking = "haneullong/serious.png"
    image haneullong shock speaking = "haneullong/shock.png"

    image hanseol happy speaking = "hanseol/happy.png"
    image hanseol happy2 speaking = "hanseol/happy2.png"
    image hanseol idle speaking = "hanseol/idle.png"
    image hanseol idle2 speaking = "hanseol/idle2.png"
    image hanseol sad speaking = "hanseol/sad.png"
    image hanseol sad2 speaking = "hanseol/sad2.png"
    image hanseol shock speaking = "hanseol/shock.png"
    image hanseol shock2 speaking = "hanseol/shock2.png"

    image overwatch devil speaking = "overwatch/devil.png"
    image overwatch fury speaking = "overwatch/fury.png"
    image overwatch idle speaking = "overwatch/idle.png"
    image overwatch idle2 speaking = "overwatch/idle2.png"

    image overwatch2 devil speaking = "overwatch/devil.png"
    image overwatch2 fury speaking = "overwatch/fury.png"
    image overwatch2 idle speaking = "overwatch/idle.png"
    image overwatch2 idle2 speaking = "overwatch/idle2.png"

    image principal cry speaking = "principal/cry.png"
    image principal cry2 speaking = "principal/cry2.png"
    image principal happy speaking = "principal/happy.png"
    image principal happy2 speaking = "principal/happy2.png"
    image principal idle speaking = "principal/idle.png"
    image principal idle2 speaking = "principal/idle2.png"
    image principal sad speaking = "principal/sad.png"
    image principal sad2 speaking = "principal/sad2.png"
    image principal sentimental speaking = "principal/sentimental.png"
    image principal sentimental2 speaking = "principal/sentimental2.png"
    image principal shock speaking = "principal/shock.png"
    image principal shock2 speaking = "principal/shock2.png"

    image principalglass happy speaking = "principalglass/happy.png"
    image principalglass happy2 speaking = "principalglass/happy2.png"
    image principalglass idle speaking = "principalglass/idle.png"
    image principalglass idle2 speaking = "principalglass/idle2.png"

    image yeonwoo happy speaking = "yeonwoo/happy.png"
    image yeonwoo happy2 speaking = "yeonwoo/happy2.png"
    image yeonwoo idle speaking = "yeonwoo/idle.png"
    image yeonwoo idle2 speaking = "yeonwoo/idle2.png"

    image yeongwon adult speaking = "yeongwon/adult.png"
    image yeongwon blush speaking = "yeongwon/blush.png"
    image yeongwon blush2 speaking = "yeongwon/blush2.png"
    image yeongwon fury speaking = "yeongwon/fury.png"
    image yeongwon fury2 speaking = "yeongwon/fury2.png"
    image yeongwon happy speaking = "yeongwon/happy.png"
    image yeongwon happy2 speaking = "yeongwon/happy2.png"
    image yeongwon idle speaking = "yeongwon/idle.png"
    image yeongwon idle2 speaking = "yeongwon/idle2.png"
    image yeongwon sad speaking = "yeongwon/sad.png"
    image yeongwon sad2 speaking = "yeongwon/sad2.png"
    image yeongwon serious speaking = "yeongwon/serious.png"
    image yeongwon serious2 speaking = "yeongwon/serious2.png"
    image yeongwon shock speaking = "yeongwon/shock.png"
    image yeongwon shock2 speaking = "yeongwon/shock2.png"

    # Darker varients
    image fstudent = im.MatrixColor("extra/fstudent.png", im.matrix.brightness(-0.2))
    image keibi = im.MatrixColor("extra/keibi.png", im.matrix.brightness(-0.2))
    image mstudent = im.MatrixColor("extra/mstudent.png", im.matrix.brightness(-0.2))
    image teacher = im.MatrixColor("extra/teacher.png", im.matrix.brightness(-0.2))

    image hanbyeol fury = im.MatrixColor("hanbyeol/fury.png", im.matrix.brightness(-0.2))
    image hanbyeol fury2 = im.MatrixColor("hanbyeol/fury2.png", im.matrix.brightness(-0.2))
    image hanbyeol happy = im.MatrixColor("hanbyeol/happy.png", im.matrix.brightness(-0.2))
    image hanbyeol happy2 = im.MatrixColor("hanbyeol/happy2.png", im.matrix.brightness(-0.2))
    image hanbyeol idle = im.MatrixColor("hanbyeol/idle.png", im.matrix.brightness(-0.2))
    image hanbyeol idle2 = im.MatrixColor("hanbyeol/idle2.png", im.matrix.brightness(-0.2))
    image hanbyeol sad = im.MatrixColor("hanbyeol/sad.png", im.matrix.brightness(-0.2))
    image hanbyeol sad2 = im.MatrixColor("hanbyeol/sad2.png", im.matrix.brightness(-0.2))
    image hanbyeol serious = im.MatrixColor("hanbyeol/serious.png", im.matrix.brightness(-0.2))
    image hanbyeol serious2 = im.MatrixColor("hanbyeol/serious2.png", im.matrix.brightness(-0.2))
    image hanbyeol shock = im.MatrixColor("hanbyeol/shock.png", im.matrix.brightness(-0.2))
    image hanbyeol shock2 = im.MatrixColor("hanbyeol/shock2.png", im.matrix.brightness(-0.2))

    image haneul adult = im.MatrixColor("haneul/adult.png", im.matrix.brightness(-0.2))
    image haneul fury = im.MatrixColor("haneul/fury.png", im.matrix.brightness(-0.2))
    image haneul happy = im.MatrixColor("haneul/happy.png", im.matrix.brightness(-0.2))
    image haneul happy2 = im.MatrixColor("haneul/happy2.png", im.matrix.brightness(-0.2))
    image haneul idle = im.MatrixColor("haneul/idle.png", im.matrix.brightness(-0.2))
    image haneul sad = im.MatrixColor("haneul/sad.png", im.matrix.brightness(-0.2))
    image haneul serious = im.MatrixColor("haneul/serious.png", im.matrix.brightness(-0.2))
    image haneul shock = im.MatrixColor("haneul/shock.png", im.matrix.brightness(-0.2))

    image haneullong fury = im.MatrixColor("haneullong/fury.png", im.matrix.brightness(-0.2))
    image haneullong happy = im.MatrixColor("haneullong/happy.png", im.matrix.brightness(-0.2))
    image haneullong happy2 = im.MatrixColor("haneullong/happy2.png", im.matrix.brightness(-0.2))
    image haneullong idle = im.MatrixColor("haneullong/idle.png", im.matrix.brightness(-0.2))
    image haneullong sad = im.MatrixColor("haneullong/sad.png", im.matrix.brightness(-0.2))
    image haneullong serious = im.MatrixColor("haneullong/serious.png", im.matrix.brightness(-0.2))
    image haneullong shock = im.MatrixColor("haneullong/shock.png", im.matrix.brightness(-0.2))

    image hanseol happy = im.MatrixColor("hanseol/happy.png", im.matrix.brightness(-0.2))
    image hanseol happy2 = im.MatrixColor("hanseol/happy2.png", im.matrix.brightness(-0.2))
    image hanseol idle = im.MatrixColor("hanseol/idle.png", im.matrix.brightness(-0.2))
    image hanseol idle2 = im.MatrixColor("hanseol/idle2.png", im.matrix.brightness(-0.2))
    image hanseol sad = im.MatrixColor("hanseol/sad.png", im.matrix.brightness(-0.2))
    image hanseol sad2 = im.MatrixColor("hanseol/sad2.png", im.matrix.brightness(-0.2))
    image hanseol shock = im.MatrixColor("hanseol/shock.png", im.matrix.brightness(-0.2))
    image hanseol shock2 = im.MatrixColor("hanseol/shock2.png", im.matrix.brightness(-0.2))

    image overwatch devil = im.MatrixColor("overwatch/devil.png", im.matrix.brightness(-0.2))
    image overwatch fury = im.MatrixColor("overwatch/fury.png", im.matrix.brightness(-0.2))
    image overwatch idle = im.MatrixColor("overwatch/idle.png", im.matrix.brightness(-0.2))
    image overwatch idle2 = im.MatrixColor("overwatch/idle2.png", im.matrix.brightness(-0.2))

    image overwatch2 devil = im.MatrixColor("overwatch/devil.png", im.matrix.brightness(-0.2))
    image overwatch2 fury = im.MatrixColor("overwatch/fury.png", im.matrix.brightness(-0.2))
    image overwatch2 idle = im.MatrixColor("overwatch/idle.png", im.matrix.brightness(-0.2))
    image overwatch2 idle2 = im.MatrixColor("overwatch/idle2.png", im.matrix.brightness(-0.2))

    image principal cry = im.MatrixColor("principal/cry.png", im.matrix.brightness(-0.2))
    image principal cry2 = im.MatrixColor("principal/cry2.png", im.matrix.brightness(-0.2))
    image principal happy = im.MatrixColor("principal/happy.png", im.matrix.brightness(-0.2))
    image principal happy2 = im.MatrixColor("principal/happy2.png", im.matrix.brightness(-0.2))
    image principal idle = im.MatrixColor("principal/idle.png", im.matrix.brightness(-0.2))
    image principal idle2 = im.MatrixColor("principal/idle2.png", im.matrix.brightness(-0.2))
    image principal sad = im.MatrixColor("principal/sad.png", im.matrix.brightness(-0.2))
    image principal sad2 = im.MatrixColor("principal/sad2.png", im.matrix.brightness(-0.2))
    image principal sentimental = im.MatrixColor("principal/sentimental.png", im.matrix.brightness(-0.2))
    image principal sentimental2 = im.MatrixColor("principal/sentimental2.png", im.matrix.brightness(-0.2))
    image principal shock = im.MatrixColor("principal/shock.png", im.matrix.brightness(-0.2))
    image principal shock2 = im.MatrixColor("principal/shock2.png", im.matrix.brightness(-0.2))

    image principalglass happy = im.MatrixColor("principalglass/happy.png", im.matrix.brightness(-0.2))
    image principalglass happy2 = im.MatrixColor("principalglass/happy2.png", im.matrix.brightness(-0.2))
    image principalglass idle = im.MatrixColor("principalglass/idle.png", im.matrix.brightness(-0.2))
    image principalglass idle2 = im.MatrixColor("principalglass/idle2.png", im.matrix.brightness(-0.2))

    image yeonwoo happy = im.MatrixColor("yeonwoo/happy.png", im.matrix.brightness(-0.2))
    image yeonwoo happy2 = im.MatrixColor("yeonwoo/happy2.png", im.matrix.brightness(-0.2))
    image yeonwoo idle = im.MatrixColor("yeonwoo/idle.png", im.matrix.brightness(-0.2))
    image yeonwoo idle2 = im.MatrixColor("yeonwoo/idle2.png", im.matrix.brightness(-0.2))

    image yeongwon blush = im.MatrixColor("yeongwon/blush.png", im.matrix.brightness(-0.2))
    image yeongwon blush2 = im.MatrixColor("yeongwon/blush2.png", im.matrix.brightness(-0.2))
    image yeongwon fury = im.MatrixColor("yeongwon/fury.png", im.matrix.brightness(-0.2))
    image yeongwon fury2 = im.MatrixColor("yeongwon/fury2.png", im.matrix.brightness(-0.2))
    image yeongwon happy = im.MatrixColor("yeongwon/happy.png", im.matrix.brightness(-0.2))
    image yeongwon happy2 = im.MatrixColor("yeongwon/happy2.png", im.matrix.brightness(-0.2))
    image yeongwon idle = im.MatrixColor("yeongwon/idle.png", im.matrix.brightness(-0.2))
    image yeongwon idle2 = im.MatrixColor("yeongwon/idle2.png", im.matrix.brightness(-0.2))
    image yeongwon sad = im.MatrixColor("yeongwon/sad.png", im.matrix.brightness(-0.2))
    image yeongwon sad2 = im.MatrixColor("yeongwon/sad2.png", im.matrix.brightness(-0.2))
    image yeongwon serious = im.MatrixColor("yeongwon/serious.png", im.matrix.brightness(-0.2))
    image yeongwon serious2 = im.MatrixColor("yeongwon/serious2.png", im.matrix.brightness(-0.2))
    image yeongwon shock = im.MatrixColor("yeongwon/shock.png", im.matrix.brightness(-0.2))
    image yeongwon shock2 = im.MatrixColor("yeongwon/shock2.png", im.matrix.brightness(-0.2))
    image yeongwon adult = im.MatrixColor("yeongwon/adult.png", im.matrix.brightness(-0.2))

    ################
    # Background Sprite Definition
    ################

    image background bed = "background/bed.png"
    image background classday = "background/classday.png"
    image background classnight = "background/classnight.png"
    image background dayhideout = "background/dayhideout.png"
    image background dininghall = "background/dininghall.png"
    image background dormhallway = "background/dormhallway.png"
    image background dormhanbyeol = "background/dormhanbyeol.png"
    image background dormlowchroma = "background/dormlowchroma.png"
    image background dormyeongwon = "background/dormyeongwon.png"
    image background hiddenlab = "background/hiddenlab.png"
    image background hospital = "background/hospital.png"
    image background house = "background/house.png"
    image background lab = "background/lab.png"
    image background labhallway = "background/labhallway.png"
    image background nighthideout = "background/nighthideout.png"
    image background oldclass = "background/oldclass.png"
    image background oldhallway = "background/oldhallway.png"
    image background oldschool = "background/oldschool.png"
    image background oldstairs = "background/oldstairs.png"
    image background principaloffice = "background/principaloffice.png"
    image background school = "background/school.png"
    image background schoolhallway = "background/schoolhallway.png"
    image background schoolhallwaynight = "background/schoolhallwaynight.png"
    image background shelter = "background/shelter.png"
    image background sky = "background/sky.png"
    image background skysunset = "background/skysunset.jpg"
    image background skydark = "background/skydark.jpg"
    image background library = "background/library.png"
    image background libraryin = "background/libraryin.png"
    image background stairs = "background/stairs.png"
    image background schoolstair = "background/schoolstair.png"
    image background wasteland = "background/wasteland.png"
    image background blackscreen ="background/blackscreen.jpg"
    image background blackscreen01 ="background/blackscreen01.png"
    image background blackscreen02 ="background/blackscreen02.png"
    image background blackscreen03 ="background/blackscreen03.jpg"

    image background black = Solid("#000000")
    image background gray = Solid("#d1d1d1")
    image background white = Solid("#FFFFFF")

    image background bed dark = im.MatrixColor("background/bed.png", im.matrix.brightness(-0.2))
    image background classday dark = im.MatrixColor("background/classday.png", im.matrix.brightness(-0.2))
    image background classnight dark = im.MatrixColor("background/classnight.png", im.matrix.brightness(-0.2))
    image background dayhideout dark = im.MatrixColor("background/dayhideout.png", im.matrix.brightness(-0.2))
    image background dininghall dark = im.MatrixColor("background/dininghall.png", im.matrix.brightness(-0.2))
    image background dormhallway dark = im.MatrixColor("background/dormhallway.png", im.matrix.brightness(-0.2))
    image background dormhanbyeol dark = im.MatrixColor("background/dormhanbyeol.png", im.matrix.brightness(-0.2))
    image background dormlowchroma dark = im.MatrixColor("background/dormlowchroma.png", im.matrix.brightness(-0.2))
    image background dormyeongwon dark = im.MatrixColor("background/dormyeongwon.png", im.matrix.brightness(-0.2))
    image background hiddenlab dark = im.MatrixColor("background/hiddenlab.png", im.matrix.brightness(-0.2))
    image background hospital dark = im.MatrixColor("background/hospital.png", im.matrix.brightness(-0.2))
    image background house dark = im.MatrixColor("background/house.png", im.matrix.brightness(-0.2))
    image background lab dark = im.MatrixColor("background/lab.png", im.matrix.brightness(-0.2))
    image background labhallway bright = "background/labhallwaylight.png"
    image background labhallway dark = "background/labhallwaylight2.png"
    image background labhallway dark2 = im.MatrixColor("background/labhallway.png", im.matrix.brightness(-0.4))
    image background dorm dark = im.MatrixColor("background/dorm.jpg", im.matrix.brightness(-0.2))
    image background labhallway dark = im.MatrixColor("background/labhallway.png", im.matrix.brightness(-0.2))
    image background nighthideout dark = im.MatrixColor("background/nighthideout.png", im.matrix.brightness(-0.2))
    image background oldclass dark = im.MatrixColor("background/oldclass.png", im.matrix.brightness(-0.2))
    image background oldhallway dark = im.MatrixColor("background/oldhallway.png", im.matrix.brightness(-0.2))
    image background oldschool dark = im.MatrixColor("background/oldschool.png", im.matrix.brightness(-0.2))
    image background oldstairs dark = im.MatrixColor("background/oldstairs.png", im.matrix.brightness(-0.2))
    image background principaloffice dark = im.MatrixColor("background/principaloffice.png", im.matrix.brightness(-0.2))
    image background school dark = im.MatrixColor("background/school.png", im.matrix.brightness(-0.2))
    image background schoolhallway dark = im.MatrixColor("background/schoolhallway.png", im.matrix.brightness(-0.2))
    image background schoolhallwaynight dark = im.MatrixColor("background/schoolhallwaynight.png", im.matrix.brightness(-0.2))
    image background shelter dark = im.MatrixColor("background/shelter.png", im.matrix.brightness(-0.2))
    image background sky dark = im.MatrixColor("background/sky.png", im.matrix.brightness(-0.2))
    image background stairs dark = im.MatrixColor("background/stairs.png", im.matrix.brightness(-0.2))
    image background wasteland dark = im.MatrixColor("background/wasteland.png", im.matrix.brightness(-0.2))
    image background library dark = im.MatrixColor("background/library.png", im.matrix.brightness(-0.2))

    ################
    # Predefined positions
    ################

    transform slightleft:
        xalign 0.30
        yalign 1.0

    transform slightright:
        xalign 0.75
        yalign 1.0

    transform moveright:
        linear 0.5 xalign 0.95

    transform movecenter:
        linear 0.5 xalign 0.5

    transform moveslightright:
        linear 0.5 xalign 0.75

    transform moveleft:
        linear 0.5 xalign 0.05

    transform moveslightleft:
        linear 0.5 xalign 0.3

    screen letter(content):
        zorder 10
        modal False

        add "sprite/letter.png":
            at transform:
                align (0.5, 0.5)
                zoom 0.4
                alpha 0.0
                linear 0.25 alpha 1.0
        viewport:
            maximum (400, 400)
            align (0.5, 0.5)

            text content:
                font "NanumHandwriting Kkotnaeum.ttf"
                kerning 2.5
                at transform:
                    alpha 0.0
                    linear 0.25 alpha 1.0
        key "dismiss" action Return()
