# 이 파일에 게임 스크립트를 입력합니다.

# 이미지 위치 정위
transform slightleft:
    xalign 0.30
    yalign 1.0

transform slightright:
    xalign 0.70
    yalign 1.0

# 캐릭터
define ihyun = Character("이현",color="#c8ffc8")
define isol = Character("이솔",color="#c8ffc8")
define siwook = Character("정시욱",color="#c8ffc8")
define yuhyeon = Character("김유현",color="#c8ffc8")
define hyunjoo = Character("고현주",color="#c8ffc8")
define jungyu = Character("박준규",color="#c8ffc8")
define jungeun = Character("조정은",color="c8ffc8")
# novel 모드를 위해 정의한 임시 캐릭터
define nvle = Character(" ", kind=nvl, what_text_align=0.5, what_xalign=0.5, what_yalign=0.5)

# 여기에서부터 게임이 시작합니다.
label start:
    play music "music/opening.mp3" fadeout 1
    # 앞에 nvle을 붙이면, novel 모드라고 해서 글자가 화면 중앙에 보이게 된다.
    # {cps='숫자'}이 안에 들어가있는 문장은 '숫자'만큼의 속도로 글자가 순서대로 나타난다.{/cps}
    # {color = RGB}이 안에 들어가있는 글자는 RGB의 색깔대로 나타난다.{/color}
    # 예를 들어 f00은 빨강, 0f0은 초록, 00f는 파랑이다.
    nvle ""
    nvle ""
    nvle "{cps=25}{color=f00}의인은 없나니 하나도 없으며(롬 3:10){/color}{/cps}"

    nvle "{cps=25}{color=f00}모든 사람이 죄를 지었으므로 죽음이 모든 사람에게 찾아노느니라. (룸 5:12){/color}{/cps}"

    # nvl clear : nvl 모드로 보였던 글자가 사라진다.
    nvl clear
    # with Dissolve(??)) : ??의 속도로 글자가 천천히 사라진다.
    with Dissolve(2.0)

    # 예를 들어
    # nvl clear with Dissolve(4.0)
    # 위의 코드는 글자가 더 위의 코드보다 2배 정도 빠르게 사라진다.

    #yuhyen이라는 캐릭터가 말하는 것으로 나온다.
    yuhyeon "{cps=25}사람은 누구나 선을 넘을 수 있어.{/cps}"

    "{cps=25}아무런 대답이 돌아오지 않았다. 그저 멍하니 쳐다볼 뿐.{/cps}"

    "{cps=25}눈 앞의 현장을 보고도 아무런 말을 꺼낼 수 없었다{/cps}"

    yuhyeon "{cps=25}이게 외면하고 싶은 진실이야.{/cps}"

    stop music fadeout 1
    "{cps=25}그러고는 가볍게 냉소를 지었다.{/cps}"

    # scene ?? : game/images 안에 있는 ??.png 파일을 띄운다.

    scene cg 1
    with Dissolve(3.0)
    # game/images 안에 있는 cg 1.png라는 파일을 3.0의 속도로 띄운다.

    "{cps=25}겨누어진 칼끝에 전등이 불이 반사되어 빚나고 있었다.{/cps}"

    scene bg blackscreen
    with Dissolve(3.0)

    "{cps=5}양의 안식처{/cps}"

    scene bg incheon1
    with Dissolve(3.0)

    play music "music/normal scene.mp3" fadeout 1
    "{cps=25}인천의 한 거리{/cps}"

    "{cps=25}부둣가가 근처에 있어서일까? 바람이 꽤 쌀쌀하다{/cps}"

    "{cps=25}낮시간임에도 사람들이 붐빈다{/cps}"

    # show ?? at left : game/images 안에 있는 ??.png 파일을 왼쪽에 띄운다.
    # show ?? at right : game/images 안에 있는 ??.png 파일을 오른쪽에 띄운다.

    show ihyun_happy at left
    show isol_idle at right
    with Dissolve(2.0)
    # ihyun_happy.png 파일을 왼쪽에 isol_dile.png 파일을 오른쪽에 띄운다.
    # 2.0의 속도로 천천히


    ihyun "{cps=25}이렇게 가족끼리 나오는 것도 정말 오랜만이야. 그렇지?{/cps}"
    isol "{cps=25}......{/cps}"

    "{cps=25}이솔은 이현의 말에 아무런 대답도 하지 않고 무표정으로 있다.{/cps}"
    "{cps=25}이현은 애써 분위기를 띄워 보려하지만 이솔에게서 딱히 반응을 얻어낼 수 없었다.{/cps}"

    ihyun "{cps=25}진짜 그때 우체통을 열어봤을때 다른 날이랑은 느낌이 달랐다니까?{/cps}"

    "{cps=25}이현은 호들갑을 떨며 이솔에게 말을 걸었다.{/cps}"

    hide ihyun_happy
    hide isol_idle
    with Dissolve(0)

    show envelope
    with Dissolve(1.0)

    "{cps=25}며칠 전 우체통을 열어보았다.{/cps}"

    "{cps=25}평범한 고지서들 사이로 무언가 고급진 봉투가 눈에 띄었다.{/cps}"

    "{cps=25}유람선 위에서 열리는 파티의 초대장이었다.{/cps}"

    "{cps=25}깜짝 놀라 발신인을 찾아보니 상담사 K씨였다.{/cps}"

    "{cps=25}부모님을 여의고 정신적으로 힘든 시기를 보낸 동생에게 큰 힘이 되어주신 선생님이다.{/cps}"

    "{cps=25}초대장 뒤에는 쪽지가 있었다.{/cps}"

    # ihyun "대사대사대사" 이런 식으로 구성할 수도 있지만
    # 앞에 "K"(인물) "대사대사"(대사) 이런 식으로 넣을 수도 있다.
    "K" "{cps=25}요즘 많이 보지 못했네요.{/cps}"

    "K" "{cps=25}파티 즐겁게 다녀오시고 한번 찾아오세요.{/cps}"

    "{cps=25}역시 여러모로 오랫동안 도와주셨던 분이다.{/cps}"

    "{cps=25}이렇게 가끔씩 선물을 보내주시고 했는데 이번에는 유람선 여행이라니.{/cps}"

    "{cps=25}정말 설레는 기분이다.{/cps}"

    # hyde ?? : game/images 안에 있는 ??.png 파일을 천천히 숨긴다(사라지게 한다).
    hide envelope
    with Dissolve(1.0)

    show ihyun_happy at left
    show isol_idle at right
    with Dissolve(1.0)

    "{cps=25}이현은 그때 상황을 생각하다가 다시 이솔에게 말했다{/cps}"

    ihyun "{cps=25}배에서 내리고 나서 오랜만에 상담사님 찾아 뵈러 가야겠어. 이런 멋진 유람선 여행이라니.{/cps}"

    isol "{cps=25}그래... 같이 인사하러 가자...{/cps}"

    "{cps=25}이현은 이솔이 대답하는 것을 보고 다행이라는 생각을 했다.{/cps}"

    "{cps=25}평소라면 이렇게 물어보는 것에도 별로 대답하지 않을텐데...{/cps}"

    hide ihyun_happy at left
    show ihyun_idle at left

    ihyun "{cps=25}어디보자...{/cps}"

    "{cps=25}저쪽인가?{/cps}"

    "{cps=25}표지판을 따라 왔지만 부둣가가 어디에 있는지 찾을 수가 없었다.{/cps}"

    "{cps=25}길의 표지판을 보면서 따라가보려고 해도 어느 방향인지 알 수 없었다.{/cps}"

    hide ihyun_idle at left
    show ihyun_panic at left

    ihyun "{cps=25}오랜만에 나와서 길을 못찾기는 싫은데 말이지...{/cps}"

    ihyun "{cps=25}아무나 붙잡고 물어봐야겠다.{/cps}"

    "{cps=25}하지만 주변을 둘러보아도 무심하게 스쳐 지나갈 뿐이었다.{/cps}"

    ihyun "{cps=25}저기요... 라고 물어보면 한명쯤은 뒤돌아 보지 않을까?{/cps}"

    "{cps=25}혼자 생각을 하고 있는데 이솔이 언제 출발하냐는 듯 눈치를 준다.{/cps}"

    ihyun "{cps=25}어디로 가야 하는지 알아야 가든 말든 하지.{/cps}"

    hide ihyun_panic at left
    hide isol_idle at right

    "{cps=25}그 때 누군가랑 부딪혔다.{/cps}"

    show yuhyeon_idle at left
    show ihyun_panic at right
    with Dissolve(1.0)

    "{cps=25}양복을 입은 중년 남성이다.{/cps}"

    ihyun "{cps=25}아... 죄송합니다{/cps}"

    "???" "{cps=25}괜찮습니다{/cps}"

    "{cps=25}양복을 입은 중년 남자다.{/cps}"

    "{cps=25}회사원일까? 딱히 특징이 두드러지지 않는다.{/cps}"

    hide ihyun_panic at right
    show ihyun_idle at right
    with Dissolve(1.0)

    ihyun "{cps=25}저 죄송한데... 길 좀 물을 수 있을까요?{/cps}"

    "{cps=25}그러자 이름 모를 사람은 어디로 가야하는지는 듣지도 않고 대답했다.{/cps}"

    "???" "{cps=25}부둣가는 저쪽으로 가시면 됩니다.{/cps}"

    "???" "{cps=25}그럼 저는 빨리 가야 할 곳이 있어서...{/cps}"

    hide yuhyeon_idle
    with Dissolve(1.0)

    "{cps=25}그러면서 인파 속으로 빠르게 사라졌다.{/cps}"

    ihyun "{cps=25}부둣가는 저쪽... 좋아.{/25}"

    "{cps=25}그 때 이현의 머릿속에 의문이 떠올랐다.{/25}"

    hide ihyun_idle at right
    show ihyun_concerned at right

    ihyun "{cps=25}그런데... 저 사람은 내가 부둣가로 가는 것을 어떻게 안거지?{/25}"

    ihyun "{cps=25}이상해...{/25}"

    "{cps=25}아무리 생각해도 이상하다.{/25}"

    "{cps=25}사람 속마음을 읽는 초능력이라도 있는 것일까?{/25}"

    "{cps=25}그렇지 않다면 대체 어떻게?{/25}"

    "{cps=25}이현은 이솔과 같이 부두 쪽으로 걸으면서 이상한 느낌을 지울 수가 없었다.{/25}"

    hide ihyun_concerned at right
    show ihyun_concerned at left
    show isol_idle at right

    ihyun "{cps=25}솔아, 방금 전 그 사람 대체 어떻게 알고 있었던 걸까?{/25}"

    isol "{cps=25}...무엇을{/25}"

    ihyun "{cps=25}우리가 부둣가로 가려고 했다는 거 말이야.{/25}"

    "{cps=25}이솔은 이현의 말을 듣고 잠시 생각하다가 말했다.{/25}"

    isol "{cps=25}글쎄...{/25}"

    "{cps=25}이현은 괜스레 분위기만 심각해지는 것 같아 더 이상 생각하지 않기로 했다.{/25}"

    hide ihyun_concerned at left
    show ihyun_happy at left

    ihyun "{cps=25}아니야 그냥 우리 무슨 일이 벌어질지 상상이나 해보자.{/25}"
    ihyun "{cps=25}너도 기대되지 않아? 배 안에서 무슨 일이 벌어질지?{/25}"

    "{cps=25}이솔은 표정변화 없이 고개를 끄덕였다{/cps}"

    ihyun "{cps=25}뭐야, 별로 흥미 없지만 어쩔 수 없이 들어주겠다는 그 표정은...{/cps}"

    "{cps=25}그러자 이솔이 대답했다.{/cps}"

    isol "{cps=25}난 아무런 표정변화가 없었는걸?{/cps}"

    hide isol_idle atright
    with Dissolve(1.0)

    hide ihyun_happy at left
    show ihyun_idle at left

    ihyun "{cps=25}니 얼굴에 다 쓰여 있거든...{/cps}"

    hide ihyun_idle at left
    with Dissolve(1.0)

    "{cps=25}그렇게 이현과 이솔은 부둣가를 향해 걸었다.{/cps}"

    scene bg blackscreen
    with Dissolve(2.0)

    scene bg bay
    with Dissolve(1.0)

    "{cps=25}이상한 사람과 마주친 후 얼마 지나지 않아 부둣가에 도착했다.{/cps}"

    show ihyun_idle at left
    with Dissolve(1.0)

    ihyun "{cps=25}어디보자...{/cps}"

    "{cps=25}분명히 초대장에는 바이롱 호라고 적혀 있었다.{/cps}"

    "{cps=25}바이롱 호가 어떤 거지...?{/cps}"

    show isol_idle at right
    with Dissolve(1.0)

    isol "{cps=25}저거... 아니야?{/cps}"

    "{cps=25}이솔이 손을 뻗어 유람선 하나를 가리켰다.{/cps}"

    "{cps=25}유람선에 햇빛이 반사되어 빛나고 있는 것이 보인다.{/cps}"

    ihyun "{cps=25}와... 대단해.{/cps}"

    isol "{cps=25}배... 처음 본 것 처럼 말하네.{/cps}"

    hide ihyun_idle at left
    show ihyun_panic at left

    ihyun "{cps=25}배 처음 보거든?{/cps}"

    "{cps=25}이솔은 이상한 눈으로 나를 쳐다봤다.{/cps}"

    ihyun "{cps=25}왜 그렇게 나를 봐?{/cps}"

    "{cps=25}그러자 이솔은 약간 얼굴을 찌푸리며 말했다.{/cps}"

    isol "{cps=25}...아니야.{/cps}"

    hide ihyun_panic at left
    show ihyun_idle at left

    ihyun "{cps=25}왜? 무슨 일인데?{/cps}"

    "{cps=25}이현이 아무리 물어봐도 이솔은 대답해 주지 않았다.{/cps}"

    "{cps=25}아니 딱히 대답할 생각이 없어 보였다.{/cps}"

    ihyun "{cps=25}어쩔 수 없지. 나중에 말해줘.{/cps}"

    "{cps=25}이현은 그렇게 말하고 뒤로 돌아섰다.{/cps}"

    isol "{cps=25}......{/cps}"

    ihyun "{cps=25}뭐라고?{/cps}"

    "{cps=25}이솔이 뭔가 웅얼거리는 것에 이현이 반응했다.{/cps}"

    isol "{cps=25}...아니... 아무것도{/cps}"

    "{cps=25}이솔의 기분이 나빠진 것 같다.{/cps}"

    "{cps=25}무엇 때문일까?{/cps}"

    "{cps=25}이현은 정말 이해할 수 없었다.{/cps}"

    "{cps=25}이현과 이솔은 바이롱 호 쪽으로 걸어갔다.{/cps}"

    scene bg blackscreen
    with Dissolve(2.0)

    scene bg cruise
    with Dissolve(1.0)

    show staff at left
    show ihyun_idle at right
    with Dissolve(1.0)

    "staff" "{cps=25}이현씨 이솔씨 두 분 맞으신가요?{/cps}"

    ihyun "{cps=25}네 맞습니다.{/cps}"

    "{cps=25}바이롱 호 앞에는 스테프 한 명이 서 있었다.{/cps}"

    "{cps=25}스테프는 서류에 무언가를 쓰더니 우리에게 안내하기 시작했다.{/cps}"

    "staff" "{cps=25}방은 1인당 한개씩 지급될 예정이고요...{/cps}"

    "{cps=25}그렇게 한 5분정도 설명이 계속되었다.{/cps}"

    "staff" "{cps=25}...그래서 적어도 6시 까지는 유람선 2층의 테라스로 나와 주시면 됩니다.{/cps}"

    ihyun "{cps=25}그렇군요. 안내사항은 그게 끝인가요?{/cps}"

    "staff" "{cps=25}네 그렇습니다.{/cps}"

    "{cps=25}이현과 이솔은 약간 들뜬 그리고 약간 긴장한 기분으로 유람선에 올랐다.{/cps}"

    stop music fadeout 1

    scene bg blackscreen
    with Dissolve(2.0)

    scene bg hallway
    with Dissolve(1.0)

    play music "music/peace.mp3" fadeout 1

    "{cps=25}이현과 이솔은 각자의 이름이 쓰여진 방을 찾아 걸었다.{/cps}"

    show ihyun_idle at left
    show isol_idle at right
    with Dissolve(1.0)

    ihyun "{cps=25}생각보다 방이 많지 않네?{/cps}"

    "{cps=25}이현은 밖에서 본 것보다 방의 개수가 적다는 것에 신기해했다.{/cps}"

    "{cps=25}그리고 이현과 이솔의 방은 복도의 맨 끝이었다.{/cps}"

    "{cps=25}맨 끝이라고 하기에는 배의 구조가 조금 특이했다.{/cps}"

    "{cps=25}복도의 맨 끝이라고 말하기 보다는 입구의 정 반대편이라고 하는 것이 좋을 것이다.{/cps}"

    ihyun "{cps=25}들은 대로 문이 잠겨 있지는 않네{/cps}"

    ihyun "{cps=25}밖에서 잠글 수단도 없어.{/cps}"

    "{cps=25}몸을 힘주어 열자 생각보다 넒은 방 안이 보였다.{/cps}"

    ihyun "{cps=25}우와 여기 방 진짜 큰데?{/cps}"

    ihyun "{cps=25}방이 적게 있던 이유가 있었네.{/cps}"

    "{cps=25}이솔은 그 말에 맞장구를 쳤다.{/cps}"

    isol "{cps=25}...그러게{/cps}"

    ihyun "{cps=25}너 방은 내 옆이구나{/cps}"

    "{cps=25}이현은 하품을 하며 말했다.{/cps}"

    ihyun "{cps=25}혹시 이따가 다섯시 쯤에 나를 깨우러 와줄 수 있어?{/cps}"

    ihyun "{cps=25}나 알람소리 잘 못 들으니까 말이야.{/cps}"

    "{cps=25}이솔은 아무 말 없이 고개를 끄덕였다.{/cps}"

    hide ihyun_idle at left
    show ihyun_happy at left

    ihyun "{cps=25}고마워{/cps}"

    ihyun "{cps=25}오랜만에 운전했더니 좀 피곤하네. 먼저 들어갈께!{/cps}"

    play sound "sounds/Door2.wav" fadeout 1

    hide ihyun_happy at left
    with Dissolve(1.0)

    "{cps=25}이현은 이솔에게 손을 흔들고 방으로 들어갔다.{/cps}"

    scene bg blackscreen
    with Dissolve(3.0)

    scene bg ihyun room
    with Dissolve(3.0)

    show isol_idle at right
    with Dissolve(1.0)

    isol "{cps=25}일어나{/cps}"

    show ihyun_idle at left
    with Dissolve(1.0)
    "{cps=25}아... 벌써 시간이 이렇게 되었나{/cps}"

    ihyun "{cps=25}벌써 5시야?{/cps}"

    "{cps=25}이솔은 고개를 가로저으며 말했다.{/cps}"

    isol "{cps=25}아니 5시 20분.{/cps}"

    hide ihyun_idle at left
    show ihyun_panic at left

    ihyun "{cps=25}왜 5시 20분이야...?{/cps}"

    ihyun "{cps=25}5시에 안일어나도 계속 깨워야지.{/cps}"

    isol "{cps=25}깨워도 안일어나길래 계속 깨웠어.{/cps}"

    "{cps=25}이쯤 되면 이현이 딱히 할말은 없었다.{/cps}"

    hide ihyun_panic at left
    show ihyun_happy at left

    ihyun "{cps=25}요즘 좀 많이 피곤한가 보다. 잠깐 잔 건데 이렇게 오래 자버리다니.{/cps}"

    ihyun "{cps=25}준비는 다 끝났어?{/cps}"

    isol "{cps=25}응...{/cps}"

    isol "{cps=25}오빠만 준비하면 돼.{/cps}"

    hide isol_idle at right
    with Dissolve(1.0)

    ihyun "{cps=25}알았어 금방 준비하고 나갈게.{/cps}"

    "{cps=25}배가 위 아래로 움직이는 것, 그리고 밖에서 물을 가르는 소리가 들린다.{/cps}"

    ihyun "{cps=25}드디어 파티의 시작이구나.{/cps}"

    "{cps=25}이현은 준비를 마친 뒤 마지막으로 외투를 입고 방문을 나섰다.{/cps}"

    stop music fadeout 3

    scene bg blackscreen
    with Dissolve(2.0)

    scene bg partyroom
    with Dissolve(1.0)

    play music "music/dream of you.mp3" fadeout 1

    show ihyun_idle at slightright
    show isol_idle at right
    with Dissolve(1.0)

    "{cps=25}이현과 이솔은 방에서 나와 테라스로 걸어갔다{/cps}"

    "{cps=25}테라스에는 먹음직스러운 음식들이 구비되어 있다.{/cps}"

    ihyun "{cps=25}하나 둘 셋...{/cps}"

    ihyun "{cps=25}이렇게 큰 배에 사람이 적어서 쾌적하고 좋네.{/cps}"

    "{cps=25}주위를 둘러보니 낯이 익은 얼굴이 조금씩 보인다.{/cps}"

    ihyun "{cps=25}기분 탓이겠지.{/cps}"

    isol "{cps=25}저쪽 가서 뭐 좀 먹자... 배고파{/cps}"

    "{cps=25}이솔은 구석 자리를 가리키며 말했다.{/cps}"

    ihyun "{cps=25}그렇게 하자.{/cps}"

    "{cps=25}식사를 가볍게 하며 사람들과 인사를 나눈다.{/cps}"

    "{cps=25}웨이터들은 분주하게 돌아다니며 음식을 나른다.{/cps}"

    show yuhyeon_idle at left
    with Dissolve(1.0)

    "{cps=25}인사를 하면서 돌아다니다가 아까 마주친 사람을 만났다.{/cps}"

    hide ihyun_idle at slightright
    show ihyun_happy at slightright

    ihyun "{cps=25}어...? 안녕하세요{/cps}"

    "{cps=25}그러자 그 남자는 신기하다는 듯이 대답했다{/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_happy at left

    "???" "{cps=25}여기서 또 만나게 되는군요.{/cps}"

    "{cps=25}그리고 손을 내밀며 말했다.{/cps}"

    yuhyeon "{cps=25}안녕하세요. 김유현이라 합니다.{/cps}"

    "{cps=25}이현은 너무나 신기한 우연에 다짜고짜 질문을 했다.{/cps}"

    hide ihyun_happy at slightright
    show ihyun_idle at slightright

    ihyun "{cps=25}혹시 아까 어떻게 우리가 부둣가로 가는 줄 알고 있었죠?{/cps}"

    hide yuhyeon_happy at left
    show yuhyeon_idle at left

    yuhyeon "{cps=25}별 것 아닙니다{/cps}"

    yuhyeon "{cps=25}그저 관찰을 했을 뿐이지요.{/cps}"

    "{cps=25}이현이 무슨 소리냐는 듯한 반응을 보이자 김유현은 웃으며 말했다.{/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_happy at left

    yuhyeon "{cps=25}아까 전 길가의 표지판 말입니다.{/cps}"

    yuhyeon "{cps=25}세세한 장소가 많이 적혀 있었죠?{/cps}"

    yuhyeon "{cps=25}그런데 중간에 보면 부러진 부분이 하나 있었을 겁니다.{/cps}"

    "{cps=25}이현은 설마하는 표정으로 김유현을 바라보았다.{/cps}"

    "{cps=25}김유현은 계속 웃으며 말했다.{/cps}"

    yuhyeon "{cps=25}제가 이 근처에 살거든요.{/cps}"

    yuhyeon "{cps=25}어떤 표지판이 없어졌을지 주변에 있는 것을 생각해보니 부둣가일 것 같더라고요.{/cps}"

    yuhyeon "{cps=25}그래서 부둣가의 방향을 말씀드린 거죠.{/cps}"

    "{cps=25}그리고 김유현은 와인잔을 기울여 술을 마시고 말했다.{/cps}"

    hide yuhyeon_happy at left
    show yuhyeon_idle at left

    yuhyeon "{cps=25}근데 아직 성함을 안 말해주셨는데요?{/cps}"

    hide ihyun_idle at slightright
    show ihyun_panic at slightright

    "{cps=25}이현은 당황하며 말했다.{/cps}"

    ihyun "{cps=25}아... 제 이름은 이.. 이현이라 합니다.{/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_happy at left

    yuhyeon "{cps=25}이이현이요?{/cps}"

    hide ihyun_panic at slightright
    show ihyun_idle at slightright

    ihyun "{cps=25}아니 이현이요. 이 현{/cps}"

    "???" "{cps=25}둘이 무슨 얘기 하고 있나요?{/cps}"

    "{cps=25}얘기를 하고 있는데 누군가 다가왔다.{/cps}"

    hide yuhyeon_happy at left
    with Dissolve(1.0)

    show yuhyeon_idle at slightleft
    show hyunjoo_happy at left
    with Dissolve(1.0)

    "???" "{cps=25}오랜만이에요 김유현씨.{/cps}"

    "{cps=25}한 여자가 다가와서 말했다.{/cps}"

    hide yuhyeon_idle at slightleft
    show yuhyeon_panic at slightleft

    yuhyeon "{cps=25}당신을 여기서 만날 줄은 몰랐는데 말이죠.{/cps}"

    yuhyeon "{cps=25}고현주씨{/cps}"

    "{cps=25}버건디 민무늬 스웨터에 몸에 붙는 치마를 입고 나타난 사람의 이름은 고현주였다. {/cps}"

    ihyun "{cps=25}두분이서는 아는 사이이신가요?{/cps}"

    hyunjoo "{cps=25}예전에 만났죠.{/cps}"

    hyunjoo "{cps=25}아주 재미있는 일로 말이에요.{/cps}"

    "{cps=25}고현주는 웃으며 그렇게 말했다.{/cps}"

    "{cps=25}이현이 물어보려는 찰나 고현주가 다시 입을 열었다.{/cps}"

    hide hyunjoo_happy at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}하지만 별로 말해주고 싶지는 않네요.{/cps}"

    hyunjoo "{cps=25}저쪽에 계신 분은 동생분인가요?{/cps}"

    "{cps=25}이현이 바라보니 고현주는 이솔을 보고 있었다.{/cps}"

    ihyun "{cps=25}아 네...{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_happy at left

    hyunjoo "{cps=25}재미있군요.{/cps}"

    hide hyunjoo_happy at left
    with Dissolve(1.0)

    hide yuhyeon_panic at slightleft
    show yuhyeon_panic at left
    with Dissolve(1.0)

    "{cps=25}이현이 무엇이 재미있는지를 물어보기도 전에 고현주는 등을 돌려 원래 있던 자리로 돌아갔다.{/cps}"

    hide yuhyeon_panic at left
    show yuhyeon_idle at left

    yuhyeon "{cps=25}신경 쓰지마세요{/cps}"

    ihyun "{cps=25}아 말씀 편하게 하셔도 됩니다.{/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_happy at left

    yuhyeon "{cps=25}아 그런가?{/cps}"

    yuhyeon "{cps=25}그럼 편하게 하겠네.{/cps}"

    "{cps=25}김유현은 웃으며 말했다.{/cps}"

    "{cps=25}그 때 이솔이 이현을 불렀다.{/cps}"

    ihyun "{cps=25}왜 그래? 어디 아파?{/cps}"
    isol "{cps=25}아니 그런건 아니고.{/cps}"

    "{cps=25}그렇게 사람들과 대화하고 얼마나 지났을까.{/cps}"

    "{cps=25}스태프가 큰 상자를 들고 나왔다{/cps}"

    "staff" "{cps=25}여러분 오래 기다리셨습니다.{/cps}"

    "staff" "{cps=25}모두 파티는 잘 즐기고 계신가요?{/cps}"

    "{cps=25}사람들이 웃으면서 그렇다고 말한다.{/cps}"

    "staff" "{cps=25}저희도 여러분들이 그렇게 느끼신다니 다행이라고 생각합니다.{/cps}"

    "staff" "{cps=25}여러분들을 위한 특별한 선물이 있습니다.{/cps}"

    "{cps=25}그리고 가지고 나온 상자를 가리키며 말을 이어 나갔다.{/cps}"

    "staff" "{cps=25}누가 그러더군요 선물은 뜯는 순간이 가장 기대된다고 말이죠. {/cps}"

    "staff" "{cps=25}저희는 잠시 자리를 비켜 드릴테니 열어 보고 싶으신 분이 나와서 열어 보시면 됩니다.{/cps}"

    "staff" "{cps=25}그럼 이만 남은 시간 즐겁게 보내시기 바랍니다.{/cps}"

    "{cps=25}그러고는 인사를 하고 물러났다.{/cps}"

    ihyun "{cps=25}저게 뭘까?{/cps}"

    "{cps=25}사람들은 서로 주변의 친한 사람들과 얘기를 하거나 혼자 웃으며 저게 무엇일지 생각하고 있는 분위기였다.{/cps}"

    hide ihyun_idle at slightright
    show ihyun_happy at slightright

    ihyun "{cps=25}저거 열어보고 싶지 않아?{/cps}"

    "{cps=25}그렇게 이솔에게 말하고 이솔을 바라보았지만 이솔은 아무런 대답을 하지 않았다.{/cps}"

    "{cps=25}어디선가 풍덩 하는 소리가 들렸고 이솔이 잠시 동요했다.{/cps}"

    hide ihyun_happy at slightright
    show ihyun_idle at slightright

    ihyun "{cps=25}왜 그래?{/cps}"

    "{cps=25}하지만 이솔은 아무런 대답을 하지 않았다.{/cps}"

    ihyun "{cps=25}무슨 소리인지 알아보고 올까?{/cps}"

    "{cps=25}그러자 이솔은 아주 약간 고개를 끄덕였다.{/cps}"

    ihyun "{cps=25}그래 갔다올게. 어디 가지 말고 기다려.{/cps}"

    hide ihyun_idle at slightright
    with Dissolve(1.0)

    stop music fadeout 3

    scene bg blackscreen
    with Dissolve(2.0)

    scene bg cruisehall
    with Dissolve(1.0)

    play music "music/Cruise Whitnoise.mp3" fadeout 1
    show ihyun_idle at left
    with Dissolve(1.0)

    ihyun "{cps=25}무슨 소리지?{/cps}"

    "{cps=25}이현은 배의 바깥쪽 복도에서 무슨일이 벌어지는지 확인을 했다.{/cps}"

    "{cps=25}배의 뒤편에는 불빛이 있었다.{/cps}"

    ihyun "{cps=25}모터보트?{/cps}"

    "{cps=25}이상한 일이다. 모터보트가 왜 여기에 있을까?{/cps}"

    "{cps=25}모터보트의 진행방향은 유람선과 반대 방향이었다.{/cps}"

    "{cps=25}옷을 자세히 보니 아까 전까지 사람들에게 서빙을 해주던 스태프들이다{/cps}"

    ihyun "{cps=25}왜 갑자기 떠나는 거지?{/cps}"

    "{cps=25}뭐 중요한 거라도 두고 온건가?{/cps}"

    "{cps=25}하지만 저렇게 단체로 갈 일은 아니라고 생각했다.{/cps}"

    ihyun "{cps=25}대체 무슨 일이야.{/cps}"

    ihyun "{cps=25}단체로 집에 가스 불 안 끄고 나온 것도 아닐테고.{/cps}"

    "{cps=25}이현은 복잡해진 머릿속을 달래기 위해 주머니에서 담배를 꺼냈다.{/cps}"

    "{cps=25}그리고 불을 붙이려는 순간{/cps}"

    play sound "sounds/scream.mp3"

    "???" "{cps=25}{color=f00}{size=+20}꺄아아아아아악{/size}{/color}{/cps}"

    "???" "{cps=25}{color=f00}{size=+10}뭐야 이게!{/size}{/color}{/cps}"

    "{cps=25}갑자기 원래 있던 곳에서 비명이 들렸다.{/cps}"

    stop music fadeout 3

    scene bg blackscreen
    with Dissolve(2.0)

    scene bg partyroom
    with Dissolve(1.0)

    play music "music/dream of you.mp3" fadeout 1

    show hyunjoo_happy at left
    with Dissolve(1.0)

    hyunjoo "{cps=25}이게 뭘까요?{/cps}"

    "{cps=25}고현주가 웃으며 사람들의 앞에 나섰다.{/cps}"

    show jungyu_idle at right
    with Dissolve(1.0)

    jungyu "{cps=25}글쎄 모르지.{/cps}"

    jungyu "{cps=25}먹을 거라도 되려나?{/cps}"

    "{cps=25}고현주는 상자를 만지며 말했다.{/cps}"

    hyunjoo "{cps=25}일리 있는 말이에요.{/cps}"

    hyunjoo "{cps=25}우리는 지금까지 음식을 많이 먹긴 했는데 디저트 종류는 아무것도 나오지 않았죠?{/cps}"

    hyunjoo "{cps=25}그럼 케이크 같은 것이 아닐까요?{/cps}"

    show siwook_happy at slightright
    with Dissolve(1.0)

    siwook "{cps=25}저게 만약 케이크면 내가 본 케이크 중에서는 가장 큰 것이 되겠군.{/cps}"

    "{cps=25}그러자 박준규는 약간 싫다는 표정을 지으며 말했다.{/cps}"

    hide jungyu_idle at right
    show jungyu_cold at right

    jungyu "{cps=25}저만한 크기의 케이크라니.{/cps}"

    "{cps=25}고현주는 의외라는 표정을 지으며 물었다.{/cps}"

    hide hyunjoo_happy at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}케익을 싫어하시나요? 저는 좋은데... 특히 생크림 케이크가 말이죠.{/cps}"

    hide jungyu_cold at right
    show jungyu_idle at right

    jungyu "{cps=25}아니 케이크의 크림이 싫어서 별로 좋아하지 않는 건데...{/cps}"

    jungyu "{cps=25}디저트 종류라면 케이크가 아닌 다른 것이 나왔으면 좋겠군.{/cps}"

    "{cps=25}고현주는 손을 들고 말했다.{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_happy at left

    hyunjoo "{cps=25}그렇다면 상자를 제가 열어도 될까요?{/cps}"

    hide jungyu_idle at right
    show jungyu_happy at right

    jungyu "{cps=25}아니 내가 열게.{/cps}"

    jungyu "{cps=25}당신이 열면 케이크가 아니어도 케이크가 될 것만 같아서 말이야.{/cps}"

    "{cps=25}사람들이 크게 웃는다.{/cps}"

    hide hyunjoo_happy at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}정말이지... 당신이 한번 열어봐요.{/cps}"

    "{cps=25}고현주는 못말린다는 듯 웃으며 한 발짝 물러섰다.{/cps}"

    "{cps=25}그리고 상자를 완전히 열고 안쪽을 보는 박준규의 몸동작이 멈췄다.{/cps}"

    stop music fadeout 3

    hyunjoo "{cps=25}뭘 그렇게 혼자만 봐요?{/cps}"

    "{cps=25}그리고 한 발짝 다가서며 말했다.{/cps}"

    stop music fadeout 1

    hyunjoo "{cps=25}궁금하게....?{/cps}"

    hide hyunjoo_happy at left
    show hyunjoo_pale at left

    hyunjoo "{cps=5}이게...뭐야?{/cps}"

    scene bg blackscreen
    with Dissolve(2.0)

    scene cg 2
    with Dissolve(2.0)

    play music "music/bad events.mp3" fadeout 1

    nvle "{cps=25}아비규환이다{/cps}"
    nvle "{cps=25}고현주는 박스에서 멀어져 손톱을 물어 뜯으며 혼잣말을 중얼거리고 있었고.{/cps}"
    nvle "{cps=25}조정은은 비명을 지르고 있었다.{/cps}"
    nvle "{cps=25}구토를 하는 사람, 그리고 울고 있는 사람이 보인다.{/cps}"
    nvle "{cps=25}단테의 신곡과도 같은 분위기이다.{/cps}"
    nvle "{cps=25}김유현은 상자에서 물러서 심각하게 무언가를 생각하는 듯 하다.{/cps}"
    nvle "{cps=25}방금 전까지 파티가 일어났다고 생각하기 어려웠다.{/cps}"
    nvl clear
    with Dissolve(2.0)

    show ihyun_panic at left
    with Dissolve(1.0)

    ihyun "{cps=25}이게 무슨 일이죠?{/cps}"

    "{cps=25}이현은 김유현에게 다가가 물었다.{/cps}"

    show yuhyeon_concerned at right

    "{cps=25}하지만 김유현은 대답하지 않고 단지{/cps}"

    yuhyeon "{cps=25}한태현... 당신이 왜 여기에{/cps}"

    "{cps=25}라는 말만 반복해서 하고 있었다.{/cps}"

    "{cps=25}그리고 이현의 눈에는 김유현의 몸에 가려 제대로 보이지 않았던 것이 보였다.{/cps}"

    hide yuhyeon_concerned at right
    with Dissolve(1.0)
    hide ihyun_panic at left
    show ihyun_pale at left

    ihyun "{cps=1}....시.....체?{/cps}"

    "{cps=25}이현은 빠르게 이솔을 찾았다.{/cps}"

    hide ihyun_pale at left
    show ihyun_panic at left

    ihyun "{cps=25}솔아!!{/cps}"

    show isol_pale at right

    "{cps=25}그리고 의자에 앉아 바닥을 보고 있는 이솔에게 다가갔다.{/cps}"

    ihyun "{cps=25}솔아 괜찮아? 무슨 일이 있었던 거야...?{/cps}"

    "{cps=25}이솔은 잠시 멍하게 있다가 대답했다.{/cps}"

    isol "{cps=10}...저기...상자에서{/cps}"

    isol "{cps=10}...상자에서...{/cps}"

    isol "{cps=10}...시체가... 나왔어...{/cps}"

    isol "{cps=10}웨이터들이... 선물로 준... 상자에서{/cps}"

    "{cps=25}이현은 갑자기 왜 이런 상황이 일어났는지 이해할 수 없었다.{/cps}"

    hide ihyun_panic at left
    show ihyun_pale at left

    ihyun "{cps=25}왜...?{/cps}"

    ihyun "{cps=25}갑자기 이게 무슨 상황이야...{/cps}"

    stop music fadeout 3

    scene bg blackscreen
    with Dissolve(3.0)

label ninth:

    play music "music/quiet.mp3" fadeout 1

    "{cps=25}아수라장이다.{/cps}"
    "{cps=25}사람들의 말소리가 섞여 무슨 말이 들리는지 구분이 되지 않았다.{/cps}"
    "{cps=25}이현은 그저 이솔의 손을 잡고 있다.{/cps}"

    scene bg partyroom
    with Dissolve(3.0)

    "{cps=25}감은 눈을 떴다.{/cps}"
    "{cps=25}하지만 꿈이 아니기 때문에 바뀌는 것은 아무것도 없었다.{/cps}"

    show ihyun_pale at left

    ihyun"{cps=25}괜찮아…{/cps}"
    ihyun"{cps=25}괜찮을거야…{/cps}"

    show yuhyeon_idle at right
    yuhyeon"{cps=25}잠시 집중 좀 해 주십시오.{/cps}"

    "{cps=25}김유현이 가운데로 나서며 주의를 끌었다. {/cps}"

    yuhyeon"{cps=25}일단은 스탭들은 다 어디에 있죠?{/cps}"
    hide  ihyun_pale
    show ihyun_idle at left
    ihyun"{cps=25}아까전에 배 뒤쪽에서 탈출하는걸 봤어요.{/cps}"
    ihyun"{cps=25}그때는 무슨 상황인지 몰라서…{/cps}"

    "{cps=25}김유현은 잠시 고민하는 듯 했다.{/cps}"

    yuhyeon"{cps=25}아무래도 일단 시체를 잠시 살펴봐야겠군요.{/cps}"

    pause(3.0)
    "{cps=25}시체를 살피며 김유현은 말을 이어나갔다. {/cps}"

    yuhyeon"{cps=25}이분의 이름은 한태현씨입니다. {/cps}"
    yuhyeon"{cps=25}직업은 검사이고…{/cps} "

    hide  ihyun_idle
    show siwook_idle  at left
    "{cps=25}그 때 정시욱이 끼어들며 말했다. {/cps}"

    siwook"{cps=25}그걸 당신이 어떻게 알지?{/cps}"
    siwook"{cps=25}저 사람이 검사라는 걸 당신이 어떻게 알아?{/cps}"
    hide siwook_idle at left
    show siwook_cold at left
    siwook"{cps=25}혹시 당신이 이 사건을 일으킨 주범 아니야?{/cps}"

    yuhyeon"{cps=25}저는 전직 형사입니다.{/cps}"
    yuhyeon"{cps=25}예전에 한태현 검사와 같이 사건 하나를 수사했었죠.{/cps}"
    yuhyeon"{cps=25}그 사건 이후로 일을 그만두긴 했습니다만..{/cps}"
    yuhyeon"{cps=25}이제 충분한 설명이 되셨나요?{/cps}"

    "{cps=25}시체를 살펴보던 김유현이 이상하다는 듯 말했다.{/cps}"
    hide yuhyeon_idle at right
    show yuhyeon_concerned at right
    yuhyeon"{cps=25}이상한 글귀가 쓰여 있군요{/cps}"
    yuhyeon"{cps=25}양들은 목자를 욕되게 하지 말라…?{/cps}"

    "{cps=25}그 말을 하는 순간 선상에 있던 대부분의 사람들이 움찔했다. {/cps}"
    hide yuhyeon_concerned at right
    show yuhyeon_cold at right
    yuhyeon"{cps=25}뭔가 알고 있으신 게 있나보군요.{/cps}"
    yuhyeon"{cps=25}이게 무엇이죠?{/cps}"
    yuhyeon"{cps=25}정시욱씨 이번에는 당신이 제 질문에 대답해보지 않으시겠습니까?{/cps}"

    "그러자 정시욱은 크게 당황하며 말했다."

    hide siwook_cold at left
    show siwook_angry at left
    siwook"{cps=25}아니 난 몰라! 모르는 일이라고!{/cps}"

    yuhyeon"{cps=25}그렇습니까?{/cps/}"
    yuhyeon"{cps=25}상관 없습니다. 다른 사람들도 다 아는 것 같으니.{/cps}"

    "그리고 김유현은 고현주를 바라보며 물었다. "

    hide yuhyeon_cold
    show yuhyeon_idle at right
    yuhyeon"{cps=25}고현주씨 대답해 주시죠.{/cps}"

    hide siwook_angry
    show hyunjoo_idle at left
    "{cps=25}고현주는 잠시 생각하다가 심호흡을 한번 하고 말을 꺼냈다.{/cps}"
    hyunjoo"{cps=25}어차피 제가 말을 안해도 다른 사람들이 말해야 될 테니…{/cps}"
    hyunjoo"{cps=25}좋아요. 말씀드리죠.{/cps}"
    hyunjoo"{cps=25}김유현씨 당신이 한태현 검사와 같이 수사한 마지막 사건이 뭐죠?{/cps}"
    "{cps=25}김유현이 대답을 꺼내기 전에 고현주가 다시 말을 이어 나갔다. {/cps}"
    hyunjoo"{cps=25}그 사건은 아마 지금은 파일도 남아 있지 않겠지만 그 시절에 경찰에서는 선백교 사건이라 불렀죠.{/cps}"
    hyunjoo"{cps=25}그거에요 그냥{/cps}"
    hyunjoo"{cps=25}현재는 사라진… {/cps}"
    hyunjoo"{cps=25}선백교의 7가지 교리 중 하나죠.{/cps}"

    "{cps=25}그러고 고현주는 주위를 한번 둘러 보았다. {/cps}"

    hyunjoo"{cps=25}사실 여기 와서 사람들을 보고 무언가 잘못되었다는 생각을 많이 했죠.{/cps}"
    hyunjoo"{cps=25}아는 사람들이 너무 많았거든요.{/cps}"
    hyunjoo"{cps=25}결국 이런 일이 터져버렸군요.{/cps}"

    "{cps=25}그리고 잠시 숨을 고르고 말했다. {/cps}"

    hyunjoo"{cps=25}조금 더 저 말을 풀어 쓰자면…{/cps}"
    hyunjoo"{cps=25}양들은 목자를 욕되게 하지 말라.{/cps}"
    hyunjoo"{cps=25}여기서 양들은 신도, 또는 일반적인 사람을 의미하죠.{/cps}"
    hyunjoo"{cps=25}그리고 목자는 신을 의미하고 있죠.{/cps}"
    hyunjoo"{cps=25}사실 당신들도 다 알고있지 않나요?{/cps}"
    hyunjoo"{cps=25}대답해 보시죠.{/cps}"

    "{cps=25}그러자 몇몇 사람들이 동요하는 것이 보인다. {/cps}"

    hide yuhyeon_idle
    show yuhyeon_concerned at right
    yuhyeon"{cps=25}그렇다면 그 말뜻은…{/cps}"
    yuhyeon"{cps=25}한태현은 신을 부정했고 수사를 했기 때문에 죽었다는 말인가?{/cps}"
    hyunjoo"{cps=25}살인자의 생각은 모르겠지만 아마도…{/cps}"
    hyunjoo"{cps=25}그렇게 해석되겠죠.{/cps}"

    "{cps=25}정시욱이 큰 소리로 외쳤다.{/cps}"

    show siwook_angry
    siwook"{cps=25}우리는 다 죽을거야!{/cps}"
    siwook"{cps=25}이게 다 선백교의 품에서 벗어났기 때문이라고!{/cps}"
    hide hyunjoo_idle
    show hyunjoo_cold at left
    hyunjoo"{cps=25}이분이 갑자기… 무슨 말씀을 하시는거에요.{/cps}"
    hyunjoo"{cps=25}이게 신이 벌인 행동이라 생각하는건가요?{/cps}"

    "{cps=25}정시욱은 화를 내며 말했다. {/cps}"

    siwook"{cps=25}여기있는 사람들은 다 선백교에서 나온 사람들이라고.{/cps}"
    siwook"{cps=25}다 하나씩 죽을거야.{/cps}"
    siwook"{cps=25}우리가 목자를 떠나왔기 때문에 죽는거라고!{/cps}"
    hyunjoo"{cps=25}정말 말이 안통하는 상대네요.{/cps}"
    hyunjoo"{cps=25}뭐? 목자를 떠나왔기 때문에 죽는다고?{/cps}"
    hyunjoo"{cps=25}그저 우리에게 원한이 있어서 우리를 모은거겠지.{/cps}"
    hyunjoo"{cps=25}말도 안 되는 소리 좀 하지 마세요.{/cps}"

    "{cps=25}조정은이 나서서 말했다. {/cps}"

    hide siwook_angry
    show jungeun_pale
    jungeun "{cps=25}그러면 우리는 대체 왜 여기에 있는 거에요?{/cps}"
    jungeun "{cps=25}저는 아무런 죄를 짓지 않았다고요!{/cps}"
    hide jungeun_pale

    "{cps=25}그 소리에 사람들이 웅성거린다.{/cps}"

    show jungyu_pale
    "박준규" "{cps=25}맞아! 나도 죄를 짓지 않았어.{/cps}"
    "박준규" "{cps=25}대체 왜 우리가 여기 있는 거야!{/cps}"
    hide jungyu_pale

    "{cps=25}쾅!{/cps}"
    "{cps=25}김유현이 테이블을 거칠게 내려쳤다.{/cps}"

    hide yuhyeon_concerned
    show yuhyeon_angry at right
    yuhyeon"{cps=25}모두… 조용히 하십시오.{/cps}"
    yuhyeon"{cps=25}말이 되든 안 되든…{/cps}"
    yuhyeon"{cps=25}우리가 여기에 고립되었다는 사실은 변치 않습니다. {/cps}"
    yuhyeon"{cps=25}그리고 우리를 죽이려 한다는 사실도 변하지 않죠.{/cps}"

    "{cps=25}김유현은 코트의 깃을 고치며 말했다. {/cps}"

    hide yuhyeon_angry
    show yuhyeon_idle at right
    yuhyeon"{cps=25}지금 다들 핸드폰을 확인해 보시면 알 수 있을 겁니다.{/cps}"
    yuhyeon"{cps=25}현재 전파가 터지지 않죠.{/cps}"

    "{cps=25}이현은 주머니의 휴대폰을 꺼내 통신 상태를 확인했다.{/cps}"
    "{cps=25}정말 전파가 터지지 않았다.{/cps}"

    siwook"{cps=25}이게 뭐야!{/cps}"
    yuhyeon"{cps=25}중요한 건 변하지 않습니다. {/cps}"
    yuhyeon"{cps=25}누군가가 우리를 죽이려 한다는 사실입니다.{/cps}"

    hide yuhyeon_angry
    hide hyunjoo_cold

    jump tenth

    # scene 10: 방안
label tenth:

    scene bg ihyun room with dissolve
    pause (1.0)
    show ihyun_concerned at right
    ihyun"{cps=25}이게 어떻게 된 일이지…{/cps}"

    "{cps=25}아무리 생각해 봐도 이해할 수 없다.{/cps}"
    "{cps=25}지금 이 상황이 어떤 상황인지.{/cps}"
    "{cps=25}무슨 행동을 해야 하는지 알 수 없었다.{/cps}"
    "{cps=25}이현은 옆에 앉아있는 이솔을 보았다.{/cps}"

    ihyun"{cps=25}솔아 괜찮아?{/cps}"

    show isol_idle at left
    "{cps=25}이솔은 고개를 가로저었다. {/cps}"
    hide ihyun_concerned at right
    show ihyun_idle at right
    ihyun"{cps=25}그래… 그렇겠지.{/cps}"

    "{cps=25}그런 상황을 겪고도 괜찮다면 오히려 그게 이상한 상황일 것이다. {/cps}"
    "{cps=25}아까 전의 상황도 전부 기억나지 않는다.{/cps}"
    "{cps=25}너무 혼란스러운 상황이었기에{/cps}"

    isol"{cps=25}나 이제 혼자 있고 싶어.{/cps}"
    ihyun"{cps=25}아… 그래.{/cps}"
    ihyun"{cps=25}무슨 일이 있으면 불러도 괜찮아. 바로 옆방이니까.{/cps}"
    ihyun"{cps=25}문은 잘 닫고 있으렴.{/cps}"

    "{cps=25}이현은 문을 나서기 전에 이솔을 바라보았다. {/cps}"
    "{cps=25}이솔은 평상시보다 약간 어두운 얼굴로 침대에 앉아 있었다. {/cps}"

    hide ihyun_idle
    hide  isol_idle

    stop music fadeout 1

    jump eleventh

    # scene 11: 복도
label eleventh:
    scene bg cruisehall with dissolve
    pause (1.0)

    play music "music/bizarre.mp3" fadeout 1

    "{cps=25}달칵!{/cps}"
    "{cps=25}문이 닫히는 소리가 난다. {/cps}"
    "{cps=25}잠시 뒤 문이 잠기는 소리가 들린다. {/cps}"
    "{cps=25}이현은 그제서야 안심한듯 발걸음을 옮긴다. {/cps}"
    show yuhyeon_idle at left
    yuhyeon"{cps=25}또 보는군.{/cps}"
    "{cps=25}뒤에서 김유현이 불렀다. {/cps}"
    menu:
        "무시한다":
                jump ffirst
        "무슨일인지 물어본다.":
                jump fsecond
label fsecond:
    "{cps=25}이현은 경계를 늦추지 않으며 대꾸했다. {/cps}"
    show ihyun_idle at right
    ihyun"{cps=25}무슨 일이시죠?{/cps}"
    jump ffirst

label ffirst:
    yuhyeon"{cps=25}그저 궁금한 것이 있어서 불렀네.{/cps}"
    yuhyeon"{cps=25}여기는 다른 사람이 들을 수도 있으니 위로 올라가는게 어떤가?{/cps}"
    "{cps=25}이현은 잠시 생각하다가 대답했다.{/cps}"
    ihyun"{cps=25}아니요. 여기서 얘기하죠.{/cps}"
    ihyun"{cps=25}여기라면 다른 사람이 있으니 안전할 거라는 생각이 드네요.{/cps}"

    "{cps=25}김유현은 그 말을 듣고 쓰게 웃었다. {/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_happy at left
    yuhyeon"{cps=25}날 못믿는 모양이군{/cps}"
    yuhyeon"{cps=25}이해하네.{/cps}"
    yuhyeon"{cps=25}이런 상황이라면 누구라도 믿기 힘든 것이 사실이지.{/cps}"
    "{cps=25}그러고는 주머니에서 담배를 꺼냈다.{/cps}"

    hide yuhyeon_happy
    show yuhyeon_idle at left
    yuhyeon"{cps=25}혹시 담배 피나? 아니면 냄새를 별로 좋아하지 않는다거나.{/cps}"
    ihyun"{cps=25}담배는 피우지 않습니다만…{/cps}"
    yuhyeon"{cps=25}옆에서 피는 것은 별로 신경쓰지 않는다는 말이군.{/cps}"
    "{cps=25}김유현이 담배에 불을 붙이며 말했다. {/cps}"
    ihyun"{cps=25}역시 눈치가 빠르시네요.{/cps}"
    yuhyeon"{cps=25}전직 형사로써 기본 소양이지.{/cps}"
    yuhyeon"{cps=25}아무튼 내가 묻고 싶은 것은 따로 있네.{/cps}"
    yuhyeon"{cps=25}자네와 이솔은 여기에 어떻게 오게 되었지?{/cps}"
    ihyun"{cps=25}저희는 어느 상담사분의 초대장을 받고 오게 되었습니다. {/cps}"
    yuhyeon"{cps=25}상담사의 이름을 혹시 알 수 있나?{/cps}"
    "{cps=25}이현은 고개를 가로저었다.{/cps}"
    ihyun"{cps=25}그저 상담사 K라고만…{/cps}"
    yuhyeon"{cps=25}그렇군…{/cps}"
    yuhyeon"{cps=25}그렇다면…{/cps}"
    yuhyeon"{cps=25}선백교와는 무슨 관계가 있지?{/cps}"

    hide ihyun_idle
    show ihyun_happy at right
    ihyun"{cps=25}잠시만요.{/cps}"
    ihyun"{cps=25}제가 대답만 하는 것은 아무래도 불공평하지 않나요?{/cps}"
    yuhyeon"{cps=25}재미있군.{/cps}"
    "{cps=25}김유현은 물고 있던 담배를 바다에 버리고 새로운 담배를 꺼냈다.{/cps}"
    yuhyeon"{cps=25}좋아.{/cps}"
    yuhyeon"{cps=25}그렇다면 내 이야기부터 먼저 해 주도록 하지.{/cps}"

    hide ihyun_happy
    hide yuhyeon_idle

    stop music fadeout 1

    jump twelvth_1

    # scene 12 : 4년 전 길거리
label twelvth_1:
    scene bg road with dissolve
    pause (1.0)

    play music "music/quiet.mp3" fadeout 1

    show yuhyeon_idle at left
    yuhyeon"{cps=25}요새 일이 별로 없군.{/cps}"
    yuhyeon"{cps=25}사건이 안 터졌다는 말이니까 좋은 일이겠지…{/cps}"
    "{cps=25}김유현은 그저 길을 걷고 있었다.{/cps}"
    "{cps=25}그 때 옆의 골목길에서 이상한 냄새가 났다.{/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_concerned at left
    yuhyeon"{cps=25}뭐지..?{/cps}"
    "{cps=25}비릿한 냄새.{/cps}"
    "{cps=25}아무리 생각해도 혈향이다. {/cps}"

    scene cg 3 with dissolve #(2.0)
    pause (1.0)

    "{cps=25}골목길 안으로 들어가자 한 여성이 옆구리에 칼에 찔려 쓰러져 있는 것이 보인다. {/cps}"
    "{cps=25}바닥에는 이미 꽤 많은 출혈의 흔적이 보인다. {/cps}"

    "???" "{cps=25}사… 살려…{/cps}"

    hide yuhyeon_concerned at left
    show yuhyeon_panic at left
    yuhyeon"{cps=25}무슨 일입니까! 누가 이렇게 한 거죠?{/cps}"
    "???" "{cps=25}선백교… {/cps}"

    "{cps=25}여성은 말을 끝마치지 못하고 정신을 잃었다.{/cps}"

    yuhyeon"{cps=25}맞아. 119{/cps}"

    "{cps=25}핸드폰을 붙잡은 손이 떨린다. {/cps}"
    "{cps=25}겨우 전화를 걸었다. {/cps}"

    yuhyeon"{cps=25}네! 여기 장소는요…{/cps}"

    hide  yuhyeon_panic

    jump twelvth_2

    # scene12: 병원복도

label twelvth_2:

    scene bg hospital with dissolve
    pause (1.0)

    show yuhyeon_concerned at right
    yuhyeon"{cps=25}상태는 어떻습니까?{/cps}"
    "의사" "{cps=25}죄송하지만… 힘들 것 같습니다.{/cps}"

    "{cps=25}김유현은 혼자서 자책했다. {/cps}"

    yuhyeon"{cps=25}내가 조금만 더 빨리 발견했더라면…{/cps}"
    yuhyeon"{cps=25}그랬다면 구할 수도 있었을 텐데…{/cps}"

    "{cps=25}누군가 김유현의 옆에 앉았다.{/cps}"
    "{cps=25}한태현이었다.{/cps}"

    hide yuhyeon_concerned at right
    show yuhyeon_idle at right
    show taehyeon at left
    "한태현""{cps=25}너무 자책하지는 말게.{/cps}"
    "한태현""{cps=25}억울한 일이 있으면 풀어줘야지.{/cps}"
    "한태현""{cps=25}그게 형사의 할 일이 아닌가?{/cps}"

    "{cps=25}한태현은 김유현에게 위로의 말을 건냈다. {/cps}"
    "{cps=25}그 때 순경 한 명이 파일을 들고 다가왔다.{/cps}"

    "경찰""{cps=25}검사님. 피해자 신상조회 끝났습니다.{/cps}"
    "한태현""{cps=25}그래. 고맙네.{/cps}"
    "한태현""{cps=25}잠시 자리를 비켜줄 수 있겠나?{/cps}"
    "한태현""{cps=25}이 사람과 잠시 얘기할 거리가 있어서 말이지.{/cps}"
    "경찰""{cps=25}네, 알겠습니다. {/cps}"

    "{cps=25}순경이 사라지자 한태현은 파일을 열어 보았다.{/cps}"

    "한태현""{cps=25}이름… 안시영{/cps}"
    "한태현""{cps=25}직업은… 그냥 학생이군, 대학교가 이 근처네.{/cps}"
    "한태현""{cps=25}특이사항은 없고{/cps}"
    "한태현""{cps=25}친구 관계도 원만하고, 주위에 특별히 무언가가 있는것도 아니고…{/cps}"
    "{cps=25}한태현은 조용히 파일을 접었다.{/cps}"
    "한태현""{cps=25}역시 서류상으로는 딱히 드러나는 게 없단 말이지.{/cps}"

    "{cps=25}김유현은 생각했다. {/cps}"
    "{cps=25}검사인데도 서류, 파일에 의존하지 않고 현장을 중요시하는 사람.{/cps}"
    "{cps=25}표면적으로 드러나지 않은 것을 캐치할 수 있는 사람.{/cps}"
    "{cps=25}김유현이 느끼기에 한태현은 그런 사람이었다. {/cps}"

    "한태현""{cps=25}무언가 들은 것은 없나? 최초의 목격자?{/cps}"

    hide yuhyeon_idle at right
    show yuhyeon_concerned at right
    yuhyeon "{cps=25}딱히…{/cps}"

    "{cps=25}그러던 중 김유현의 머릿속으로 여성의 말이 스쳐지나갔다. {/cps}"

    yuhyeon "{cps=25}선백교.. 맞아 선백교라고 그랬습니다. {/cps}"
    "한태현""{cps=25}선백교라…{/cps}"
    "한태현""{cps=25}설마 선백교가 다리 이름은 아닐테고…{/cps}"
    "한태현""{cps=25}종교인가?{/cps}"

    "{cps=25}한태현은 일어나 옷매무새를 만지며 말했다.{/cps}"

    "한태현""{cps=25}아무래도 조금 골치아픈 사건을 만난 것 같은데 말이지.{/cps}"
    yuhyeon "{cps=25}그런 것 같군요.{/cps}"

    "{cps=25}창 밖은 이미 어두워진지 오래다. {/cps}"

    hide yuhyeon_concerned
    hide taehyeon

    jump twelvth_3

    # scene 12: 경찰서 복도
label twelvth_3:

    scene bg police with dissolve
    pause (1.0)

    "{cps=25}펄럭{/cps}"
    show taehyeon at left
    "한태현""{cps=25}잠시 이쪽으로 와줄 수 있겠나?{/cps}"

    "{cps=25}서류를 넘기고 있던 김유현을 한태현이 불렀다. {/cps}"

    show yuhyeon_idle at right
    yuhyeon"{cps=25}무슨 일이십니까?{/cps}"
    "{cps=25}한태현은 김유현에게 서류를 넘기며 말했다.{/cps}"
    "한태현""{cps=25}정말 골치아픈 사건이야.{/cps}"
    "한태현""{cps=25}그것도 아주 악질의…{/cps}"
    "한태현""{cps=25}그리고 영장을 받을 수 있는 방법도 보이질 않아.{/cps}"

    "{cps=25}그러자 김유현이 웃으며 말했다.{/cps}"

    hide yuhyeon_idle at right
    show yuhyeon_happy at right
    yuhyeon"{cps=25}저도 저 나름대로 조사를 좀 해 봤습니다.{/cps}"
    "{cps=25}그리고 자신의 자리에서 서류 하나를 가져왔다. {/cps}"
    yuhyeon"{cps=25}선백교의 장부입니다.{/cps}"
    yuhyeon"{cps=25}뭔가 이상한게 보이지 않으세요?{/cps}"
    "{cps=25}한태현이 서류를 읽고 잠시 후{/cps}"
    "한태현""{cps=25}아주 좋은데?{/cps}"
    "한태현""{cps=25}이거라면 받을 수 있을 거야{/cps}"
    "{cps=25}한태현은 웃으면서 말했다. {/cps}"

    hide yuhyeon_happy
    hide taehyeon

    stop music fadeout 1

    jump thirteenth

    #13 scene: 선백교 건물 앞
label thirteenth:
    scene bg church with dissolve
    pause (1.0)

    play music "music/bad events.mp3" fadeout 1

    "{cps=25}선백교회 지부.{/cps}"
    "{cps=25}하얀색 고층빌딩을 중심으로 경찰과 검찰이 둘러싸고 있다. {/cps}"
    "{cps=25}도로는 통제된지 오래. 한태현이 차에서 김유현과 함께 내려 주위를 둘러본다.{/cps}"

    show taehyeon at left
    "한태현""{cps=25}하, 이거 산 넘어 산이구먼. 영장 발부 다음에 무력반항이라니.{/cps}"

    "{cps=25}한태현이 건물을 바라보며 말했다. {/cps}"

    "한태현""{cps=25}저것들 아주 악질이야.{/cps}"
    "한태현""{cps=25}염원을 이뤄준다는 부적을 만드는데…{/cps}"
    "한태현""{cps=25}동물을 며칠동안 굶겨.{/cps}"
    "한태현""{cps=25}물만 주면서 먹이를 하나도 주지 않고.{/cps}"
    "한태현""{cps=25}그 동물을 끝이 좁아지는 방 안에 넣는거야.{/cps}"
    "한태현""{cps=25}그리고 방 안 제일 좁은 곳에는 음식이 놓여있지.{/cps}"
    "한태현""{cps=25}그래서 동물이 기어서 음식쪽으로 가는데 음식이 있는 곳은 좁아서 닿지를 않아.{/cps}"
    "한태현""{cps=25}그렇게 발을 뻗어서라도 그 음식을 가져가려는 순간 동물을 죽이고 앞발을 잘라.{/cps}"
    "한태현""{cps=25}그 앞발에 간절히 원하는 염원이 담겨있다고 하고 그걸 몸에 지니고 다니는거지.{/cps}"

    "{cps=25}김유현은 그 말을 듣고 질린다는 표정을 지었다. {/cps}"

    show yuhyeon_concerned at right
    yuhyeon "{cps=25}잔인하군요.{/cps}"
    "한태현""{cps=25}그렇지, 잔인하지.{/cps}"
    yuhyeon "{cps=25}그래도 이렇게 영장까지 가지고 나온 이상…{/cps}"
    "{cps=25}김유현의 말이 끝나기도 전에 고층빌딩 4층에서 붉은색 불기둥이 터졌다.{/cps}"
    "{cps=25}{color=#eb2106}{size=+20}'펑!'{/size}{/color}{/cps}"
    "{cps=25}이를 예상하지 못했는지 경찰들이 우왕좌왕한다. {/cps}"

    "경찰""{cps=25}불이야!{/cps}"
    "경찰""{cps=25}4층에서 불이 났다!{/cps}"
    "한태현""{cps=25}이, 이런 젠장..!{/cps}"

    "{cps=25}한태현이 주위를 둘러보면서 주먹을 꽉 쥔다.{/cps}"
    "{cps=25}경찰 한 명이 다급하게 다가오면서 한태현에게 묻는다.{/cps}"

    "경찰""{cps=25}어, 어떡할까요, 검사님?{/cps}"
    "한태현""{cps=25}어떡하긴 뭘 어떻게 해! 119 연락하고 정문 부셔! {/cps}"

    "{cps=25}불길은 점점 퍼져나간다. {/cps}"
    "{cps=25}경찰들은 달려가서 문을 부순다. {/cps}"
    "{cps=25}그리고 얼마 지나지 않아 경찰 한명이 소리를 지른다. {/cps}"

    "경찰""{cps=25}사, 사람이 나옵니다!{/cps}"

    "{cps=25}불길이 2층과 5층으로 순식간에 퍼져나가 어떡할지 고민하던 중에 경찰의 한마디에 모두의 이목이 문으로 쏠린다.{/cps}"
    "{cps=25}굳게 닫혀진 현관에서 검은 연기와 함께 사람 한명이 겨우겨우 나온다.{/cps}"

    hide yuhyeon_concerned
    hide  taehyeon
    show hyunjoo_idle
    hyunjoo "{cps=25}쿨럭, 쿨럭, {/cps}"
    "경찰" "{cps=25}생존자다. 얼른 병원으로 이송해!{/cps}"

    "{cps=25}경찰 몇 명이 생존자에게 몰려 안전하게 빠져나오도록 부축해준다.{/cps}"
    "{cps=25}그때 마침 연락한 소방차와 구급차가 온다. {/cps}"

    hide  hyunjoo_idle
    show yuhyeon_panic at right
    yuhyeon"{cps=25}화재.. 화재라니.{/cps}"
    yuhyeon"{cps=25}(제3자의 개입인가? 아니면 증거인멸을 위한 화재?){/cps}"

    show taehyeon at left
    "한태현""{cps=25}야, 김유현. 빨리 타!{/cps}"
    "{cps=25}아수라장이 된 현장에서 김유현은 찝찝함을 남겨두고 한태현의 차에 올라탄다.{/cps}"
    "{cps=25}그렇게 한태현의 차는 구급차와 함께 병원으로 향한다.{/cps}"

    hide taehyeon
    hide yuhyeon_panic

    scene bg blackscreen with dissolve
    jump forteenth

    # 14: 선백교 건물 앞
label forteenth:
    scene bg hospital with dissolve
    pause (1.0)

    play sound "sounds/Door2.wav"

    "{cps=25}병실 문이 닫히면서 신경질적인 얼굴의 한태현과 차분한 김유현이 나온다.{/cps}"
    stop sound

    show taehyeon at right
    show yuhyeon_concerned at left
    "한태현""{cps=25}이런 더러운..{/cps}"
    yuhyeon "{cps=25}교주와 임원 몇몇이 불을 지르고 지하실을 통해 도망갔다.. {/cps}"
    yuhyeon "{cps=25}일이 점점 꼬이네요.{/cps}"

    pause(1.0)
    play sound "sounds/477.mp3"
    play sound "sounds/477.mp3"
    pause(1.0)

    "{cps=25}한태현이 휴대전화를 확인하고는 한숨을 내쉰다.{/cps}"
    "한태현""{cps=25}전화 좀 받고 온다.{/cps}"
    hide taehyeon

    "{cps=25}한태현이 전화를 받으러 어디론가 사라진다.{/cps}"
    "{cps=25}남은 김유현은 병실 문 앞에서 복잡한 머리를 정리하려 한다.{/cps}"

    yuhyeon "{cps=25}(방화로 증거들은 다 사라졌겠고.. 고현주의 증언만으로 파헤치는 것도 한계가 있을텐데..){/cps}"

    play sound "sounds/Door2.wav"

    yuhyeon "{cps=25}음?{/cps}"
    stop sound

    show hyunjoo_idle at right
    "{cps=25}문이 열리자 환자복의 여성이 나온다. 이름은 고현주. 그 불지옥에서 살아남은 유일한 생존자이다.{/cps}"
    "{cps=25}고현주는 경계 가득한 얼굴로 김유현을 쳐다보다가 주위를 둘러보고는 입을 연다.{/cps}"

    hyunjoo"{cps=25}그쪽은 형사고…{/cps}"
    yuhyeon "{cps=25}네, 그렇습니다만..{/cps}"
    hyunjoo"{cps=25}아까 그분이 검사이신가요?{/cps}"
    yuhyeon "{cps=25}네, 맞습니다. {/cps}"
    hyunjoo"{cps=25}…사실 방금 전 증언에서 말하지 않은게 있어요.{/cps}"
    yuhyeon "{cps=25}무엇이죠?{/cps}"

    "{cps=25}김유현이 침을 삼킨다.{/cps}"

    hyunjoo"{cps=25}제가, 선백교 임원이에요.{/cps}"

    hide yuhyeon_concerned
    show yuhyeon_panic at left
    yuhyeon "{cps=25}..네?{/cps}"

    hide hyunjoo_idle
    show hyunjoo_concerned at right
    hyunjoo"{cps=25}교회에 불을 지르고 도망가자는 건 모든 임원들의 의견이 아니었어요. 교주를 중심으로 몇몇 임원들이 주장한거죠.{/cps}"
    hyunjoo"{cps=25}저를 비롯한 몇몇 임원들이 쪽방에서 머물 동안 다른 임원들과 교주가 불을 지르고 도망간거에요.{/cps}"
    hyunjoo"{cps=25}물론, 살아남은건 저뿐인 것 같지만..{/cps}"

    "{cps=25}고현주의 추가증언에 김유현은 침착하게 되묻는다.{/cps}"

    hide yuhyeon_panic
    show yuhyeon_concerned at left
    yuhyeon "{cps=25}이걸 말해주는 이유가 무엇이죠?{/cps}"
    hyunjoo"{cps=25}더 이상 선백교를 파지 마세요. 당신 목숨만 위험해져요. 교주는, 진짜 자기가 신이라도 되는 것처럼 구는 사람이니까.{/cps}"
    hyunjoo"{cps=25}그런 미친 놈은, 물불 안 가리거든요.{/cps}"

    hide hyunjoo_concerned
    "{cps=25}고현주는 자기 할 말을 끝내고 다시 병실에 들어간다. 그 순간,{/cps}"
    pause 1.0

    "한태현""{cps=25}이런 젠장!!!{/cps}"

    show taehyeon at right
    "{cps=25}한태현이 신경질을 내며 돌아온다.{/cps}"
    "한태현""{cps=25}하여튼 윗선 놈들, 머리에는 뭐가 들었는지.{/cps}"
    "{cps=25}김유현은 고현주의 증언을 곱씹다가 한태현을 돌아본다.{/cps}"

    hide yuhyeon_concerned
    show yuhyeon_idle at left
    yuhyeon "{cps=25}뭐랍니까?{/cps}"
    "한태현""{cps=25}이번 화재사건으로 사상자가 너무 많아 더 이상 깊게 수사하면 안된다고 하더라.{/cps}"
    yuhyeon "{cps=25}네..?{/cps}"
    "한태현""{cps=25}이번에 수사한게 언론에 알려지면 희생자들 왜 못구했냐고, 탄압수사 아니냐고 난리 날거라고 하더라.{/cps}"

    "{cps=25}한태현의 말에 김유현이 어이없다듯이 말한다.{/cps}"

    yuhyeon "{cps=25}사이비 종교입니다. 더 두면 더 큰 피해가..{/cps}"

    "한태현""{cps=25}나도 알아, 안다고. 그래서 설득해보려고 했는데.. 너도 알잖냐. 조직에 피해가 오는거 죽도록 싫어하는거.{/cps}"
    "{cps=25}한태현의 말에 김유현은 고현주의 증언을 삼킨다.{/cps}"

    "한태현""{cps=25}미안하다, 내가 할 수 있는 일은 여기까지인 거 같다. {/cps}"
    "{cps=25}한태현은 미안하다는 눈빛으로 김유현을 봤다.{/cps}"

    hide  yuhyeon_idle
    hide taehyeon

    stop music fadeout 3

    jump fifteenth

    #15: 이현의 방

label fifteenth:
    scene bg ihyun room with dissolve
    pause (1.0)

    play music "music/bad end.mp3" fadeout 1

    "{cps=25}이현의 방.{/cps}"

    "{cps=25}이현이 지끈거리는 머리를 붙잡고 일어난다. {/cps}"
    "{cps=25}김유현과 이야기를 나누고 방에 들어왔지만 혼란스러운 머리는 정리되지 않는다.{/cps}"
    "{cps=25}아직도 그 이야기가 머릿속에서 맴돈다. {/cps}"
    "{cps=25}아직도.. 찝찝하다.{/cps}"

    show ihyun_concerned at right
    ihyun"{cps=25}박준규.. 어쩐지 익숙한 이름이다 했어.{/cps}"
    "{cps=25}예전에 이솔한테 들었던 이름이었다. 이솔의 전 남자친구.{/cps}"
    ihyun"{cps=25}그러고보니.. 예전에 솔이도 교회를 다녔었는데..{/cps}"
    "{cps=25}어느 순간 가는 걸 그만두었지만.. 그 시기가 화재사건이랑 비슷한것 같은데..{/cps}"
    ihyun"{cps=25}..그럼 이솔도..?{/cps}"
    "{cps=25}박준규를 교회에서 만났다면 선백교 밖에 없다. 이솔이 다니던 교회가 선백교일 가능성이 높다. 그래서 이곳에 온거겠지.{/cps}"
    "{cps=25}그럼.. 이솔도 범행의 표적이 될 수도 있다는 것이다.{/cps}"
    ihyun"{cps=25}그것만은 안돼.. 내가 지켜야해.{/cps}"

    scene bg blackscreen with dissolve
    pause (3.0)

    hide ihyun_concerned
    jump scene15

##15 : 이현의 방
label scene15:
    scene bg ihyun room with dissolve
    pause (1.0)

    "{cps=25}이현은 거의 뜬눈으로 밤을 지새웠다. {/cps}"

    show ihyun_idle at left

    ihyun "{cps=25}지금이 몇시지?{/cps}"
    "{cps=25}핸드폰 화면은 8시 반을 가리키고 있었다. {/cps}"
    ihyun "{cps=25}거의 한숨도 자지 못했어.{/cps}"
    "{cps=25}새벽녘이 되어서야 잠이 든게 전부다{/cps}"
    "{cps=25}그마저도 이렇게 금방 깨어버렸지만.{/cps}"

    hide ihyun_idle at left
    show ihyun_concerned at left

    ihyun "{cps=25}절대… 누구에게도 휘둘리지 않겠어.{/cps}"
    "{cps=25}이현은 몇 번 심호흡을 한 뒤 방을 나섰다. {/cps}"

    hide ihyun_concerned


    jump scene16

##16 : 복도
label scene16:

    scene bg hallway with dissolve#(2.0)
    pause (1.0)
    "{cps=25}똑똑똑{/cps}"
    "{cps=25}이현은 이솔의 방문을 두드렸다. {/cps}"

    show ihyun_idle at left

    ihyun "{cps=25}솔아, 안에 있어?{/cps}"
    "{cps=25}잠시 후 작은 소리로 대답이 들려왔다. {/cps}"
    isol "{cps=25}…응{/cps}"    # 여기서 이솔을 등장시키진 말아주세요.
    "{cps=25}시간이 얼마나 지났을까. {/cps}"
    "{cps=25}방문이 열리고 이솔이 나왔다.{/cps}"

    show isol_idle at right

    isol "{cps=25}나 나왔어.{/cps}"
    "{cps=25}약간 피곤해보이는 느낌이다. {/cps}"
    "{cps=25}이솔도 잠을 잘 자지 못한 것은 아닐까?{/cps}"
    "{cps=25}이현은 그렇게 생각했다. {/cps}"
    isol "{cps=25}나… 배고파.{/cps}"
    ihyun "{cps=25}어… 그래.{/cps}"
    ihyun "{cps=25}식당으로 가자.{/cps}"
    "{cps=25}이현은 식당으로 걸어가며 생각했다. {/cps}"

    hide ihyun_idle at left
    show ihyun_concerned at left

    ihyun "{cps=25}(반드시… 반드시 누구에게도 휘둘리지 않겠어.){/cps}"
    ihyun "{cps=25}(나 자신을 위해서라도… 솔이를 위해서라도…){/cps}"

    hide ihyun_concerned
    hide isol_idle

    stop music fadeout 1

    jump scene17

##17 : 식당
label scene17:
    scene bg cafeteria with dissolve
    pause (1.0)

    play music "music/quiet.mp3" fadeout 1

    "{cps=25}식당{/cps}"

    "{cps=25}이현과 이솔이 식당에 도착했을 때에는 대부분의 사람이 모여 있었다. {/cps}"
    "{cps=25}다행히도 식당에는 먹을 것이 충분했다. {/cps}"

    show ihyun_idle at left

    ihyun "{cps=25}스태프들이 다 떠나서 어쩌나 했는데 다행이야.{/cps}"

    show isol_idle at right
    isol "{cps=25}…{/cps}"

    "{cps=25}이현은 이솔의 눈치를 살짝 보았다.{/cps}"
    "{cps=25}아무래도 평소랑 비슷한 것 같지만 많이 피곤해 보인다. {/cps}"



    ihyun "{cps=25}많이 피곤한가보네.{/cps}"
    ihyun "{cps=25}피곤할테니까 밥 먹고 빨리 방으로 돌아가자.{/cps}"

    hide isol_idle
    "{cps=25}이현은 주위를 둘러보았다.{/cps}"
    "{cps=25}이미 대부분의 사람들이 식당에 모여 있었다. {/cps}"
    ihyun "{cps=25}사람들이 거의 다 모여있네… 하나.. 둘…{/cps}"
    "{cps=25}정시욱 한 명을 제외하면 모두 모여 있었다. {/cps}"

    hide ihyun_idle

    show yuhyeon_idle at right

    yuhyeon "{cps=25}크흠…{/cps}"
    "{cps=25}김유현이 말을 꺼내려는 듯 헛기침을 했다. {/cps}"
    "{cps=25}사람들의 시선이 김유현에게 쏠린다. {/cps}"
    yuhyeon "{cps=25}이쯤 되면 다들 모인 것 같군요.{/cps}"
    yuhyeon "{cps=25}어제는 상황이 상황이다 보니 얘기를 제대로 못 했습니다. {/cps}"
    yuhyeon "{cps=25}일단 지금 상황부터 정리해보죠.{/cps}"
    yuhyeon "{cps=25}어제{/cps}"
    yuhyeon "{cps=25}우리는 유람선을 타게 되었죠.{/cps}"
    yuhyeon "{cps=25}각자 여기에 오게 된 이유는 조금씩 다를 겁니다. {/cps}"
    yuhyeon "{cps=25}하지만 그 이유가 중요하다고 생각되지는 않는군요.{/cps}"
    yuhyeon "{cps=25}그리고 유람선 안에서는 파티가 열렸습니다.{/cps}"
    yuhyeon "{cps=25}서로 좀 시간이 지났지만 점점 얘기를 하면서 확신으로 바뀌었겠죠.{/cps}"
    yuhyeon "{cps=25}여기 있는 사람들은 내가 알던 사람들이 아닐까.{/cps}"
    yuhyeon "{cps=25}그러면서 불안감이 좀 커졌을 겁니다. {/cps}"
    yuhyeon "{cps=25}그 불안감이 서서히 커져가던 중 갑자기 스탭들이 선물을 들고왔죠.{/cps}"
    "{cps=25}사람들이 동요한다.{/cps}"
    yuhyeon "{cps=25}그 선물은 사람의 시체였습니다. {/cps}"
    yuhyeon "{cps=25}시체의 주인공은 한태현.{/cps}"
    yuhyeon "{cps=25}한때 선백교 사건을 담당하던 검사입니다.{/cps}"
    yuhyeon "{cps=25}그리고 여기 대부분의 선백교 사람들이 모여 있군요.{/cps}"
    yuhyeon "{cps=25}아니… 이게 전부인가요?{/cps}"
    "{cps=25}사람들이 서로를 힐끗힐끗 쳐다보기만 한다.{/cps}"
    "{cps=25}이현 또한 이솔을 힐끗 본다. {/cps}"
    yuhyeon "{cps=25}지금 가장 중요한 것은 신뢰일 듯 합니다. {/cps}"
    yuhyeon "{cps=25}서로가 불안감을 좀 덜어내야겠지요.{/cps}"
    yuhyeon "{cps=25}알고 있는 정보를 조금씩 풀어보는게 어떻습니까.{/cps}"

    show hyunjoo_cold at left

    hyunjoo "{cps=25}헛소리!!{/cps}"
    "{cps=25}김유현의 중저음 목소리와 대비되는 앙칼진 여성의 목소리가 들렸다.{/cps}"
    hyunjoo "{cps=25}지금 이 방에 범인이 있을 수도 있는데 정보를 꺼내 공유하자고?{/cps}"
    hyunjoo "{cps=25}누구 좋으라고?{/cps}"
    yuhyeon "{cps=25}정보가 없으면 범인을 잡을 수 없습니다. {/cps}"
    yuhyeon "{cps=25}범인을 잡지 못하면 여기 모두가 죽을 수도 있고요.{/cps}"
    "{cps=25}고현주가 냉소를 지으며 말했다. {/cps}"
    hyunjoo "{cps=25}범인에게 정보가 가면 우리를 죽일 방법도 많아지겠지.{/cps}"

    hide yuhyeon_idle at right
    show yuhyeon_angry at right

    yuhyeon "{cps=25}당신은 대체…{/cps}"
    "{cps=25}두 남녀의 싸움소리가 식당에 울린다. {/cps}"
    "{cps=25}누구는 흥미롭다는 듯이.{/cps}"
    "{cps=25}누구는 불안하다는 듯이 쳐다본다. {/cps}"

    hide yuhyeon_angry at right
    show yuhyeon_concerned at right

    yuhyeon "{cps=25}하지만 제일 먼저 물어보고 싶은 것은 저것입니다. {/cps}"
    "{cps=25}김유현이 벽의 공지란을 가리키며 말했다. {/cps}"
    "{cps=25}공지란에는 서류가 하나 붙어 있었다. {/cps}"
    yuhyeon "{cps=25}저 장부의 정체를 말씀드리죠.{/cps}"
    "{cps=25}사람들의 관심이 장부로 쏠린다. {/cps}"
    yuhyeon "{cps=25}많이 익숙하실 겁니다. {/cps}"
    yuhyeon "{cps=25}선백교의 장부이니까요.{/cps}"
    yuhyeon "{cps=25}제가 수사를 할 당시 저 장부로 인해서 영장이 나올 수 있었죠.{/cps}"
    yuhyeon "{cps=25}경찰들이 본격적으로 수사를 할 수 있는 빌미를 주었던 장부입니다. {/cps}"
    yuhyeon "{cps=25}그렇다면 저 장부를 관리하던 사람이 누구죠?{/cps}"
    "{cps=25}김유현은 사람들을 바라보며 말했다.{/cps}"
    yuhyeon "{cps=25}분명 임원 중 한명이겠죠.{/cps}"
    "{cps=25}김유현의 눈이 고현주에게서 멈췄다. {/cps}"
    "{cps=25}고현주는 김유현의 시선에 어쩔 수 없다는 듯 말했다. {/cps}"

    hide hyunjoo_cold at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}장부는 정시욱씨가 관리했어.{/cps}"
    hyunjoo "{cps=25}어짜피 여기 있는 대부분의 사람들은 다 알잖아.{/cps}"
    hyunjoo "{cps=25}임원들도 여럿 있고 선백교 임원이 비밀인 것도 아니니까.{/cps}"
    "{cps=25}박준규와 조정은이 왜 그런 것을 말하냐는 표정으로 고현주를 쳐다본다.{/cps}"
    hyunjoo "{cps=25}왜 찔리는 거라도 있어?{/cps}"
    hyunjoo "{cps=25}박준규, 조정은?{/cps}"

    show jungyu_angry at slightright
    show jungeun_panic at slightleft

    jungyu "{cps=25}아니 당신이란 사람은…{/cps}"
    jungeun "{cps=25}왜 굳이 말하지 않아도 될 걸 말하는거에요.{/cps}"
    "{cps=25}김유현이 흥미롭다는 듯 말한다.{/cps}"

    hide yuhyeon_concerned at right
    show yuhyeon_cold at right

    yuhyeon "{cps=25}임원들이 누가 있었는지는 처음 듣는군요.{/cps}"
    yuhyeon "{cps=25}고현주씨, 또 임원이 누가 있죠?{/cps}"
    hyunjoo "{cps=25}여기 있는 셋에 정시욱 그리고 교주.{/cps}"
    "{cps=25}고현주가 계속해서 얘기를 하자 박준규와 조정은이 말하지 말라고 화를 낸다.{/cps}"
    "{cps=25}하지만 고현주는 별로 신경쓰지 않는 듯 하다. {/cps}"

    hide yuhyeon_cold at right
    show yuhyeon_idle at right

    yuhyeon "{cps=25}결국 저 장부에 대해서 자세한 것은 정시욱씨를 봐야 알겠군요.{/cps}"
    "{cps=25}시계는 벌써 열한시를 넘어가고 있었다. {/cps}"
    ihyun "{cps=25}그런데 이상하지 않아요?{/cps}"
    ihyun "{cps=25}아직 정시욱씨가 나오지 않았어요.{/cps}"
    ihyun "{cps=25}무슨 일이 생긴 것은 아닐지…{/cps}"

    hide yuhyeon_idle at right
    show yuhyeon_concerned at right

    yuhyeon "{cps=25}흠…{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_cold at left

    hyunjoo "{cps=25}혹시 모르지.{/cps}"
    hyunjoo "{cps=25}두려움에 떨면서 이불 속에 숨어있을지도.{/cps}"
    "{cps=25}김유현이 자리에서 일어나며 말했다. {/cps}"

    hide yuhyeon_concerned at right
    show yuhyeon_idle at right

    yuhyeon "{cps=25}그럼 한번 찾아가보죠.{/cps}"

    hide hyunjoo_cold
    hide jungeun_panic
    hide jungyu_angry
    hide yuhyeon_idle

    stop music fadeout 1

    jump scene18

##18 : 복도
label scene18:
    scene bg hallway with dissolve#(2.0)
    pause (1.0)

    play music "music/Cruise Whitnoise.mp3" fadeout 1

    "{cps=25}똑똑똑{/cps}"

    show yuhyeon_idle at left

    yuhyeon "{cps=25}정시욱씨… 정시욱씨?{/cps}"
    play sound "sounds/weak_knock.mp3"
    "{cps=25}문을 두드리며 불러보지만 대답은 돌아오지 않았다.{/cps}"

    show ihyun_idle at right

    ihyun "{cps=25}왜 이렇게 안 나오시지?{/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_concerned at left

    yuhyeon "{cps=25}흠…{/cps}"
    yuhyeon "{cps=25}대답을 안하는 것일 수도 있고…{/cps}"
    "{cps=25}고현주가 뒷말을 받았다.{/cps}"

    hide ihyun_idle
    show hyunjoo_concerned at right

    hyunjoo "{cps=25}무슨 일이 생긴 걸지도 모르지.{/cps}"
    "{cps=25}이현의 머릿속에는 어제의 사건이 떠올랐다.{/cps}"
    "{cps=25}이어 불길한 예감이 등골을 타고 올라와 몸에 전율한다. {/cps}"
    play sound "sounds/strong_knock.mp3"
    "{cps=25}{size=+20}탕탕탕{/size}{/cps}"
    "{cps=25}박준규가 전보다 거세게 문을 두드린다.{/cps}"

    show jungyu_panic at slightleft

    jungyu "{cps=25}정시욱씨! 문 좀 열어봐요!{/cps}"
    "{cps=25}하지만 안에서는 아무런 반응이 없었다. {/cps}"

    hide yuhyeon_concerned at left
    show yuhyeon_idle at left

    yuhyeon "{cps=25}이렇게 되면 강제로 들어가는 방법밖에 없습니다. {/cps}"
    yuhyeon "{cps=25}문을 강제로 열죠.{/cps}"

    show jungeun_panic at slightright

    jungeun "{cps=25}하지만… 일부러 안 여시는 거라면…{/cps}"
    "{cps=25}김유현이 잠시 뒤로 물러나면서 말했다. {/cps}"
    yuhyeon "{cps=25}그건 그것대로 문을 열 이유가 됩니다. {/cps}"
    yuhyeon "{cps=25}찔릴 게 없다면 열어줄 수 있겠죠.{/cps}"
    yuhyeon "{cps=25}모두 물러나세요.{/cps}"
    play sound "sounds/bang.wav"
    "{cps=25}쾅!{/cps}"
    "{cps=25}김유현이 문을 발로 찼다.{/cps}"
    play sound "sounds/bang2.wav"
    "{cps=25}쾅! 쾅! 콰직!{/cps}"
    play sound "sounds/doorbreak.wav"
    "{cps=25}이윽고 몇번 더 문을 차자 나무 문은 큰 소리를 내며 부서졌다.{/cps}"
    "{cps=25}그리고 방 안에서 썩은 냄새가 진하게 났다. {/cps}"

    hide yuhyeon_idle
    hide hyunjoo_concerned
    hide jungyu_panic
    hide jungeun_panic

    stop music fadeout 1

    jump scene19

##19 : 정시욱의 방
label scene19:
    scene bg other rooms with dissolve
    pause (1.0)

    play music "music/nervous.mp3" fadeout 1

    "{cps=25}김유현이 먼저 방 안으로 들어왔다. {/cps}"

    show yuhyeon_concerned at left

    yuhyeon "{cps=25}이게 무슨 냄새지…?{/cps}"
    "{cps=25}이윽고 나머지 사람들도 방 안으로 들어왔다.{/cps}"

    show jungeun_panic at right

    jungeun "{cps=25}이게 무슨 상황인가요…?{/cps}"
    "{cps=25}각 벽의 한 가운데에는 못으로 돈이 고정되어 있다.{/cps}"
    "{cps=25}기괴하다.{/cps}"
    "{cps=25}천장을 보니 검붉은 글씨가 쓰여 있다. {/cps}"
    "{cps=25}양들은 타인의 물건을 탐하지 말고 도둑질하지 말라{/cps}"
    yuhyeon "{cps=25}이번에도 똑같군…{/cps}"
    "{cps=25}박준규가 나서서 말했다.{/cps}"

    show jungyu_concerned at slightleft

    jungyu "{cps=25}정시욱씨는 어디에 있죠?{/cps}"
    "{cps=25}하지만 방 안을 둘러보아도 정시욱은 보이지 않았다. {/cps}"
    yuhyeon "{cps=25}화장실에 있는 건가?{/cps}"
    "{cps=25}화장실 문을 열었지만 아무도 없었다.{/cps}"
    yuhyeon "{cps=25}어디에 있는거지?{/cps}"
    "{cps=25}그 때 박준규가 비명을 질렀다.{/cps}"

    hide jungyu_concerned at slightleft
    show jungyu_pale at slightleft

    jungyu "{cps=25}으악!{/cps}"
    "{cps=25}그리고 박준규가 있는 곳을 바라본 사람들은 모두 숨을 멈췄다.{/cps}"

    hide yuhyeon_concerned
    hide jungeun_panic
    hide jungyu_pale
    with Dissolve(2.0)

    scene cg 4 with dissolve
    pause (2.0)

    show hyunjoo_pale at left

    hyunjoo "{cps=25}이게… 무슨…{/cps}"
    "{cps=25}금고 안에는 정시욱이 들어가 있었다. {/cps}"
    "{cps=25}안에는 피가 흥건했다.{/cps}"
    "{cps=25}정시욱은 고통스러운 얼굴을 하고 죽어 있었다.{/cps}"

    hide jungyu_pale at right

    jungyu "{cps=25}이거 정말…{/cps}"
    jungyu "{cps=25}신이 노한 것인가?{/cps}"
    "{cps=25}고현주가 말도 안되는 소리라며 소리를 지른다.{/cps}"

    hide hyunjoo_pale at left
    show hyunjoo_angry at left

    hyunjoo "{cps=25}당신 정말 말도 안되는 소리를 하고 있는걸 자각하고 있어?{/cps}"

    show jungeun_angry at slightleft

    jungeun "{cps=25}제발 다들 그만 좀 해요!{/cps}"
    "{cps=25}지금까지 조용히 있던 조정은이 소리를 지른다.{/cps}"
    jungeun "{cps=25}이런 상황인데 싸울 만한 기력이 있기는 해요?{/cps}"
    jungeun "{cps=25}뭐하는거에요! 다들.{/cps}"
    "{cps=25}김유현이 거들었다.{/cps}"
    yuhyeon "{cps=25}맞습니다. {/cps}"
    yuhyeon "{cps=25}지금은 저희가 이렇게 싸우고 있을 때가 아닙니다. {/cps}"
    yuhyeon "{cps=25}증거를 찾아보죠.{/cps}"
    "{cps=25}그러고는 그대로 돌아서 방을 살펴보기 시작한다. {/cps}"

    hide jungyu_panic at right
    show jungyu_angry at right

    jungyu "{cps=25}저는 더 이상 여기에 못 있겠습니다.{/cps}"
    "{cps=25}박준규가 문 밖으로 나가자 조정은이 같이 따라 나간다. {/cps}"

    show yuhyeon_idle at slightright

    yuhyeon "{cps=25}방을 조금 더 여유롭게 살펴볼 수 있겠군요.{/cps}"
    yuhyeon "{cps=25}일단 정시욱씨부터 확인해 봅시다. {/cps}"
    yuhyeon "{cps=25}꺼내기는 힘드니 손가락 관절로 확인해 보았을 때{/cps}"
    yuhyeon "{cps=25}사후 경직은 확실히 온 것 같습니다. {/cps}"
    yuhyeon "{cps=25}일단 사망 이후 3시간은 충분히 지났다는 소리죠.{/cps}"
    "{cps=25}그리고 금고의 문을 닫으며 말했다. {/cps}"
    yuhyeon "{cps=25}금고 아래쪽으로 쓸린 흔적이 있군요.{/cps}"
    yuhyeon "{cps=25}아마 시체를 옮겼기 때문에 생긴 흔적이겠죠.{/cps}"
    yuhyeon "{cps=25}그리고 그 외에 특별한 것은 시신 근처에서는 찾을 수는 없군요.{/cps}"
    "{cps=25}이현이 말을 꺼냈다.{/cps}"

    ihyun "{cps=25}이 벽에 있는 못들은 무엇을 의미할까요?{/cps}"
    yuhyeon "{cps=25}잠시 생각을 해 봐야 할 것 같습니다. {/cps}"
    yuhyeon "{cps=25}여기 방들은 특이하죠{/cps}"
    yuhyeon "{cps=25}밖에서는 잠글 수 없고 안에서만 잠글 수 있습니다. {/cps}"
    yuhyeon "{cps=25}그런데 자살이 아닌 이상 안에서 잠그기는 힘들죠.{/cps}"
    "{cps=25}김유현은 못을 손가락으로 만지며 말했다. {/cps}"
    yuhyeon "{cps=25}아마 이 못이랑 관계가 있을 듯 한데….{/cps}"
    yuhyeon "{cps=25}어떻게 잠근 것이지?{/cps}"
    "{cps=25}고현주가 나섰다.{/cps}"

    hide hyunjoo_angry at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}대부분의 밀실은 실을 이용하긴 하지.{/cps}"
    hyunjoo "{cps=25}솔직히 여기같은 경우는 돌려서 내리는 것이기 때문에 얼음으로도 충분해 보이지만…{/cps}"
    "{cps=25}김유현이 부서진 문을 들었다. {/cps}"
    yuhyeon "{cps=25}지금 보니 몰랐는데 문에도 못이 박혀 있군요.{/cps}"
    yuhyeon "{cps=25}그렇다면 네 방위 모두 못이 박혀 있다는 소리인데…{/cps}"
    yuhyeon "{cps=25}그리고 문에는 젖은 흔적이 없습니다. {/cps}"
    yuhyeon "{cps=25}목재 문이기 때문에 물에 젖었다면 얼룩이 지겠지요.{/cps}"
    "{cps=25}모든 사람이 생각에 잠겼다. {/cps}"
    "{cps=25}정적을 깨고 고현주가 말을 꺼냈다. {/cps}"
    hyunjoo "{cps=25}아무리 생각해도 실을 이용한 것 같은데.{/cps}"
    yuhyeon "{cps=25}하지만 딱히 지금 생각나는 것은 없죠.{/cps}"
    yuhyeon "{cps=25}범인이 저런 장치를 해 둔 것에는 분명히 이유가 있을 겁니다. {/cps}"
    hyunjoo "{cps=25}그렇지…{/cps}"
    yuhyeon "{cps=25}보통은 두 가지 의미이지요.{/cps}"
    "{cps=25}김유현은 손가락 하나를 피며 말했다.{/cps}"
    yuhyeon "{cps=25}첫 번째는 트릭이나 기술로 장치를 사용한 것.{/cps}"
    yuhyeon "{cps=25}그리고 두 번째는 매우 드물기도 하고 소설에나 나올 법한 이야기이지만…{/cps}"
    yuhyeon "{cps=25}두 번째는 살인에 의미를 부여하기 위함입니다. {/cps}"
    "{cps=25}그리고 한숨을 쉬며 말했다. {/cps}"
    yuhyeon "{cps=25}지금 생각하기에는 두 가지 의미를  모두 부여하기 위함이라고 생각해봐야겠군요.{/cps}"

    hide yuhyeon_idle
    hide jungeun_angry
    hide jungyu_angry
    hide hyunjoo_idle

    stop music fadeout 1
    jump scene20

##20 : 식당
label scene20:
    scene bg cafeteria with dissolve
    pause (1.0)
    play music "music/quiet.mp3" fadeout 1

    "{cps=25}식당으로 돌아왔다. {/cps}"
    "{cps=25}이솔이 잠시 혼자 떨어지더니 원래 있던 자리에서 가방을 가지고 온다.{/cps}"
    "{cps=25}이솔이 가방을 가지고 이현 옆에 앉자 김유현이 말을 꺼냈다. {/cps}"

    show yuhyeon_idle at left

    yuhyeon "{cps=25}아까 전에 얻은 정보를 정리해보죠.{/cps}"
    yuhyeon "{cps=25}일단 첫 번째…{/cps}"
    "{cps=25}김유현은 숨을 잠시 멈춘 후 말했다. {/cps}"
    yuhyeon "{cps=25}살인 사건은 밤 중에 일어났습니다. {/cps}"
    yuhyeon "{cps=25}그리고 시체의 상흔은 후두부의 충격과 몸의 검상정도가 되겠군요.{/cps}"
    yuhyeon "{cps=25}아마 기절을 시킨 후 칼로 찔러 죽인 것 같습니다. {/cps}"
    "{cps=25}고현주가 말을 꺼냈다.{/cps}"

    show hyunjoo_concerned at right

    hyunjoo "{cps=25}그 말뜻은 우리 모두가 범인이 될 수 있다는 말이지.{/cps}"
    hyunjoo "{cps=25}칼 정도야 쉽게 구할 수 있고…{/cps}"
    hyunjoo "{cps=25}시간이 밤이라면 누구든 나갈 수 있을 테니까.{/cps}"
    hyunjoo "{cps=25}늙은이니까 혼자 생각도 많았을 것이고… 밖으로 나오는 타이밍도 있었겠지.{/cps}"

    show ihyun_concerned at slightleft

    ihyun "{cps=25}그리고 범인은 우리에게 누가 죽었는지 알려줬지요.{/cps}"
    ihyun "{cps=25}저 게시판을 통해서.{/cps}"
    "{cps=25}사람들이 게시판을 바라본다. {/cps}"
    "{cps=25}게시판에는 아직도 장부가 걸려 있다. {/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_concerned at left

    yuhyeon "{cps=25}정말… 소름돋는군…{/cps}"
    yuhyeon "{cps=25}그리고 두 번째로는…{/cps}"
    yuhyeon "{cps=25}밀실에 관한 부분입니다. {/cps}"
    yuhyeon "{cps=25}지금 이 상황 자체는 두 가지라고 생각하시면 됩니다. {/cps}"
    "{cps=25}고현주가 이상하다는 듯이 말했다.{/cps}"

    hide hyunjoo_concerned at right
    show hyunjoo_idle at right

    hyunjoo "{cps=25}왜 두 가지…?{/cps}"

    hide yuhyeon_concerned at left
    show yuhyeon_idle at left

    yuhyeon "{cps=25}정확히 말하면 흠…{/cps}"
    yuhyeon "{cps=25}밀실을 풀었다 라고 해두죠{/cps}"
    yuhyeon "{cps=25}첫 번째 밀실은 다들 알고 계실겁니다. {/cps}"
    yuhyeon "{cps=25}바로 문이 어떻게 잠겼는가에 대한 이야기이죠.{/cps}"
    yuhyeon "{cps=25}그리고 아까 문틈을 만져보았는데 {/cps}"
    yuhyeon "{cps=25}약간 홈이 깊게 파인 부분이 있었습니다. {/cps}"
    yuhyeon "{cps=25}이게 실로 인한 것인지 아니면 원래 있는 것인지는 모르겠지만….{/cps}"
    yuhyeon "{cps=25}정황상 실로 인해 생긴 것이라고 보는 게 편하겠죠.{/cps}"
    yuhyeon "{cps=25}그리고 두 번째 밀실…{/cps}"
    yuhyeon "{cps=25}이건 밀실이라 말하기는 좀 그렇습니다. {/cps}"
    yuhyeon "{cps=25}어떻게 금고를 풀었냐… 인데…{/cps}"

    hide ihyun_concerned at slightleft
    show ihyun_idle at slightleft

    ihyun "{cps=25}그러고 보니 그렇군요…{/cps}"
    "{cps=25}이현은 잠시 생각하다가 의견을 냈다. {/cps}"
    ihyun "{cps=25}혹시 정시욱과 가까운 사이인 사람이 범인이 아닐까요?{/cps}"
    hyunjoo "{cps=25}가까운 사이라고 해도 비밀번호를 알려 줄 만한 사람이 있을까?{/cps}"
    hyunjoo "{cps=25}흠…{/cps}"
    hyunjoo "{cps=25}임원들끼리도 별로 친하게 지내지 않았어.{/cps}"
    hyunjoo "{cps=25}정말 비즈니스적인 관계였다고.{/cps}"
    ihyun "{cps=25}아니면 처음부터 열려 있었을 수도 있죠.{/cps}"

    hide hyunjoo_idle at right
    show hyunjoo_concerned at right

    hyunjoo "{cps=25}아니…{/cps}"
    hyunjoo "{cps=25}그건 아니야.{/cps}"
    hyunjoo "{cps=25}그 사람은 특정한 부분에서는 정말 철저한 사람이라고.{/cps}"
    ihyun "{cps=25}하지만…{/cps}"
    "{cps=25}김유현이 말을 꺼냈다.{/cps}"
    yuhyeon "{cps=25}물론 우연의 경우일 수도 있겠죠.{/cps}"
    yuhyeon "{cps=25}하지만 정말 그런 경우일 때 어떤 방법으로 했을지 생각해 보아야 합니다.{/cps}"
    yuhyeon "{cps=25}그 방법을 아는 순간 실마리를 잡을 수 있을 테니까요.{/cps}"
    yuhyeon "{cps=25}그리고 마지막으로 세 번째입니다. {/cps}"
    yuhyeon "{cps=25}벽의 못이죠.{/cps}"
    "{cps=25}하지만 다음에 이어지는 말은 기대를 충족시켜주지 못했다.{/cps}"
    yuhyeon "{cps=25}아직 이 못이 어떤 역할을 하는지는 잘 모르겠습니다. {/cps}"

    hide yuhyeon_idle
    hide hyunjoo_concerned
    hide ihyun_idle

    stop music fadeout 1

    jump scene21

##21 : 복도
label scene21:
    scene bg hallway with dissolve
    pause (1.0)

    play music "music/sadness.mp3"  fadeout 1
    "{cps=25}복도다.{/cps}"
    "{cps=25}이현은 고현주와 둘이 있었다. {/cps}"

    show hyunjoo_idle at left

    hyunjoo "{cps=25}당신을 이렇게 따로 부른 이유는…{/cps}"
    "{cps=25}그리고 말을 이었다.{/cps}"
    hyunjoo "{cps=25}당신이 제일 중요한 인물이 될 것 같기 때문이야{/cps}"
    "{cps=25}이현은 그 말을 듣고 이해할 수 없다는 표정을 지었다. {/cps}"
    hyunjoo "{cps=25}그래. 그런 반응이 나올 거라 생각했어.{/cps}"

    show ihyun_panic at right

    ihyun "{cps=25}왜 내가 제일 중요한 인물이 될 거라고 생각하시죠?{/cps}"
    ihyun "{cps=25}저는 아무것도 보여준 것이 없는데?{/cps}"
    "{cps=25}그 말에 고현주는 웃으며 말했다.{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_happy at left

    hyunjoo "{cps=25}무언가 보여주어야 중요한 사람이 되는 것은 아니지.{/cps}"
    hyunjoo "{cps=25}그리고 당신이 일을 벌일 것 같다는 말도 아니야.{/cps}"
    hyunjoo "{cps=25}당신이 아마 사건의 중심이 있을 것 같으니 하는 말이라 생각해.{/cps}"
    "{cps=25}이현이 재차 물었다.{/cps}"

    hide ihyun_panic at right
    show ihyun_idle at right

    ihyun "{cps=25}그래서 왜 제가 중요한 인물이 될 거라고 생각하시는지…{/cps}"

    hide hyunjoo_happy at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}당신…{/cps}"
    hyunjoo "{cps=25}선백교에 대해 아는 것이 있어?{/cps}"
    "{cps=25}이현이 뭔가 말하려는 순간 고현주가 다시 말을 꺼냈다.{/cps}"
    hyunjoo "{cps=25}아니.{/cps}"
    hyunjoo "{cps=25}여기 와서 들은 것 이전에 선백교에 대해 들은 것이 있어?{/cps}"
    "{cps=25}이현은 생각했다.{/cps}"
    "{cps=25}과연 자신이 선백교에 대해서 들은 것이 있는가?{/cps}"
    "{cps=25}생각해 보면 없었다.{/cps}"
    hyunjoo "{cps=25}어때?{/cps}"
    hyunjoo "{cps=25}생각해 보면 없지?{/cps}"
    "{cps=25}이현은 조용히 고개를 끄덕였다.{/cps}"
    hyunjoo "{cps=25}나도 좀 신기해.{/cps}"
    hyunjoo "{cps=25}무슨 일로 당신이 여기에 있는 건지.{/cps}"
    hyunjoo "{cps=25}아직도 잘 이해하지 못하겠어{/cps}"
    hyunjoo "{cps=25}보통 그런 경우에는 공범자인 경우가 많긴 한데…{/cps}"
    "{cps=25}고현주는 이현을 바라보며 말했다.{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_happy at left

    hyunjoo "{cps=25}하지만 당신은 공범자는 아닌 것 같아.{/cps}"
    hyunjoo "{cps=25}당신 선백교에 대해서 아는 것이 있어?{/cps}"
    ihyun "{cps=25}김유현씨에게 조금 들은 것이…{/cps}"
    "{cps=25}고현주는 잠시 고민하는 듯 했다.{/cps}"

    hide hyunjoo_happy at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}…?{/cps}"
    hyunjoo "{cps=25}그렇다면 내 이야기도 들었겠네.{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_concerned at left

    hyunjoo "{cps=25}흠…{/cps}"
    "{cps=25}고현주는 팔짱을 풀며 말했다.{/cps}"

    hide hyunjoo_concerned at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}그 사람이 말해준 것은 아마 대부분이 진실일 거야.{/cps}"
    hyunjoo "{cps=25}물론 그 사람이 이상한 것을 말했다고 해도 내가 굳이 변명할 이유는 없지.{/cps}"
    hyunjoo "{cps=25}누구 말을 들을지는 당신의 선택이니까.{/cps}"
    "{cps=25}바람이 세차게 분다.{/cps}"
    hyunjoo "{cps=25}고작 1박2일짜리 여행에 무슨 일이 생길 거라고 생각하고 온 사람은 없었겠지.{/cps}"
    ihyun "{cps=25}당신도 초대를 받고 온 건가요?{/cps}"
    hyunjoo "{cps=25}맞아.{/cps}"
    hyunjoo "{cps=25}원래 이런 분위기를 좋아하거든.{/cps}"
    hyunjoo "{cps=25}유람선 파티라던가… 시끌벅적한 분위기{/cps}"
    ihyun "{cps=25}그래서 당신이 제게 하려는 이야기는 무엇이죠?{/cps}"
    "{cps=25}고현주는 약간 웃음을 지으며 말했다.{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_cold at left

    hyunjoo "{cps=25}정말 성급하네.{/cps}"
    hyunjoo "{cps=25}그냥 과거의 이야기야.{/cps}"
    hyunjoo "{cps=25}교주에 관한…{/cps}"

    hide hyunjoo_cold at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}우리는 교주를 K라고 불렀었어.{/cps}"

    hide ihyun_idle at right
    show ihyun_panic at right

    ihyun "{cps=25}뭐라고요?{/cps}"
    "{cps=25}순간 이현의 머리에는 상담사 K씨가 떠올랐다.{/cps}"
    hyunjoo "{cps=25}왜 그래?{/cps}"
    hyunjoo "{cps=25}아는 사람이 있어?{/cps}"
    "{cps=25}이현은 황급히 말을 얼버무렸다.{/cps}"

    hide ihyun_panic at right
    show ihyun_idle at right

    ihyun "{cps=25}아니에요. 그냥 계속 얘기 하세요.{/cps}"
    hyunjoo "{cps=25}그래…{/cps}"
    hyunjoo "{cps=25}교주는 정말 대단한 사람이었지.{/cps}"
    hyunjoo "{cps=25}웅변 실력이며 사람을 휘어잡는 것…{/cps}"
    hyunjoo "{cps=25}그리고 말하는 것에 신뢰가 가게 만드는 그 느낌.{/cps}"
    hyunjoo "{cps=25}정말 대단했어.{/cps}"
    hyunjoo "{cps=25}그리고 자신이 원하는 것을 이루어 낼 수 있다고 생각하는 사람이었지.{/cps}"
    hyunjoo "{cps=25}물론 수단과 방법을 가리지 않는다는 점은 있었지만 말이야.{/cps}"
    hyunjoo "{cps=25}그래서 김유현씨에게 이야기를 들었다면…{/cps}"
    hyunjoo "{cps=25}내가 사고를 당했던 사실도 들었겠지?{/cps}"
    "{cps=25}이현은 고개를 끄덕였다. {/cps}"
    hyunjoo "{cps=25}하…{/cps}"
    hyunjoo "{cps=25}무슨 말을 해야 할까?{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_angry at left

    hyunjoo "{cps=25}사람들을 버리고 도망가자고 한 것은 교주였어.{/cps}"
    hyunjoo "{cps=25}그리고 시욱 할아버지나 박준규같은 놈들은 그 말에 찬성했지.{/cps}"
    hyunjoo "{cps=25}하지만 그 말을 듣는 순간 나는 참을 수가 없었어.{/cps}"
    hyunjoo "{cps=25}자신의 안위를 위해서 사람들을 위험에 빠트린다고?{/cps}"
    hyunjoo "{cps=25}그게 말이나 되는 소리라고 생각해?{/cps}"
    hyunjoo "{cps=25}나는 정말 격렬히 반대했지.{/cps}"
    ihyun "{cps=25}그럼 사고를 당한 이유가…{/cps}"
    "{cps=25}고현주는 한숨을 쉬더니 말했다. {/cps}"

    hide hyunjoo_angry at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}그렇지.{/cps}"
    hyunjoo "{cps=25}반대를 했으니까 임원들은 나를 임원들끼리 있던 방에 가두고 탈출했어.{/cps}"
    hyunjoo "{cps=25}나는 그 때 평신도들과 같이 있지 않았기 때문에 오히려 살 수 있었지만.{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_happy at left

    hyunjoo "{cps=25}그 날 이후로 이름도 바꾸고 얼굴도 바꾸고 이렇게 살고 있지.{/cps}"
    "{cps=25}고현주는 소리없이 웃었다. {/cps}"
    hyunjoo "{cps=25}정말 의사들이 대단하다는 생각밖에 들지 않더라고.{/cps}"

    hide hyunjoo_happy at left
    show hyunjoo_idle at left

    hyunjoo "{cps=25}그런데 이 얘기를 해준 것은 다른 건 아니고.{/cps}"

    hide hyunjoo_idle at left
    show hyunjoo_concerned at left

    hyunjoo "{cps=25}당신… 김유현씨를 정말 믿어?{/cps}"
    "{cps=25}고현주가 정색을 하며 물었다. {/cps}"
    hyunjoo "{cps=25}정말 김유현씨를 믿을 수 있어?{/cps}"
    "{cps=25}이현의 얼굴이 딱딱해졌다. {/cps}"
    "{cps=25}김유현을 믿을 수 있을까?{/cps}"
    "{cps=25}그것은 이현에게 한 번도 생각해 본 적이 없는 질문이었다. {/cps}"
    hyunjoo "{cps=25}당신… 몇 번 느껴봤을 거야.{/cps}"
    hyunjoo "{cps=25}그 사람의 통찰력이라던과 상황 판단 능력 같은 것을.{/cps}"
    hyunjoo "{cps=25}그 사람을 믿을 수 있어?{/cps}"

    menu:
        "화를 내며 믿을 수 있다고 말한다.":
                jump sfirst
        "의심스러운 부분도 있다고 동조한다.":
                jump ssecond

label sfirst:
    ihyun "{cps=25}무슨 말씀을 하시는 겁니까!{/cps}"
    hyunjoo "{cps=25}당황스럽네…{/cps}"
    "{cps=25}고현주는 약간 쓰게 웃음을 지었다.{/cps}"
    ihyun "{cps=25}당신처럼 이런 상황 속에서 이간질하는 사람은 믿을 수 없습니다.{/cps}"
    ihyun "{cps=25}괜히 시간만 뺏긴 것 같군요.{/cps}"
    hyunjoo "{cps=25}그래…?{/cps}"
    "{cps=25}고현주는 돌아서며 말했다.{/cps}"
    hyunjoo "{cps=25}그런 사람에게 굳이 더 말해줄 이유는 없지…{/cps}"
    hyunjoo "{cps=25}재미있는 시간이었어 이현씨.{/cps}"
    "{cps=25}이현은 자신의 방으로 가는 고현주를 가만히 서서 바라보았다. {/cps}"
    "{cps=25}고현주가 방금 한 질문에 대해서 생각하며…{/cps}"
    "{cps=25}꽤 오랜 시간을 자신의 방문 앞에서 보냈다. {/cps}"

    jump scene22

label ssecond:
    hide ihyun_idle at right
    show ihyun_concerned at right
    ihyun "{cps=25}확실히 그렇군요…{/cps}"
    "{cps=25}이현은 김유현을 처음 만났을 때를 생각했다. {/cps}"
    "{cps=25}어디로 가야 하는지 묻지도 않았는데 바로 말하는 상황 판단 능력{/cps}"
    "{cps=25}그리고 그 정보를 얻기까지 필요했던 관찰력{/cps}"
    "{cps=25}사람들을 꿰뚫어보는 통찰력{/cps}"
    "{cps=25}무엇 하나 평범하게 느껴지는 사람은 아니다.{/cps}"
    "{cps=25}하지만 아까 상황은 어땠지?{/cps}"
    ihyun "{cps=25}그 자리에서 무언가 대답을 꺼내지 못했을 때 이상하다는 느낌이 들기도 했어요.{/cps}"
    hyunjoo "{cps=25}맞아.{/cps}"
    hyunjoo "{cps=25}그런 사람이 그렇게 말한다는 것은{/cps}"
    hyunjoo "{cps=25}무언가 숨기고 있다고 밖에 생각되지 않아.{/cps}"
    "{cps=25}고현주는 주위를 둘러보더니 말했다. {/cps}"
    hyunjoo "{cps=25}그리고 선백교 사건 이후로 가장 일이 풀리지 않은 사람이 누구일까?{/cps}"
    hyunjoo "{cps=25}나?{/cps}"
    hyunjoo "{cps=25}나는 이 생활에 만족해. 새로 얻은 직장도 만족하고…{/cps}"
    hyunjoo "{cps=25}새로운 인생을 살고 있는데 불만이 있을 리가 없지.{/cps}"
    hyunjoo "{cps=25}정시욱씨?{/cps}"
    hyunjoo "{cps=25}아니면 준규랑 조정은씨 그 커플…?{/cps}"
    hyunjoo "{cps=25}아니면 너네 동생일까?{/cps}"

    hide ihyun_concerned at right
    show ihyun_idle at right

    ihyun "{cps=25}흠…{/cps}"
    "{cps=25}고현주는 다시 팔짱을 끼며 말했다.{/cps}"
    hyunjoo "{cps=25}아무리 생각해도 김유현이라고 생각되지 않아?{/cps}"
    hyunjoo "{cps=25}그 사건 이후로 경찰이라는 직업을 잃었고.{/cps}"
    hyunjoo "{cps=25}흥신소를 운영하고 있긴 하지만 이게 잘 될까?{/cps}"
    hyunjoo "{cps=25}그리고 이번에 온 이유도 들어 봤어?{/cps}"
    hyunjoo "{cps=25}예전 미제 사건의 단서를 알려주겠다고 해서 찾아온거야.{/cps}"
    hyunjoo "{cps=25}그렇게 과거를 못 잊는 사람이 이런 일을 벌였다는 생각은 안해봤어?{/cps}"
    "{cps=25}이현은 한숨을 쉬었다.{/cps}"
    "{cps=25}고개를 젖히자 벽에 머리가 닿는 것이 느껴진다. {/cps}"
    "{cps=25}차가운 냉기가 머리를 타고 들어오는 느낌이다. {/cps}"
    "{cps=25}하지만 한번 꼬인 머리는 풀리지 않았다.{/cps}"

    hide ihyun_idle at right
    show ihyun_concerned at right

    ihyun "{cps=25}잠시 혼자 생각을 해도 될까요?{/cps}"
    ihyun "{cps=25}아니…{/cps}"
    ihyun "{cps=25}이제부터는 혼자 있고 싶네요.{/cps}"
    "{cps=25}고현주는 잠시 이현을 바라보았다.{/cps}"
    hyunjoo "{cps=25}그래.{/cps}"
    hyunjoo "{cps=25}아마 당신도 많이 머릿속이 복잡하겠지.{/cps}"
    hyunjoo "{cps=25}하지만 한번 잘 생각해 보라고.{/cps}"
    hyunjoo "{cps=25}너를 지키기 위해 무엇이 필요할지 말이야.{/cps}"

    hide hyunjoo_idle
    hide ihyun_concerned

    stop music fadeout 1
    jump scene22

##22 : 이현의 방 안
label scene22:
    scene bg ihyun room with dissolve
    pause (1.0)

    show ihyun_concerned at left

    play music "music/regret.mp3" fadeout 1

    ihyun "{cps=25}하…{/cps}"
    "{cps=25}이현은 침대에 누워서 한숨을 쉬었다.{/cps}"

    hide ihyun_concerned at left
    show ihyun_idle at left

    ihyun "{cps=25}하나도 모르겠다.{/cps}"
    "{cps=25}정말 그 말 이외에 다른 말이라고는 나오지 않았다. {/cps}"
    ihyun "{cps=25}솔이는 괜찮을까…{/cps}"
    "{cps=25} {/cps}"



    menu:
        "이솔의 방을 찾아간다.":
                jump badend1
        "혼자 머리속으로 생각한다.":
                jump tfirst

label badend1:
    "{cps=25}아무래도 이솔이 걱정이 된다. {/cps}"
    ihyun "{cps=25}지금이 몇시지?{/cps}"
    "{cps=25}시계를 보니 새벽 2시이다. {/cps}"
    ihyun "{cps=25}나갔다가 살인마를 만나기 딱 좋은 시간이네.{/cps}"
    "{cps=25}이현은 침대에서 일어나서 밖으로 나갔다. {/cps}"
    "{cps=25}바깥은 바람이 세차게 불고 있었다. {/cps}"
    ihyun "{cps=25}바람이 센데…{/cps}"
    "{cps=25}이현은 잠시 한 바퀴를 둘러보기로 결정했다. {/cps}"

    stop music fadeout 1
    play music "music/opening.mp3" fadeout 1

    "{cps=25}이현이 복도의 절반쯤을 지나왔을 때 누군가의 방문이 열렸다. {/cps}"

    hide ihyun_idle at left
    show ihyun_panic at left

    ihyun "{cps=25}뭐… 뭐야!{/cps}"
    "{cps=25}그리고 그 방문에선 누군가가 뛰쳐나와 이현을 찔렀다. {/cps}"

    hide ihyun_panic at left
    show ihyun_pale at left

    ihyun "{cps=25}커… 커억…{/cps}"
    "{cps=25}이현은 고개를 들어 상대방을 보려고 했지만 고개를 들 수 없었다. {/cps}"
    "{cps=25}이윽고 눈꺼풀이 무거워지고 어둠이 깔리기 시작했다. {/cps}"

    stop music fadeout 3

    scene bg blackscreen
    with dissolve

    "{cps=5}BAD END : 너무 빠른 종결{/cps}"

    return

label tfirst:
    "{cps=25}이현은 이솔의 생각을 하다가 아무래도 오늘 들은 말을 정리해 보기로 했다.{/cps}"

    hide ihyun_idle at left
    show ihyun_concerned at left

    ihyun "{cps=25}내가 김유현씨를 믿을 수 있을까?{/cps}"
    "{cps=25}생각해보면 맞는 말이다. {/cps}"
    "{cps=25}그 날 이후로 가장 불행해진 사람이 누구일까 생각을 해 봐도…{/cps}"
    "{cps=25}김유현이 맞는 것 같다. {/cps}"
    ihyun "{cps=25}그리고 무언가를 숨기고 있는 것 같긴 해.{/cps}"
    "{cps=25}이현은 내일은 다른 일이 벌어지지 않기를 바라면서 잠을 청했다. {/cps}"
    stop music fadeout 1

    hide ihyun_concerned

    jump scene23

##23 : 이현의 방 안
label scene23:

    scene bg blackscreen
    with Dissolve(2.0)

    scene bg ihyun room
    with Dissolve(3.0)

    play music "music/quiet.mp3" fadeout 1

    "{cps=25}이현의 방{/cps}"

    show ihyun_pale at left

    ihyun "{cps=25}헉… 헉…{/cps}"
    "{cps=25}이현이 식은땀을 흘리고 있다.{/cps}"
    "{cps=25}떨리는 손을 들어 핸드폰을 확인한다. {/cps}"
    "{cps=25}시간은 6시 18분.{/cps}"
    "{cps=25}이현이 자기 시작한지 한 시간도 되지 않았다. {/cps}"

    hide ihyun_pale at left
    show ihyun_concerned at left

    ihyun "{cps=25}하…{/cps}"
    "{cps=25}이현은 정말 피곤하다는 생각을 했다. {/cps}"

    hide ihyun_concerned at left
    show ihyun_idle at left

    ihyun "{cps=25}아무래도 지금 또 잠들기에는 너무 시간이 늦어 버렸지.{/cps}"
    "{cps=25}이현은 외투를 대충 걸치고 밖으로 나섰다. {/cps}"

    hide ihyun_idle
    stop music fadeout 1

    scene bg blackscreen
    with Dissolve(3.0)

    jump scene24

##24 : 이현의 방 앞 복도
label scene24:

    scene bg cruisehall
    with Dissolve(3.0)

    play music "music/Cruise Whitnoise.mp3" fadeout 1

    "{cps=25}아직 해가 뜨지 않았다. {/cps}"
    "{cps=25}보통 11월 말에는 약 7시 정도에 해가 뜨니…{/cps}"
    "{cps=25}아직 해가 뜨려면 40분 정도를 더 기다려야 한다. {/cps}"

    show ihyun_concerned at left

    ihyun "{cps=25}후…{/cps}"
    "{cps=25}입에서 하얀 입김이 나오는 것이 보인다. {/cps}"

    hide ihyun_concerned at left
    show ihyun_idle at left

    ihyun "{cps=25}오늘로써… 3일째인가…{/cps}"
    "{cps=25}아직 해상경찰은 도착하지 않았다. {/cps}"
    "{cps=25}아마 조만간 도착하겠지 라는 생각을 해 본다. {/cps}"
    ihyun "{cps=25}솔이에게 가볼까?{/cps}"
    "{cps=25}하지만 시간이 너무 이르다.{/cps}"
    "{cps=25}아무래도 가는 것은 별로 좋은 생각은 아닌 듯 하다. {/cps}"

    hide ihyun_idle at left
    show ihyun_concerned at left

    ihyun "{cps=25}김유현씨를 믿을 수 있을까?{/cps}"
    "{cps=25}이현은 갑자기 그런 생각이 들었다. {/cps}"
    "{cps=25}어제 밤 복도 앞에서 고현주와 했던 이야기가 떠오른다. {/cps}"
    "{cps=25}김유현을 믿을 수 있을까…?{/cps}"
    "{cps=25}이현은 생각하며 걷기 시작했다. {/cps}"
    "{cps=25}자신의 방문 앞에서 이솔의 방쪽으로 향해 걷고 있을 때,{/cps}"
    "{cps=25}툭!{/cps}"
    "{cps=25}이현이 순간적으로 휘청거렸다. {/cps}"

    hide ihyun_concerned at left
    show ihyun_panic at left

    ihyun "{cps=25}뭐… 뭐야?{/cps}"
    "{cps=25}이현의 풀린 신발끈이 바닥의 홈에 끼어 걸려 넘어질 뻔하게 만들었다.{/cps}"

    hide ihyun_panic at left
    show ihyun_idle at left

    ihyun "{cps=25}뭔가에 찍힌 자국인가?{/cps}"
    "{cps=25}이현은 앉아서 바닥의 홈에서 조심스럽게 신발끈을 빼냈다. {/cps}"
    "{cps=25}시간이 얼마나 지났을까…{/cps}"
    "{cps=25}생각을 오랫동안 한 듯 하다. {/cps}"
    "{cps=25}조금씩 지평선이 밝아오기 시작한다. {/cps}"

    ihyun "{cps=25}오늘도 또다시 하루가 시작하네…{/cps}"
    "{cps=25}그렇게 새로운 하루가 시작되었다. {/cps}"

    stop music fadeout 3
    hide ihyun_idle

    scene bg blackscreen
    with Dissolve(3.0)

    jump scene25

##25 : 식당
label scene25:

    scene bg partyroom
    with Dissolve(3.0)

    play music "music/sadness.mp3" fadeout 1

    "{cps=25}식당이다. {/cps}"
    "{cps=25}이현은 이솔을 데리고 식당에 도착했다. {/cps}"
    "{cps=25}식당에 도착하자 이솔이 말했다.{/cps}"

    show isol_pale at left

    isol "{cps=25}오빠… 고현주씨가 보이지 않아…{/cps}"

    hide isol_pale

    "{cps=25}그랬다. {/cps}"
    "{cps=25}고현주씨가 보이지 않았다. {/cps}"
    "{cps=25}아직 오지 않은 사람이 있었지만 불안한 마음이 드는 것은 어쩔 수 없다. {/cps}"

    show ihyun_concerned at left

    "{cps=25}이현은 고개를 들어 게시판을 보았다. {/cps}"
    "{cps=25}게시판에는 원숭이가 입을 막고 있는 모양의 인형이 매달려 있었다. {/cps}"

    show yuhyeon_concerned at right

    yuhyeon "{cps=25}안 그래도 얘기하려 했네.{/cps}"
    "{cps=25}김유현은 인형을 들고 말했다. {/cps}"

    hide yuhyeon_concerned at right
    show yuhyeon_idle at right

    yuhyeon "{cps=25}이 인형은 일본 설화 중 하나지.{/cps}"
    yuhyeon "{cps=25}안 좋은 것은 보지도 말고, 듣지도 말고, 말하지도 말라.{/cps}"
    yuhyeon "{cps=25}생각보다 유명한 설화지.{/cps}"
    "{cps=25}그리고 김유현은 말을 잠시 멈췄다. {/cps}"
    yuhyeon "{cps=25}이 인형이 매달려 있다는 것은…{/cps}"
    yuhyeon "{cps=25}단순히 설화 이야기를 해 주려고 단 것은 아니겠지.{/cps}"


    ihyun "{cps=25}설마…{/cps}"

    hide yuhyeon_idle at right
    show yuhyeon_concerned at right

    "{cps=25}김유현은 심각한 표정을 지으며 말했다. {/cps}"
    yuhyeon"{cps=25}그래. 새로운 피해자가 생겼다는 뜻이겠지. {/cps}"


    show jungyu_idle at slightright
    show jungeun_idle at slightleft

    "{cps=25}김유현과 이현이 이야기하고 있을 때 조정은과 박준규가 들어왔다. {/cps}"

    yuhyeon "{cps=25}아무래도 피해자가 누구인지는 정해진 것 같군…{/cps}"
    "{cps=25}이현은 그 말을 듣자마자 밖으로 뛰어 나갔다. {/cps}"

    hide jungyu_idle at slightright
    show jungyu_panic at slightright

    jungyu "{cps=25}뭐야! 무슨 일이야!{/cps}"
    "{cps=25}뒤에서 박준규가 무언가 말하는 것을 듣긴 했지만 굳이 뒤돌아보지 않았다. {/cps}"

    stop music fadeout 3

    hide yuhyeon_concerned
    hide ihyun_concerned
    hide jungyu_panic
    hide jungeun_idle

    scene bg blackscreen
    with Dissolve(3.0)

    jump scene26

##26 : 고현주의 방 앞
label scene26:

    scene bg cruisehall
    with Dissolve(3.0)

    play music "music/nervous.mp3" fadeout 1

    "{cps=25}고현주의 방 앞이다. {/cps}"
    "{cps=25}벌써부터 혈향이 퍼지는 듯 하다.{/cps}"
    "{cps=25}분명 어제까지 같이 얘기도 하고 있었는데…{/cps}"
    "{cps=25}문을 밀어 보지만 전혀 움직이지 않는다.{/cps}"
    "{cps=25}잠겨 있다. {/cps}"
    "{cps=25}이현은 발을 들어 문을 힘껏 찍었다.{/cps}"
    play sound "sounds/bang.wav"
    "{cps=25}쾅!{/cps}"
    play sound "sounds/bang.wav"
    "{cps=25}쾅! 쾅!{/cps}"
    play sound "sounds/bang2.wav"
    "{cps=25}쾅! 콰직!{/cps}"
    "{cps=25}결국 큰 소리가 들리며 문이 떨어져 나갔다. {/cps}"
    "{cps=25}문을 부수는 동시에 사람들이 하나 둘씩 나타나기 시작했다. {/cps}"

    show yuhyeon_angry at left

    yuhyeon "{cps=25}어떤가! 상황은!{/cps}"
    "{cps=25}김유현도 나름대로 마음이 급한지 평소에 쓰는 존칭어가 아니었다. {/cps}"

    show ihyun_pale at right

    ihyun "{cps=25}죽었어요…{/cps}"
    "{cps=25}사람들은 아직 방 안으로 들어가지 않는 이현의 근처로 하나 둘씩 모였다. {/cps}"

    show jungeun_pale at slightleft

    jungeun "{cps=25}세상에…{/cps}"

    show jungyu_angry at slightright

    jungyu "{cps=25}크윽…{/cps}"

    stop music fadeout 1

    "{cps=25}그리고 방 안에는 고현주의 시체가 목이 매달린 채로 있었다. {/cps}"

    hide yuhyeon_angry
    hide ihyun_pale
    hide jungeun_pale
    hide jungyu_angry

    scene bg blackscreen
    with Dissolve(3.0)

    jump scene27

##27 : 고현주의 방
label scene27:

    scene bg other rooms
    with Dissolve(3.0)

    play music "music/quiet.mp3" fadeout 1

    "{cps=25}고현주의 방 안으로 들어왔다. {/cps}"
    "{cps=25}방의 천장에는 이전과 비슷한 문구가 쓰여 있었다. {/cps}"
    "{cps=25}양들끼리 서로 피해를 주는 거짓말을 하지 말라{/cps}"

    show yuhyeon_concerned at left

    yuhyeon "{cps=25}일단 고현주씨를 살펴보죠.{/cps}"
    "{cps=25}밧줄에 목이 매달린 고현주를 내리고 김유현은 시신을 살펴보기 시작했다.{/cps}"

    hide yuhyeon_concerned at left
    show yuhyeon_idle at left

    yuhyeon "{cps=25}흠…{/cps}"
    yuhyeon "{cps=25}목 주위에 상처가 없군요.{/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_concerned at left

    yuhyeon "{cps=25}단순하게 줄로 생긴 하나의 자국…{/cps}"

    show jungyu_panic at right

    jungyu "{cps=25}그게 무슨 의미가 있나?{/cps}"
    jungyu "{cps=25}목을 밧줄로 매달았는데?{/cps}"
    jungyu "{cps=25}당연히 자국정도는 생길 수 있는 것 아닌가?{/cps}"
    "{cps=25}박준규는 이상하다는 듯이 말했다.{/cps}"
    yuhyeon "{cps=25}이 말뜻은 자살이 아니라는 뜻입니다. {/cps}"

    hide yuhyeon_concerned at left
    show yuhyeon_idle at left

    yuhyeon "{cps=25}죽은 다음에 매달렸다는 의미이지요.{/cps}"
    yuhyeon "{cps=25}이렇게 목을 매달아서 죽게 될 경우에 목 주위에 저항흔이라고 하는 것이 생깁니다. {/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_concerned at left

    yuhyeon "{cps=25}하지만 이 경우에는 그렇지 않군요.{/cps}"
    "{cps=25}갑자기 가만히 있던 조정은이 말을 꺼냈다. {/cps}"

    show jungeun_idle at slightleft

    jungeun "{cps=25}죄송한데 저… 조금 나가 있어도 될까요?{/cps}"

    show isol_idle at slightright

    isol "{cps=25}… 저도{/cps}"

    hide jungeun_idle
    hide isol_idle

    "{cps=25}그러고는 조정은과 이솔은 방 밖으로 나갔다. {/cps}"
    "{cps=25}방 안에는 김유현과 박준규, 이현이 남게 되었다. {/cps}"

    hide yuhyeon_concerned at left
    show yuhyeon_idle at left

    yuhyeon "{cps=25}이번에도 아마 트릭은 같은 것을 사용했을 거네.{/cps}"
    yuhyeon "{cps=25}방 안에 박힌 4개의 못으로 고정된 원숭이 인형{/cps}"
    yuhyeon "{cps=25}그리고 원래부터 잠겨 있던 문…{/cps}"
    "{cps=25}김유현은 한숨을 내뱉었다.{/cps}"

    hide yuhyeon_idle at left
    show yuhyeon_concerned at left

    yuhyeon "{cps=25}무슨 일인지 모르겠군…{/cps}"

    stop music fadeout 3

    hide yuhyeon_concerned
    hide jungyu_panic

    scene bg other rooms
    with Dissolve(3.0)

    jump scene28

##28 : 식당
label scene28:

    scene bg cafeteria
    with Dissolve(3.0)

    play music "music/hint.mp3" fadeout 3

    "{cps=25}박준규가 자신의 방으로 돌아가고 김유현과 이현은 식당으로 돌아왔다.{/cps}"

    show yuhyeon_panic at left

    yuhyeon "{cps=25}이게… 무슨…{/cps}"
    "{cps=25}김유현이 바라본 곳에는 게시판이 있었다.{/cps}"
    "{cps=25}게시판에는 새로운 무언가가 걸려 있었다. {/cps}"

    hide yuhyeon_panic at left
    show yuhyeon_concerned at left

    yuhyeon "{cps=25}하트…?{/cps}"
    "{cps=25}이현이 다급하게 말했다. {/cps}"

    show ihyun_concerned at right

    ihyun "{cps=25}아직 시간이 많이 흐르지 않았습니다. 생각해보죠. {/cps}"
    ihyun "{cps=25}범인이 누구인지를…{/cps}"

    hide yuhyeon_concerned
    hide ihyun_concerned

    scene bg blackscreen
    with Dissolve(3.0)

    "{cps=5}to be continued...{/cps}"

    return
