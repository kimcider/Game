init 20:
    image ecg ketsuni 1 = "ecg/ketsuni1.png"
    image ecg ketsuni 2 = "ecg/ketsuni2.png"
    image ecg ketsuni 3 = "ecg/ketsuni3.png"
    image ecg end2 = "ecg/end2.png"

label scene421:

    scene background oldclass
    show yeongwon shock with dissolve
    yeongwon "방금 그 말... 진심이신가요...?"
    show yeongwon shock:
        moveleft
    with Pause(0.5)
    show principal idle
    with dissolve
    show haneul idle at right
    with dissolve
    show background oldclass dark
    with dissolve
    "솔직히 쉽게 믿을 수는 없었다."
    "그도 그럴 것이, 원장이 내건 조건은 지나치게 파격적이었으니까 말이다."
    play sound "effect/heartbeat.ogg"
    "원장을 따라가면 나와 주변 인물들의 목숨을 나에게 맡기겠다니. 이건..."
    "제안을 빌미 삼아 사실상 나에게 이쪽에 붙으라는 말이나 다름없었다."
    "하지만 순순히 따르는 것이 최선의 방법일지도 모른다."
    "이대로 원장의 계획을 파낼 수도 있을 것이다."
    "그렇다면, 하늘이를 구할 수 있을 뿐 아니라..."
    "한설이나 연우 같은 피해자가 더는 나오지 않게 할 수도 있어."
    "......좋아. 결심했어."
    show background oldclass
    with dissolve
    play music "music/G11.mp3"
    show yeongwon idle
    with dissolve
    yeongwon "선생님... 정말로 그렇게 해주실 수 있다면, 저는..."
    show haneul shock
    with dissolve
    haneul "영원아, 정신 차려!! 지금 뭐 하려는 거야!!!"
    haneul "넘어가지 마!!! 저 손에 연우와 한설이가 죽은 거나 마찬가지잖아!!!"
    show haneul sad
    haneul "이러다 너마저 그렇게 되어 버린다면... 영원아, 제발..."
    show keibi at slightright behind principal
    with dissolve
    show principal idle
    with dissolve
    principal "...영원이와 단 둘이서만 이야기하고 싶네요."
    hide keibi
    hide haneul
    with dissolve
    show principal idle:
        moveright
    with Pause(0.5)
    "원장의 말이 끝나기가 무섭게 경비가 하늘이를 데리고 밖으로 나가려 했다."
    "끌려 나가던 하늘이는 경비를 뿌리치고 자신의 발로 걸어 나갔다."
    "화난 듯 거칠게 내닫는 발걸음 소리마다 내 가슴도 덩달아 울렸다."
    "몇 대 얻어 맞은 것처럼, 너무나도 아팠다."
    show yeongwon shock
    with dissolve
    yeongwon "기다려! 하늘아!!!"
    "하늘이를 잡아야 한다는 생각이 들어서였을까, 나도 모르게 목소리가 터져 나왔다."
    "가장 소중한 사람, 나를 이해해줄 수 있을 유일한 사람."
    "항상 내 편이 되어 준 하늘이..."
    "그 모든 기대감을 품은 채 나도 간절한 얼굴로 하늘이를 쳐다보았다."
    "하지만, 돌아선 그의 반응은 싸늘했다. 단지 나를 슬픈 눈으로 쳐다볼 뿐이었다."
    "어째서... 하늘아..."
    stop music fadeout 1.0
    show principal idle2
    with dissolve
    show yeongwon shock
    with dissolve
    principal "이제 우리 둘만 남았으니까... 하던 이야기를 계속 해볼까?"
    principal "영원아, 아까 전처럼 애매하게 대답하지 말고, 이번에는 확실하게 해주렴."
    principal "정말로 내 제안을 받아들일 생각이니?"
    "이제 더 이상은 주저할 수 없다. 내 선택이 옳았다는 것을 모두에게 증명해 \n보일 거야."
    "이게 최선이니까..."
    show yeongwon serious2
    with dissolve
    yeongwon "...네. 알겠어요, 원장 선생님. 선생님의 제안을 받아들일게요."

label part2:
    scene background black
    with fade
    play music "music/L50.mp3"
    "마음 속에서 계속 불길한 기운이 스멀스멀 피어오른다."
    scene background principaloffice dark
    with dissolve
    "잘못된 선택을 한 것은 아닌지 회의감이 든다."
    show background principaloffice
    with dissolve
    "나와 함께 해온 소중한 친구들이 저렇게 반응한다면, 다른 아이들은 안 봐도 \n뻔할 노릇이다."
    "왜 모두들 나에게 원망의 눈초리만을 보내는 걸까...?"
    "나름대로 깊게 고민해서 내린 결정이었는데."
    "...아니야. 모두들 친한 친구들이잖아. 나중에라도 설명한다면 분명히 이해해 \n줄 거야."
    "그렇게 생각하고, 일단은 내 선택에 따라 나아가자."
    "긍정적으로 생각하려고 노력했지만, 사실 아직까지도 확신이 서지 않는다."
    "친구들이 내 행동을 이해해줄지, 이것이 옳은 선택인지까지 말이다."
    "자꾸만 마음이 흔들리는 것을 견딜 수가 없다."
    stop music fadeout 2.0
    "절대 흔들리지 않을 만큼 생각이 확고했으면 좋았을 텐데..."
    play music "music/L20.mp3"
    show principal happy
    with dissolve
    principal "아 영원아. 배고팠을 텐데, 이거라도 좀 먹어 보렴."
    "고민하고 있느라 원장이 무엇을 하는 지도 살펴보지 못했다."
    "혹시 모르니까 계속 경계를 늦추어서는 안 돼. 일단은 자연스럽게 행동하자."
    show principal happy:
        moveright
    with Pause(0.5)
    show yeongwon happy at left
    with dissolve
    yeongwon "감사합니다. 선생님."
    show yeongwon shock
    yeongwon "어...? 이 음식 혹시, 직접 만드신 건가요?"
    show principal happy
    with dissolve
    principal "그래. 영원아. 너 주려고 내가 일부러 만들었어."
    principal "고아원 안에서 먹었던 거랑은 다르지? 우선 천천히 맛보면서 긴장 풀고 있으렴."
    "...독이라도 든 건 아니겠지? 라고 생각하기에는 너무 배가 고팠다."
    "하지만 그렇다고 무작정 먹기에는 의심이 가는 것도 사실이고..."
    "그렇게 고민하는 새, 원장이 먼저 요리를 조금 맛보았다."
    show principal happy
    with dissolve
    principal "음~ 맛있어... 정말 누가 이런 판타스틱한 요리를 만들었을까~"
    "원장이 먹는 것을 보자 어쩐지 안심이 되었다."
    "그럼 조금만... 먹어볼까..."
    "정신을 차려 보니 어느샌가 음식을 전부 먹어치운 후였다."
    "원장을 향한 경계심은 어느새 사라져 있었다."
    show yeongwon happy
    with dissolve
    yeongwon "정말 너무너무 맛있네요, 원장 선생님."
    show principal happy
    with dissolve
    principal "그렇지? 사실 내가 도도한 이미지랑은 다르게 이런 취미가 있어서 말이야. \n맛있게 먹어 줬다니 고맙네~"
    principal "기분도 좋겠다~ 영원아, 혹시 뭐 필요한 거라도 있니? 해 줄 수 있는 건 해 줄게."
    show yeongwon happy
    with dissolve
    show yeongwon serious
    yeongwon "그럼, 뭐 조금만 물어 봐도 될까요?"
    show yeongwon sad
    yeongwon "친구들... 아까 끌려 나간 친구들은 어떻게 되었죠? 무슨 일이 생긴 건..."
    show principal happy
    with dissolve
    show principal idle
    principal "걱정하지 마. 내가 처음에 제안하지 않았니? 친구들 목숨은 너에게 달려\n 있다고."
    principal "적어도 내가 어떻게 하지는 않을 테니까, 안심해도 돼."

    show yeongwon sad
    with dissolve
    show yeongwon idle
    yeongwon "네. 감사해요. 아, 저, 혹시..."

    show principal idle
    with dissolve
    principal "응?"

    show yeongwon blush
    with dissolve
    yeongwon "너무 긴장해서 그런가, 땀이 너무... 혹시 세면대는 어디 있나요?"

    show principal happy
    with dissolve
    principal "아, 씻어야 하니?"
    principal "세면대 말고, 저쪽 화장실 안에 욕조가 있는데 거기서 목욕 좀 하면서 몸 좀 풀렴."
    principal "왼쪽으로 돌리면 따뜻한 물 나오니까 차가운 물 쓰지 말고. 감기 걸린다."

    scene background black
    with dissolve
    "원장은 생각했던 것과는 다르게 매우 친절했다. 가식일지도 모르지만."
    "하지만 가식이건 아니건, 원장에게는 그 자체만으로 사람의 마음을 흔드는 \n매력이 있다."
    "친구들은 지금쯤 뭘 하고 있을까? 정말 원장의 말대로 아무 일도 없는 걸까?"
    "그것보다, 내가 지금 이곳에서 이런 환대를 받는 것이 과연 맞는 일일까?"
    "아니야. 마음을 다잡아야 해. 친구들을 지키는 길이잖아..."
    "이런저런 생각을 해서인지, 목욕물이 너무 뜨거웠는지, 머릿속이 점점 \n달아오른다."
    "결국 목욕은 얼마 하지 못한 채 밖으로 나올 수밖에 없었다."

    scene background principaloffice
    with dissolve

    show principal shock2
    with dissolve
    principal "어머, 벌써 나오는 거니?"

    show principal shock2:
        moveright
    with Pause(.5)
    show yeongwon happy at left
    with dissolve
    yeongwon "네... 헤헤. 충분히 씻은 것 같아서 그냥 나왔어요."

    show principal idle
    principal "...그건 샤워지 목욕이 아니잖아."
    principal "목욕은 좀 더 오래, 몸이 완전히 풀릴 때까지 하는 거야."

    show yeongwon idle
    with dissolve
    yeongwon "아, 네, 그렇군요."

    show yeongwon sad
    with dissolve
    yeongwon "..."

    show principal shock
    principal "응? 왜 갑자기 말이 없니?"

    show yeongwon happy
    with dissolve
    yeongwon "아무것도 아니에요. 몸이 따뜻해지니까 피곤해져서 그런가..."
    yeongwon "저, 잠은 어디서 자야 하나요?"

    show principal happy2
    with dissolve
    principal "잠은 내 침대에서 자렴. 아, 나는 소파에서 자면 되니까 부담없이 잘 수 있을 \n거야."

    hide principal
    hide yeongwon
    with dissolve

    scene background principaloffice dark
    with dissolve
    "딱히 당신이 어디서 자는지는 안 궁금했는데."
    scene background bed dark
    with dissolve
    "잠옷으로 갈아입은 뒤, 원장의 안내를 따라 침대로 향했다."
    "기숙사의 것과는 전혀 다른 푹신한 침대는 마치 구름 같아서 눕자마자 푹 잠이 \n들 것만 같았다."
    "자리에 누워 이불을 덮자 원장이 내 이마에 조용히 입맞춤을 해 주었다."

    show principal idle
    with dissolve
    principal "오늘 밤이 아무리 어두워도 무섭지는 않을 거야. 내가 계속 곁을 지켜 줄 테니까."
    principal "이제 몸에 힘을 빼고..."
    $ renpy.show("background", what=im.MatrixColor("background/bed.png", im.matrix.brightness(-0.3)))
    with dissolve
    principal "네 정신이 점점 가라앉는 것을 느껴 보렴..."
    stop music fadeout 5.0
    principal "아래로, 아래로,"
    $ renpy.show("background", what=im.MatrixColor("background/bed.png", im.matrix.brightness(-0.5)))
    with dissolve
    principal "더 깊게..."
    scene background black
    with dissolve
    principal "포근한 잠 속에 빠진다... 후훗. 잘 자렴. 영원아."

    play music "music/L50.mp3"
    "언제 잠에 빠졌는지도 기억이 나지 않는다."
    $ renpy.show("background", what=im.MatrixColor("background/principaloffice.png", im.matrix.brightness(-0.3)))
    with dissolve
    "그저 눈을 뜬 순간, 깊은 숙면을 취했다는 느낌이 온 몸을 감쌌다."
    "원장은 내 옆의 소파에 누워 조용히 잠을 자고 있었다."
    show background principaloffice dark
    with dissolve
    "나는 어쩐지 침대에서 일어나기가 싫어서 천장을 바라보며 생각에 빠졌다."
    "어제까지만 해도 난 머릿속에 친구들 걱정 뿐이었는데..."
    "이제는 이 생활이 편안하게만 느껴진다."
    "내가 과연 이렇게 살아도 되는 걸까...?"
    "나중에 다시 친구들을 만나게 되었을 때, 나는 과연 제대로 설명할 수 있을까?"
    "이렇게 사는 게, 정말 모두를 위한 길일까?"
    "두려움이 엄습하기 시작했다."
    "고아원과는 다른 안락한 삶 속에서, 내가 이것을 누릴 자격이 있는지에 대한 회의감부터"
    "나를 원망의 눈초리로 바라볼 친구들의 시선. 그리고,"
    "모두를 위한 일이라 믿었던 내 신념의 흔들림까지 모든 것이 두려웠다."
    show background principaloffice
    with dissolve
    "내 마음의 혼란을 아는지 모르는지, 원장이 나를 대하는 태도는 점점 더 \n부드러워졌다."
    "이런 나를 따뜻하게 대해주는 원장 선생님은 마치 한 번도 본 적 없는 엄마 같았다."
    stop music fadeout 5.0
    "...원장 선생님에게 고민을 털어놓으면 같이 고민해 주시지 않을까?"

    play music "music/L35.mp3"
    show yeongwon serious at left
    with dissolve
    show principal idle at right
    with dissolve
    yeongwon "원장 선생님... 연우가 죽고, 한설이도 제 손으로 죽인 것이나 마찬가지인 \n시점에서..."
    yeongwon "저는 다른 친구들이라도 지켜 주고 싶었어요."
    yeongwon "아니, 아예 연우와 한설이 같은 피해자가 다시는 나오지 않게 하리라고 \n다짐했었죠."
    yeongwon "그래서 선생님의 제안을 받아들였어요."
    show yeongwon sad
    with dissolve
    yeongwon "하지만... 저에게는 차가운 시선만이 돌아왔죠."
    yeongwon "그것 뿐만이 아니에요. 친구들을 버리고 저만 이곳에서 호화롭게 생활하고 \n있어요."
    yeongwon "모두를 위하겠답시고 엄청 고민했는데... 친구들을 버리고 혼자만 이렇게 사는 건 말이 안 돼요."
    yeongwon "선생님. 저는 처음부터 선택을 잘못한 걸까요...?"

    show yeongwon sad
    with dissolve
    "원장은 내 말을 듣고 잠시 생각에 잠기는 듯했다."

    show principal cry at right
    with dissolve
    principal "영원아. 네가 왜 내 제안을 받아들였을 것 같아? 스스로 한번 생각해 봤니?"

    show yeongwon sad
    with dissolve
    yeongwon "혼자서는 여러 번 생각해 봤지만... 선생님은 어떻게 생각하시나요?"

    show principal sad at right
    with dissolve
    principal "넌 남을 지키기 위해서라면 항상 앞에 나서 모든 것을 받아내려 하지."
    principal "아마 내 제안을 들었을 때도... 그런 마음이 있었기 때문에 받아들이겠다는 \n생각을 했을 거야."
    principal "다른 아이들이라면 너처럼 받아들이겠다는 생각을 쉽게 할 수 있었을까?"
    principal "아니지. 대부분은 이런 상황이 닥치면 모두들 빠져나갈 생각만 하고 있었을 거야."
    principal "너는 정말 착하고, 똑똑한 아이란다."
    principal "남을 위해 스스로 무거운 마음의 짐을 질 만큼 정의롭기도 하고."

    show yeongwon blush
    with dissolve
    yeongwon "너무 띄워 주시는 거 아니에요?"

    show principal happy2
    with dissolve
    principal "아하하... 조금 그렇니? 이런 거 별로 안 좋아하는구나."

    show yeongwon idle
    with dissolve
    yeongwon "그런 건 아니에요. 그냥 이야기가 조금 다른 길로 빠진 것 같아서..."

    show principal idle2
    with dissolve
    principal "미안해. 안 그래도 이제 막 중요한 이야기를 하려던 참이야."

    show principal cry
    with dissolve
    principal "영원아, 사람들은 살면서 많은 선택의 기로를 만나."
    principal "아주 중요한 선택도 있을 테지만, 오늘 무엇을 먹으러 갈까 하는 사소한 선택도 있겠지."
    principal "누군가는 잘못된 선택으로 후회하기도 하지만, 다른 누구는 올바른 선택으로 \n주변에 도움을 주지."
    principal "선택이라는 것은 결국 개인의 본성에 달려 있는 것이니까."
    principal "말하자면, 그들이 어떤 사람이냐에 따라 선택에 대처하는 방식이 달라지는 거지."
    principal "영원이 네가 옳은 선택을 판단하는 근거는 친구들을 지키고 싶다는 이타심에서 나와."
    principal "친구들을 위한 선택을 한다는 건 네가 누구보다 착한 마음을 가지고 있다는 \n증거야."
    principal "그러니까 네 선택을 믿어도 좋단다, 영원아. 넌 옳은 일을 하고 있으니까."

    show yeongwon serious at left
    with dissolve
    yeongwon "...그런 걸까요?"

    show principal happy2 at right
    with dissolve
    principal "그런거야. 어쨌든, 영원이가 나에게 고민을 털어 놓다니, 선생님은 정말 기분 \n좋은걸~?"
    principal "아, 그러고 보니 벌써 시간이 이렇게 되었네. 이만 자렴. 선생님이 재워 줄게."

    scene background black
    with dissolve
    "눈을 감았지만 어쩐지 잠이 오지 않는다."
    scene ecg ketsuni 1
    with dissolve
    "어둠 너머로 친구들과의 단란했던 한때가 일렁거린다."
    "저렇게 좋았던 시절도 있었지. 하지만, 연우와 한설이는 죽어 버리고 하늘이와 한별이는..."
    "안 돼. 이대로 모두 떠나가게 둘 수는 없어. 내가 빨리 어떻게든 해야 하는데..."
    "문득 머릿속으로 원장 선생님의 도움을 받으면 어떨까 하는 생각이 스쳐 \n지나갔다."
    "물론 처음에는 연우와 한설이, 하늘이 모두가 원장의 계획과 관련되어 있을 줄 알고 그녀를 경계했지만..."
    "그분의 친절한 보살핌을 받고, 진심어린 조언을 듣자 조금이나마 남아있던 의심은 서서히 흩어져 사라졌다."
    "원장 선생님은 나쁜 사람이 아니었다. 적어도 나한테는 그랬다."
    "그래. 모두를 구하기 위해서는... 게다가 원장 선생님은 내 부탁은 다 \n들어주시잖아."
    "이런저런 생각을 하다 보니 어느샌가 잠이 들었고, 눈을 뜨니 아침 햇살이 나를 반겨 준다."
    "친구들을 구하려면 우선 밖으로 나가야 한다."
    stop music fadeout 1.0
    pause(.5)

    scene background black
    with dissolve
    with Pause(.5)

    scene background principaloffice
    with dissolve

    show yeongwon idle at left
    with dissolve
    show principal idle at right
    with dissolve
    yeongwon "선생님... 부탁이 하나 있어요. 음... 친구들이 어떻게 되었는지 걱정돼요. \n그러니까... 잠깐 나갔다 와도... 괜찮을까요?"
    "약간 불안했지만... 역시나 원장 선생님의 입에서 허락의 말이 나왔다."

    show principal happy2
    with dissolve
    principal "후훗. 당연하지, 영원아. 좋은 시간 보내고 오렴."

label part3:

    scene background principaloffice
    with fade
    play music "music/L41.mp3"
    "드디어... 밖으로 나가 친구들을 만날 수 있는 기회가 찾아 왔다."
    "하지만 조금 무서웠다."
    "헤어질 때 끝이 그다지 좋지는 못했는데... 과연 친구들이 나를 반겨 줄까??"
    "무거운 마음을 안은 채, 복도로 걸어 나간다."

    scene background schoolhallway
    with fade

    show fstudent
    with dissolve
    fstudent "어? 영원이다. 영원아!!"
    fstudent "얘들아! 영원이가 돌아왔어! 빨리 와 봐!"

    scene background classday
    with fade

    show fstudent at left
    with dissolve
    show mstudent at right
    with dissolve
    "내 주변으로 친구들이 모여 들었다."

    show mstudent at slightleft
    with dissolve
    show fstudent at slightright
    with dissolve
    "나에게 무사했냐고 물어 보는 친구, 무슨 일이 있었는지 물어 보는 친구 등등."
    "모두가 나를 걱정해 주고 있었구나..."
    "조금만 기다려 줘. 모두 무사할 수 있도록 내가 이끌어 줄 거야."
    "연우야... 한설아... 너희 같은 피해자가 다시는 나오지 않도록..."
    "그때였다. 누군가 내 머리채를 잡아 끄는 게 느껴지는 게..."

    hide mstudent
    hide fstudent
    with dissolve
    pause(.2)
    show hanbyeol fury2
    with dissolve
    hanbyeol "야! 영원 이 나쁜 년아!!!"
    hanbyeol "진짜 우리 버리고 그 여자 말을 듣는 게 말이나 돼?"
    show hanbyeol sad2
    with dissolve
    hanbyeol "왜 혼자 위험한 데 뛰어드는 거야 왜!!!"
    hanbyeol "정말... 너까지 잃을까봐 얼마나 걱정했는데... 그것도 모르고..."
    "한별이는 내 어깨를 주먹으로 때리다 말고 품에 파묻혀 흐느끼기 시작했다."
    "덩달아 내 눈에서도 눈물이 흐르기 시작했다."

    show hanbyeol sad2:
        moveright
    with Pause(0.5)
    show yeongwon happy at left
    with dissolve
    yeongwon "한별아... 무사했구나. 다행이야..."
    yeongwon "미안해... 걱정 끼쳐서... 정말 미안해."

    show hanbyeol happy at right
    with dissolve
    hanbyeol "...다시 돌아워 줘서, 정말 기뻐."
    hanbyeol "아, 맞다. 하늘이도 널 기다리고 있어. 영원아! 하늘이 만나러 가자!"

    show yeongwon shock
    with dissolve
    yeongwon "응? 하늘이가... 여기에 있다고??"

    show hanbyeol idle
    with dissolve
    hanbyeol "응... 네가 원장을 따라가고, 나랑 하늘이는 경비한테 끌려 나갔잖아. 그런데..."
    hanbyeol "갑자기 경비 아저씨가 나한테 빨리 하늘이 데려가라는 거 있지..."

    "한별이는 소매로 슬쩍 눈물을 닦았다."
    show hanbyeol happy
    with dissolve
    stop music fadeout 2.0
    "헤헤. 어쨌든. 영원아, 빨리 가자. 하늘이 만나러!"

    scene background dayhideout
    with fade
    play music "music/L20.mp3"
    show yeongwon idle at left
    with dissolve
    show hanbyeol idle at right
    with dissolve

    "하늘이는 마지막으로 만났을 때의 그 모습 그대로였다."
    "당장이라도 달려가 껴안고 싶었지만, 어쩐지 우리 둘 사이에 감도는 싸한 기운 때문에 조금 망설여졌다."
    "혹시 아직도 앙금이 남아 있는 건 아닐까...?"
    "그때, 하늘이가 조용히 입을 열었다."

    show haneul happy2 at slightright
    with dissolve
    haneul "돌아와서... 기뻐. 영원아."

    "하늘이가 멋쩍게 웃어 주자 그제서야 마음이 놓였다."
    "그때."
    show haneul serious
    with dissolve
    haneul "영원아, 물어 볼 게 있어. 혹시... 원장실에서 뭔가 이상한 점 있었어?"

    show hanbyeol shock
    with dissolve
    hanbyeol "하늘아, 그 얘기는... 나중에 물어 보기로 했잖아."
    hanbyeol "벌써 물어 보는 건 좀... 마음고생도 심했을 텐데..."

    show haneul serious
    with dissolve
    haneul "아니. 지금 당장 물어봐야 할 것 같아."
    haneul "사실 요즘 이상한 낌새가 이만저만이 아니야..."

    show hanbyeol idle
    with dissolve
    haneul "특별반 학생들을 대상으로 무언가 자행되고 있다는 건 알지?"
    haneul "처음엔 고생했다고 주는 음료수인 줄 알았는데, 날이 갈수록 애들이 \n이상해지면서 낌새가 느껴졌지."
    haneul "아마 그때일 거야. 너희가 나 안 보인다고 했을 무렵이."
    haneul "연우도 그렇게 죽었고... 나도 거의 죽을 뻔했어."
    haneul "하지만 다른 아이들과는 다르게 나는 점점 상태가 좋아졌어."

    show yeongwon shock
    with dissolve
    haneul "그리고 그때부터 신체검사 시간이 부쩍 늘어나기 시작했지."
    haneul "선생님들이 날 주목하고 있다는 것도... 느껴졌고."
    haneul "그러다 그들이 나를 \'성공작\'이라고 부르는 걸 우연히 들었어."
    haneul "마지막 신체검사 시간이 끝났을 때, 원장은 평소 가지 않던 길로 날 데리고 갔어."
    haneul "마치 영원이 네가 미행하려는 걸 미리 알고 너를 유인하려는 것처럼."
    haneul "그리고 그 뒤는 알다시피. 영원이 네가 제안을 수락하자마자, 그들은 날 갑자기 풀어 줬지."
    haneul "영원아, 이게 과연 전부 우연일까...?"
    haneul "난 특별반 아이들이 현이 씨처럼... 생체실험을 받은 것 같다고 생각해."
    haneul "나는 그중 유일한 성공 케이스고."
    yeongwon "... 한별아... 너도 알고 있었어??"
    hanbyeol "응. 하늘이가 풀려난 날, 이야기를 들었어. 너한텐 나중에 말해주려 했는데..."
    haneul "영원아, 시간이 없어. 원장실에서 수상한 일이 있었다면 전부 말해줘."
    haneul "외부인들이 계속 고아원에 드나들고 있고... 곧 무슨 일이 일어날 것 같아."
    haneul "그때가 되기 전에… 고아원 아이들을 모두 탈출시켜야 해. 영원아, 빨리..."
    "...그래서 한별이가 나를 빨리 하늘이와 만나게 해 주려고 했구나."
    "역시. 연우, 한설이, 하늘이 모두 큰 일에 휘말린 거야."
    "하지만 원장 선생님이 수상하다니, 무언가 크게 잘못 알고 있어."
    "모두 구해주기 위해서는 원장의 도움을 받아야 하는데... 친구들을 어떻게든 \n설득하는 수 밖에."
    stop music
    show yeongwon serious2
    with dissolve
    yeongwon "하늘아, 나... 너 믿는 거 알지...?"
    show yeongwon sad2
    with dissolve
    yeongwon "그런데 이번에 네가 하는 말에는 동의해 줄 수가 없어."
    show yeongwon serious2
    with dissolve
    yeongwon "원장은 정말 좋은 사람이었어. 너희가 생각하는 것보다 훨씬."
    yeongwon "그런 사람이 수상하다니... 그건 좀 아닌 것 같아."
    show hanbyeol shock2
    show haneul shock
    with dissolve
    with Pause(.5)
    show yeongwon shock2
    with dissolve
    yeongwon "무, 물론 완전히 신뢰하는 건 아니야! 우리가 모르는 데서 뭔가 어두컴컴한 일을 할지도 모르지만!"
    show yeongwon serious2
    with dissolve
    yeongwon "그래도 나는 원장이 너희 생각만큼 나쁜 사람이라고는 생각하지 않아."
    pause(.5)
    haneul "....!?"
    play music "music/L44.mp3"
    hanbyeol "뭐, 뭐야. 영원아, 지금 하늘이보다 원장 그 여자를 더 믿는 거야?"
    show hanbyeol fury2
    with dissolve
    hanbyeol "아니지...? 그래. 분명 원장한테 입막음을 당했다거나... 그랬을 거야."
    hanbyeol "영원아, 우리한테는 솔직하게 말해도 돼! 우리가 널 지켜줄 수 있어!"

    show yeongwon sad
    with dissolve
    yeongwon "아니야. 얘들아 제발... 날 믿어줘."
    yeongwon "너희가 원장을 믿지 않을지는 모르지만, 적어도 나는 믿어 줄 수 있을 거 \n아니야…"
    haneul "영원아...?"
    yeongwon "연우랑 한설이가 그렇게 가고, 하늘이 너도 온갖 고통을 겪고..."
    yeongwon "난 정말 하루하루 죽지 못해 살아갈 뿐이였어."
    yeongwon "그러다 간신히 마음을 추스리고... 원장실로 들어갔지."
    yeongwon "연우랑 한설이 같은 피해자가 더 나오지 않게 하겠다는 일념으로."
    yeongwon "하지만 시간이 갈수록 목표는 흐려졌고, 원장실의 편안한 삶이 익숙해져 가자 내 머릿속에는..."
    yeongwon "너희도, 목표도 버린 내가 과연 이 행복한 생활을 누릴 자격이 있을까 하는 생각뿐이었어."
    yeongwon "그때 고민하는 내 곁에서 원장 선생님이 함께 해 줬지."
    yeongwon "진지하게 내 문제를 들어 주고, 해결책을 내 주고..."
    show yeongwon serious
    with dissolve
    yeongwon "그때 난 생각했어. 원장 선생님은 나쁜 사람이 아니다. 언제라도 나를 도와줄 \n사람이다."
    yeongwon "그래서 모두를 데리고 원장 선생님을 찾아가려는 거야."
    yeongwon "선생님이라면 내 부탁대로 우리 모두를 도와줄 테니까..."
    show hanbyeol shock
    with dissolve
    hanbyeol "... 영원아... 너 완전히... 원장에게 회유당했구나...?"
    hanbyeol "원장실에 너무 오래 있다 보니 이제 원장의 좋은 점밖에 생각나지 않는 거야?"
    hanbyeol "네가 지금 맹목적으로 원장을 따르는 것 같다는 생각이 들지 않니?"

    show yeongwon fury2
    with dissolve
    yeongwon "맹목적으로 원장을 따르는 게 아니야!!"
    show yeongwon serious
    with dissolve
    yeongwon "너희를 구하기 위해 내가 애써 내린 판단이라고..."
    yeongwon "처음 원장 선생님의 제안을 받아들인 것도 그렇고, 모두 너희가 살아 주기를 \n바라는 마음에서 나왔어."
    yeongwon "만약 너희마저 무슨 일이 생긴다면..."
    yeongwon "연우랑 한설이를 볼 면목이 없잖아..."

    show haneul sad
    with dissolve
    haneul "영원아, 이제 그만해."
    haneul "네 마음은 잘 알겠지만 그래도 이건 너무 막무가내잖아..."
    haneul "그러지 말고 우리와 함께 움직이자."
    haneul "모두 함께 밖으로 나가서... 자유롭게 사는 거야."
    "고아원 밖으로 나가서 자유롭게 살 수 있을 리가 없다."
    "정말로 모두가 큰 일에 휘말렸다면, 누군가는 눈에 불을 켜고 우리를 찾으려 \n하겠지."
    "그걸 막기 위해서라도 강한 힘을 가진 어른의 보호를 받을 필요가 있어."
    "...하지만 둘 다 내 말을 들을 생각이 없어 보인다."
    "서로를 설득하기 위한 말이 오고 갈수록 점점 더, 나는 그들에게 이상한 아이로 보여지는 듯했다."
    "내 생각이 아무리 확고하더라도, 그들의 마음을 꺾을 수는 없는 걸까."
    haneul "...영원아. 일단은 여기까지 하자."
    haneul "아무래도 지금 당장 네 마음을 돌리기는 힘든 것 같아."
    haneul "나중에라도 함께 할 생각이 있다면 언제라도 찾아와. 기다리고 있을게..."
    hide haneul
    with dissolve
    "옛날 원장실 때처럼 슬픈 눈을 한 채로, 하늘이는 나를 떠났다."
    "하늘이가 어떤 일을 당할지 생각해 보면, 무슨 수를 써서라도 잡아 놓고 싶었다."
    "하지만 아무리 부르고, 목놓아 울어 봐도 하늘이는 돌아오지 않는다."
    "...그 아이는 더 이상 나를 믿지 않는다."
    hide hanbyeol
    with dissolve
    "결국 나는 자리를 박차고 일어나 원장실로 도망치듯 달려 갔다."
    hide yeongwon
    with dissolve
    "아무것도 지키지 못한 채로."

    scene background principaloffice
    with fade
    show yeongwon sad2
    with dissolve
    yeongwon "왜... 왜 나를 믿지 않아 주는 거야..."
    yeongwon "난 항상 너희들을 위해서 최선의 선택만 하려고 노력하는데..."
    yeongwon "내 말을 안 따라서 큰일이 나면 어떻게 하려고 이러는 거야..."
    yeongwon "평생 죄의식 속에서 살아가야 할 내 기분은 생각해 주지 않는 거야?"
    "원장실 문 앞에서 눈물과 함께 가쁜 숨을 토해 냈다."
    "...아무리 최선의 판단을 내린다 해도, 남들이 따라 주지 않으면 아무것도 할 수 없구나."
    "결심했다. 이제부터는 무슨 수를 쓰더라도 내 판단을 모두가 따르도록 만들 \n것이다."
    "그래야만 모두를 구할 수 있다."
    "난 옳은 판단을 내리고 있으니까."
    "날 따르도록 하려면 남들을 떨어지지 않도록 붙잡아 놔야겠지."
    stop music fadeout 2.0
    "그러려면 지식이든... 권력이든 뭐든... 강한 힘이 필요해."
    "원장 선생님처럼."

label part4:

    scene background school
    with fade
    play music "music/L42.mp3"
    "(10년 후)"
    show teacher
    with dissolve

    teacher "...여기가 염소 고아원인가...?"
    teacher "음... 길 좀 물어볼 사람이.. 아, 저기 있다. 저기요!"
    show teacher:
        moveleft
    with Pause(0.5)
    show keibi at right
    with dissolve

    keibi "예."
    teacher "죄송한데 길 좀 물어봐도 괜찮을까요? 제가 여기 초임이라..."
    keibi "하, 누구한테 미운 털이라도 박혔수? 하필이면 이 고아원에 부임하다니..."
    keibi "차라리 그냥 사표 내고 다른 직업을 찾아보슈."
    keibi "여기 원장이 아주 악랄하다고 온 동네방네 소문이 자자해."
    teacher "네?"
    keibi "말 그대로야. 악.랄. 자기 말에 조금이라도 따르지 않으면 무조건 찍어누르려 \n하는 폭군이지."
    keibi "당신도 여기 있으면 못 볼 꼴 다 당할 거야. 그러니 그냥 사표 내고 물러나."
    teacher "아니... 대체 어떤 사람이길래..."
    keibi "음... 들리는 소문에 따르면..."
    keibi "10년 전에 이 고아원에서 외부 구역에서도 활동할 수 있는 아이가 나타났다지."
    keibi "그래서 정부에서 그 아이를 데려가려 했는데..."
    keibi "고아들이 꼴에 친구랍시고 폭동을 일으켰나 봐."
    teacher "그래서, 어떻게 되었나요...?"
    keibi "그 아이는 정부에서 데려갔고, 고아들은 전부 사살당했다고 들었어."
    keibi "그런데 그 사건이 일어나기 며칠 전. 웬 여자애 하나가 전 원장 손을 잡은 채 \n갑자기 정부군 앞에 나타났다지."
    keibi "그 여자애 출신에 대해선 말이 많아. 사태에 휘말린 민간인이라고도 하고, \n고아들 중 하나라고도 하고..."
    keibi "그 뒤 염소 고아원이 다시 운영을 시작하자 젊은 원장이 새로 부임했는데, \n사람들 말로는 그때 그 여자애라더군."
    keibi "염소 고아원 원장... 정부에서 교육받을 때도 말이 많았어. 아주 미친년이라고..."
    keibi "암튼, 난 충분히 경고했수. 들어가도 본인 손해요!"
    stop music fadeout 1.0

    scene background classday
    with fade
    "(염소 고아원, 수업 시간)"
    play music "music/L31.mp3"
    show yeongwon adult
    with dissolve
    yeongwon "...선견지명을 가진 양심적인 사람들의 목소리를 무시한 대다수 탐욕에 물든 인간들에 의해,"
    yeongwon "오존층이 파괴되어 지구 대부분에서 사람들이 살 수 없던 시절이 있었어요."
    yeongwon "그때는 선각자들이 개발한 기술로 만들어진 안전구역 안에서 사람들이 살았죠."
    yeongwon "그러던 어느 날, 안전구역 밖에서도 살아갈 수 있는 사람이 나타났어요."
    yeongwon "바로 이곳, 염소 고아원에서요."
    play sound "effect/schoolbell.ogg"
    "수업종이 울렸다."
    yeongwon "그러면 오늘은 여기까지. 모두 수고했어요."
    stop sound fadeout 1.0
    hide yeongwon adult
    with dissolve

    scene background schoolhallway
    with dissolve
    play music "music/RainSound.mp3"
    "하늘이에 대한 수업을 할 때마다, 가슴 한편이 아파 온다."
    "그가 내 제안을 거부한 그날, 하늘이는 자신의 계획에 따라 탈출을 감행했지만,"
    "결국 한별이를 포함한 모든 친구들을 잃고 자신도 정부군에게 잡혀 가고 말았다."
    "그 뒤로 나는 다시는 하늘이를 보지 못했다."
    "허망하게 친구들을 모두 잃은 뒤, 나는 거의 제정신이 아니었다."
    "소중한 하늘이를 잃은 슬픔, 아무도 지키지 못하고 혼자만 살아남은 나 자신에 \n대한 원망이 나를 짓눌렀다."
    scene background oldschool
    with dissolve
    "그럼에도 버틸 수 있었던 건,"
    "절대 흔들리지 않을 확고한 생각이 내가 어디로 가야 할지를 알려 주고 있었기 때문이다."
    "그후로 나는 원장 선생님을 따라 정부 기관에서 교육을 받았다."
    "그리고 언젠가는 염소 고아원의 원장이 될 수 있도록 누구보다 열심히 공부했다."
    "힘이 있어야 모두를 구할 수 있으니까."
    scene background oldhallway
    with dissolve
    "사람들 입장에서는 조금 억압받겠지만, 이보다 나은 방법은 없다."
    "그들이 나를 따르지 않는다면 난 또 누군가를 잃는 고통에 시달리게 될 테니까."
    "...더 이상 그런 고통에, 죄책감에 시달리고 싶지는 않다."
    "무슨 수를 써서라도 내 판단에 따르도록 만들어야지."
    "모두가 나를 미쳤다고 욕했다. 하지만 그럴 수밖에 없는걸."
    "내 소중한 친구들... 연우, 한설이, 한별이... 그리고 사랑하는 하늘이까지..."
    "그들과 같은 피해자가 더는 나오지 않게 하는 것이 내 유일한 속죄의 길이니까."
    scene ecg ketsuni 2
    with dissolve
    "(어딘가에서 발걸음을 멈춘다. 이제는 비어 버린 옛 비밀 기지가 보인다.)"
    scene ecg ketsuni 3
    with dissolve
    stop music fadeout 1.0
    pause(.5)
    "... 날 용서해 줘, 모두들..."
    scene end2
    with fade
    with Pause(3)
    $ renpy.movie_cutscene("end2credit.webm")
    return
