init 20:
    image ecg ketsuichi 1 = "ecg/ketsuichi1.png"
    image ecg ketsuichi 2 = "ecg/ketsuichi2.png"
    image ecg ketsuichi 3 = "ecg/ketsuichi3.png"
    image ecg ketsuichi 4 = "ecg/ketsuichi4.png"
    image ecg ketsuichi 5 = "ecg/ketsuichi5.png"
    image ecg ketsuichi 6 = "ecg/ketsuichi6.png"
    image ecg ketsuichi 7 = "ecg/ketsuichi7.png"
    image ecg end1 = "ecg/end1.png"

#시작
label scene411:
#1:구교사 교실
    scene background black
    with fade
    play sound "effect/gunshot.ogg"
    "한 발의 총소리가 빈 공간에 울려퍼졌다."
    stop sound
    show yeongwon shock
    with dissolve
    yeongwon "꺄악!!!"
    scene background oldclass
    with fade
    play music "music/L45.mp3"
    "방금 전까지만 해도 나와 이야기하고 있던 원장이, 저항할 새도 없이 힘없이 앞으로 쓰러졌다."
    "원장의 몸에서 흘러나온 피가 바닥을 서서히 물들여갔다."
    "무슨 일이 일어난 거지....?"
    "설마 이건... 누군가가 원장을 죽..."
    show overwatch2 idle2
    with dissolve
    overwatch2 "얘들아! 괜찮니?!"
    hide overwatch2
    with dissolve
    "어둠 속에서 몸을 드러낸 것은 다름아닌 1반 선생님이었다."
    show yeongwon shock at left
    with dissolve
    yeongwon "서... 선생님?"
    show haneul shock at right
    with dissolve
    haneul "읏..."
    show hanbyeol shock
    with dissolve
    hanbyeol "어떻게 된 거야..."
    hide hanbyeol
    hide yeongwon
    hide haneul
    with dissolve
    show overwatch2 idle2
    with dissolve
    teacher  "설명할 시간이 없어. 따라오렴!"
    hide overwatch2
    with dissolve
    "심신을 추스르기도 전에 1반 선생... 아니, 이젠 누군지 감도 안 잡히는 이 남자가 내 손목을 잡아끌었다."
    "그도 모든 사실을 알고 있나?"
    "혼란스럽긴 했지만 우리 말고도 고아원의 정체를 아는 사람이 또 있다는 것, 그것이 1반 선생님이었다는 것에 살짝 안도감이 느껴졌다."
    "나는 고개를 끄덕이며 선생님을 따라갔다. 어차피 다른 선택지도 없었다."
    show haneul shock
    with dissolve
    haneul "잠깐만요."
    haneul "총을... 총을 버려주세요."
    haneul "그러면 믿고 따라갈게요. 괜찮죠...?"
    hide haneul
    with dissolve
    "그래. 혹시 모르니까... 이 상황에서도 침착하게 생각할 수 있다니 대단하네, 하늘이."
    "......"
    play sound "effect/drop.ogg"
    "이내 권총 한 자루가 둔탁한 소리를 내며 바닥에 떨어졌다."
    show overwatch2 idle2
    with dissolve
    stop music fadeout 3.0
    overwatch2 "아까도 말했지만 시간이 별로 없어. 내가 안내할 테니 따라오렴."
    hide overwatch2
    with dissolve
#
#2:실험실
    scene background lab
    with fade
    play music "music/L44.mp3"
    "선생님을 따라 도달한 곳은 최상층에 있는 실험실이었다. 이전에도 한번 와본 적 있는 장소다."
    show overwatch2 idle2
    with dissolve
    teacher "실험실에 대해서는 너희도 대강 알고 있겠지. 자, 이쪽으로 들어오렴."
    hide overwatch2
    with dissolve
    "선생님은 실험실 벽으로 다가가 무언가를 누르려는 듯 손을 갖다 댔다."
    play sound "effect/dooropen.ogg"
    "그 순간 둔탁한 소리를 내며 벽이 문처럼 열렸다."
    show yeongwon shock
    with dissolve
    yeongwon "......!"
    scene background hiddenlab
    with fade
    "안쪽에는 수많은 실험도구들과 안이 들여다보이는 여러 개의 통이 있었고, 그 통 안에는 한때 인간의 일부였던 것으로 보이는 것이 들어 있었다."
    show yeongwon shock
    with dissolve
    yeongwon "우...우욱...!"
    "순간 헛구역질이 났다. 한별이와 하늘이 또한 당황한 표정이었고, 한별이는 입술을 깨물고 떨고 있었다."
    show yeongwon shock:
        moveright
    with Pause(0.5)
    show haneul shock at left
    with dissolve
    haneul "원장... 저런 짓까지...."
    show overwatch2 idle with dissolve
    overwatch2 "흠 뭐, 큰 일을 위해서라면 희생양이 필요한 법이지."
    show overwatch2 devil with dissolve
    overwatch2 "다행이야, 그래도 우리 하늘이는 잘 버텨 줘서."
    yeongwon "...뭐라고요?"

    show overwatch2 idle
    with dissolve
    overwatch2 "아아, 너희는 아마 날 1반의 선생님으로 알고 있겠지?"
    hide overwatch2
    show overwatch devil
    with dissolve
    overwatch "어차피 곧 죽게 되는 김에 다 알려 주지. 나는 사실 세계정부에서 실험을 감독하라고 파견한 감시자다."
    "건조한 톤으로 친절한 설명이 이어졌다."

    show overwatch idle
    with dissolve
    overwatch "그래서 나 같은 감시자를 파견하지. 원장 같은 반동분자가 허튼수작 못 하도록."

    show overwatch devil
    with dissolve
    overwatch "선생 역할을 하면서 너희랑 정도 들어버렸는데 여기서 끝이라니 좀 허무하네?"
    "이게 다 무슨 말이지...? 선생님이... 정부의 감시자....?"
    "선생님은 항상 학생들에게 친근하고 상냥하게 대해 주어서 믿고 따르는 아이들이 많았다."
    "그 모든 게 다 연극이었다니..."
    "원장을 죽일 때부터 평소 선생님의 모습과는 달라보이긴 했지만, 그래도 우리를 도와주려고 그런 것이라고 생각했다."
    "한치의 의심도 하지 않았다."
    "그런데... 대체 왜 원장을 죽인 거지...?"
    yeongwon "그럼 원장은 왜..."
    show overwatch fury
    with dissolve
    overwatch "그 여자는 이제 쓸모가 없게 되어서 버렸어. 애들한테 업무기밀이나 술술 불고 말이지."
    overwatch "그래도 시키는 대로 말은 나름 잘 들었는데 참 아쉽게 됐어."

    hide yeongwon
    hide haneul
    with dissolve
    show overwatch fury:
        moveright
    with Pause(0.5)
    show hanbyeol shock at left
    with dissolve
    hanbyeol "그... 그럼 이 모든 걸 다 네가..."

    show overwatch devil
    with dissolve
    overwatch "음? 너는 한설이의 언니였지? 그 애 참 귀엽고 싹싹했는데."

    show hanbyeol fury
    with dissolve
    hanbyeol "이 개새끼야아아아!!!!!!!!!!!"
    "소리를 지르며 한별이가 선생... 아니 감시자에게 달려들었다."

    show hanbyeol with hpunch
    play sound "effect/punch.ogg"
    with dissolve
    hanbyeol "꺄앗...!"

    hide overwatch
    hide hanbyeol
    with dissolve
    "감시자가 한별이를 발로 차는 소리가 들렸다."
    "한별이는 벽에 머리를 박은 후 바닥에 쓰러졌다. 머리에서 선홍색의 피가 흘러내리는 것이 보였다."
    show yeongwon shock speaking at right
    show haneul shock speaking at left
    with dissolve
    "영원, 하늘" "한별아!!!!!!"
    show yeongwon shock
    show haneul shock
    with dissolve
    "나와 하늘이가 한별이에게 달려가서 보니 한별이는 기절해 있었다."
    "죽은 건 아니겠지... 설마... 설마. 저 감시자는 나와 한별이를 죽일 작정인 것 같았다."
    "여기서 끝인 건가. 그럼 하늘이는... 어떻게 되지...? 나는 하늘이를 지킬 수 없는데..."
    show haneul serious
    with dissolve
    haneul "내가... 내가 어떻게든 해 볼게."
    hide haneul
    with dissolve
    "말 없이 한별이를 바라보던 하늘이가 감시자 쪽으로 몸을 틀었다. 감시자와 자신의 몸을 대가로 거래를 할 생각인 게 분명했다. 나는 그런 하늘이를 팔로 막아섰다."
    show yeongwon serious
    with dissolve
    yeongwon "안 돼!!! 하늘이를 데려갈 수는 없어."
    "안 통할 얘기란 걸 알면서도 말이 맘대로 튀어나왔다."
    hide yeongwon
    with dissolve
    play sound "effect/punch.ogg"
    with vpunch
    with hpunch
    "감시자에게 얼굴을 맞아 입안에 피가 고인 것이 느껴졌다."
    "뒤이어 감시자의 발이 나를 짓눌렀다. 빠져나갈 수 없었다."

    show yeongwon shock at left
    show overwatch fury at right
    with dissolve
    yeongwon "크윽..."

    show haneul serious
    with dissolve
    haneul "그만... 이젠 그만해... 나를 데려가!!!"

    show haneul sad
    with dissolve
    haneul "내가 따라가서 원하는 게 뭐든 다 해줄 테니 한별이와 영원이는 제발 놔줘... 입막음도 철저히 할게."
    "하늘이의 목소리였다. 그건 안 돼. 이런 식으로 나만 살아서 무슨 의미가 있을까."

    show yeongwon sad
    with dissolve
    yeongwon "하늘아...!"
    overwatch "대체 내가 왜 그래야 하지? 어차피 너는 데려갈 텐데 얼토당토가 없는 거래로군."
    overwatch "너가 순순히 따라줘야 친구들이 편히 죽을 수는 있겠지."
    "감시자는 나를 누르고 있던 발을 옮겨 내 목을 짓눌렀다."

    scene background black
    with Dissolve(1.0)
    "숨을 쉴 수가 없었다. 눈앞이 조금씩 흐려져 갔다."
    show yeongwon shock at left
    show overwatch fury at right
    with dissolve
    yeongwon "......윽..."
    stop music fadeout 1.0
    overwatch "......"

    scene background hiddenlab
    with fade
    play music "music/L14.mp3"
    show haneul fury
    with dissolve
    haneul "으아아아!!"
    "그때 하늘이가 감시자를 향해 몸을 날렸다. 하늘이가 저렇게 소리를 지르는 것은 처음이었다. "
    hide haneul
    with dissolve
    "감시자는 조금 당황했는지 움찔하며 넘어질 뻔하였고, 내 목을 누르던 무게가 가벼워진 게 느껴졌다."
    "막혀 있던 숨이 터져 나왔다."

    show yeongwon shock at left
    show overwatch idle at right
    with dissolve
    yeongwon "허억... 허억..."
    overwatch "귀찮게도 하는군. 멀쩡한 상태로 데려가려 했더니만, 너 먼저 기절해 줘야겠다."

    hide overwatch
    hide yeongwon
    with dissolve
    "감시자가 하늘이의 멱살을 잡고 들어올렸다."
    "이대로라면 우린 모두 끝이다. 무슨 수를 써서라도 막아야만 한다는 생각이 들었다."
    "엎드린 채로 감시자의 다리를 깨물고, 때리고 별 짓을 다 했다."
    "그런데 갑자기 감시자의 얼굴 위로 액체같은 것이 쏟아져 내렸다."

    scene ecg ketsuichi 1
    with fade
    overwatch "으아아아아아아아아아악!!!!!"
    "감시자는 소리를 지르며 하늘이의 멱살을 쥐고있던 손을 놓았다."

    scene ecg ketsuichi 2
    with dissolve
    "일어나 보니 얼굴이 녹아내린 감시자가 고통에 몸부림치고 있었다. 눈 뜨고 보기 힘들 정도로 처참한 광경이었다."
    hanbyeol "하아... 하아..."
    "한별이었다."
    "한별이가 화학약품이 담겨 있었던 통을 손에 쥔 채 주저 앉아 있었다."
    "한별이는 제대로 움직일 수도 없을 정도로 다치고 지쳐 보였지만, 그 얼굴에는 해냈다는 표정만이 감돌고 있었다."
    "그리고 그런 한별이 앞에 있는 감시자는 얼굴 군데군데 뼈가 드러나 원래 얼굴조차 알 수 없게 되어 있었다."
    "참혹하게 죽어가는 그를 바라보니 예전에 아이들과 웃으면서 이야기하고 놀았던 광경이 머릿속에 떠올랐다."
    "그랬던 그가 정부의 감시자라는 정체를 드러내고, 나와 한별이를 죽이려고 했다. 단 몇 분 만에 일어난 일이었다."
    "감시자를 바라보니 눈만은 아직도 생생하게 우리를 노려보고 있었다."
    overwatch "너희들은 탈출할 수 없어... 이곳을... 바꿀 수는 없다..."
    overwatch "내가 죽으면 곧...... 정부에서 알아챌 것이다...... 이 고아원의... 모든 안전구역은... 정부의 손에 있으니까..."
    stop music fadeout 2.0
    "한별, 영원, 하늘" "......"
    scene background black
    with fade
    play sound "effect/siren.ogg"
    "고아원 전체에 사이렌 소리가 울렸다."
    stop sound fadeout 2.0

#3 실험실
    scene background lab
    with fade
    play music "music/L20.mp3"
    show haneul idle at left
    show hanbyeol idle2 at right
    with dissolve
    haneul "조금만 가만히 있어봐."
    hanbyeol "알았어. 앗...!"
    "하늘이가 다친 나와 한별이를 위해 응급처치를 해주겠다고 나섰다. 의외로 실력이 수준급이었다. 양호선생님보다 더 잘 할지도 모르겠다는 생각이 들었다."
    "하늘이에게 이런 재능이 있다는 것을 처음 알았다."

    show yeongwon idle2
    with dissolve
    yeongwon "하늘아, 이렇게 하는 건 어디서 배운 거야?"
    haneul "특별반에서 수업시간에 배웠는데, 관심이 가서 따로 열심히 공부했거든."
    "하긴 나도 어렸을 때 응급처치 교육을 잠깐 받았던 것 같다."
    "나는 대강 듣고 다 까먹었는데, 하늘이는 기억하고 있는 모양이다. 학교에서 가르치는 데는 다 이유가 있었다."
    haneul "영원이는 이 정도로 된 것 같아."
    hide haneul
    with dissolve
    show yeongwon idle2:
        moveleft
    "나는 조금 멍이 들고 긁힌 정도이지만 한별이는...이곳저곳 많이 다친 것 같다."
    "한별이가 어떻게든 같이 안전하게 탈출할 수 있기를 바랄 뿐이다."
    "순간 방금 전에 감시자에게 머뭇거림 없이 달려들던 한별이의 모습이 떠오르면서, 여태까지의 우유부단하던 나의 모습이 또다시 한심하게 느껴졌다."
    "난 사실 하늘이가 안전했으면 좋겠다는 것을 핑계삼아 나의 안위를 걱정했던 게 아닐까."

    show hanbyeol sad2
    with dissolve
    hanbyeol "영원아... 나 이제 괜찮아."
    "내 생각을 읽기라도 하듯 한별이가 내게 말했다."
    "순간 눈물이 고였다."
    "동생이라는 버팀목이 사라진 상태에서 한별이는 홀로 고된 싸움을 해왔을 것이다."
    "나는 한별이의 손을 꼭 잡았다."

    show yeongwon serious
    with dissolve
    yeongwon "우리 꼭 다 같이 탈출하자!"

    show hanbyeol happy
    with dissolve
    hanbyeol "당연하지. 나가서 너랑 하늘이랑 대놓고 꽁냥대는 거, 구경할 거 생각하니 즐겁다. "

    show yeongwon blush
    with dissolve
    yeongwon "에... 에엥?!"
    "너무 훅 들어오는 거 아니야? 얼굴이 순간 붉어졌다."
    "하늘이는 고개를 숙이고 쿡쿡거리며 웃고 있었다. 이게 그렇게 비웃을 정도인가?!"

    show haneul idle
    with dissolve
    haneul "이 정도면 된 것 같아. 일어날 수 있겠어?"

    show hanbyeol idle
    with dissolve
    hanbyeol "대충 움직일 수 있을 것 같아. 고마워."
    haneul "아직은 부축 없이 걷기 힘들 거야. 앞으로는 조심해야 돼, 한별아."
    hide hanbyeol
    with dissolve
    show haneul:
        moveright
    pause(0.5)
    with dissolve
    play sound "effect/siren.ogg"
    "사이렌은 아직도 울리고 있었다."

    show yeongwon serious
    with dissolve
    yeongwon "빨리 움직여야 할 것 같아. 이제 어디로 가야 하지...?"

    show haneul serious
    with dissolve
    haneul "일단 아이들이 있는 기숙사동 쪽으로 가자. 아마 다들 당황해서 나와 있을 거야."

    show yeongwon idle
    with dissolve
    yeongwon "한별이는 내가 부축할게! 한별아, 나한테 업혀!"

    hide yeongwon
    hide haneul
    with dissolve
    scene background black
    with fade
    "감시자는 사라졌다."
    "그러나 감시자가 말했듯이... 곧 정부에서 사람들이 고아원에 도착할 것이다."
    "지쳤지만 아직 끝이 난 것이 아니다. 하늘이, 한설이, 연우, 그리고 특별반 친구들 모두를 괴롭힌 실험실을 뒤로 하고
우리는 천천히 발걸음을 옮기기 시작했다."
    stop sound fadeout 1.0
    stop music fadeout 1.0
#
#4 고아원 정문앞 외부(운동자 쪽)
    scene background school
    with fade
    play music "music/L51.mp3"
    "'염소 고아원에 있는 학생들은 지금 모두 정문 앞으로 집합해 주시길 바랍니다. 염소 고아원에 있는 학생들은 지금 모두 정문 앞으로 집합해 주시길 바랍니다.'"
    show fstudent at left
    show mstudent at right
    with dissolve
    fstudent "무슨 일이지?"
    mstudent "오늘 휴일인데... 아 귀찮아~"
    fstudent "어? 저기 오는 사람 영원이랑 한별이 아니야?"
    fstudent "...뭐지...? 많이 다쳐 보이는데...?"
    hide fstudent
    hide mstudent
    with dissolve
    scene background black
    with fade
    "'집합 방송 때문에 모인 아이들에게 진실을 알리자.'라는 급조된 계획."
    "정부에서 모든 학생들을 집합시킨 이유는 변절자를 찾아내려고 하는 것이겠지."
    "예상대로 탈출하지 못하게 고아원 밖으로 출입하는 문은 잠긴 것 같았다."
    "사실 비밀 탈출로를 통해 우리끼리만 도망칠 수도 있었다."
    "그러나 그랬더라면, 인체실험은 계속되고, 아무것도 달라진 것이 없을 것이다."
    "아무 죄 없는 생명들이 하나둘씩 계속 죽어나갈 것이다."
    scene background school
    with fade
    "학생들에게는 진실을 알 권리가 있다."
    show mstudent speaking at left
    show fstudent speaking at right
    with dissolve
    "여학생, 남학생" "다들 괜찮아?!! 대체 무슨 일이야...!!!"
    show mstudent
    show fstudent
    with dissolve
    "여러 명의 학생들이 나와 하늘이, 한별이에게로 몰려들었다."

    hide fstudent
    hide mstudent
    with dissolve
    show yeongwon serious
    with dissolve
    yeongwon "잠시만, 잠시만 모두 들어 주세요!"
    "나는 원장의 정체, 1반 선생님의 정체를 포함한 모든 사실을 숨가쁘게 이야기했다."
    hide yeongwon
    with dissolve
    "이야기를 들은 아이들의 얼굴이 파랗게 질려 있었다."
    show fstudent at left
    with dissolve
    fstudent "...말도 안 돼......"
    show mstudent at right
    with dissolve
    mstudent "우, 우리 다 죽는 거 아니야??"
    "믿을 수 없다는 눈치인 아이들, 동생이 특별반에 들어간 이후부터 느낌이 싸했다는 아이들, 웅성거림은 점점 더 커져 갔다.
훌쩍훌쩍 울기 시작하는 아이도 있었다."
    hide mstudent
    hide fstudent
    with dissolve
    show yeongwon serious
    with dissolve
    yeongwon "그래서...!"
    yeongwon "곧 국가에서 사람을 보낼 거야. 우리는 그전에 탈출해야 해."
    hide yeongwon
    with dissolve
    "사실 다 함께 탈출이 가능할지 장담할 수는 없었다."
    "가야만 한다고, 목소리 높여 말했지만 마음 한켠에서는 불안함이 계속 있었다."
    "언제 국가에서 보낸 사람들이 우리를 쫓아올지 모르고 확실한 계획이 없었기에... 그저 최선을 다해 보자는 것이었다."
    show fstudent at left
    with dissolve
    fstudent "그런데 무슨 수로 탈출을 해?"
    show haneul serious at right
    with dissolve
    haneul "다들 학교에 있는 폐건물 알고 있을 거야. 그쪽에..."
    stop music fadeout 1.0
    fstudent "잠깐 저기... 무엇인가가 오고 있어......"
    hide fstudent
    hide haneul
    with dissolve
    play music "music/L45.mp3"
    "얘기를 듣고 있던 한 명의 학생이 손으로 고아원 밖을 멀리 가리켰다."
    "멀리서 다가오는 것은 온통 푸른 빛이었다."
    "바로 머리부터 발끝까지 최첨단으로 무장한... 정부 친위대다."
    scene background black
    with fade
    "우리가 너무 늦었구나."
    "그 한 덩어리의 무리는 믿을 수 없는 속도로 고아원 정문 앞에 도착했다."
    "친위대" "모두 움직임을 멈춰라."
    "무미건조하고 기계적인 목소리가 공간을 울렸다."
    "친위대" "고아원은 갈 곳 없는 너희들을 환경 파괴로부터 지켜줄 수 있는 유일한 기관이다."
    "친위대" "고아원의 외부는 온통 죽음의 땅인데 대체 무엇을 할 수 있다고 생각하지?"
    "친위대" "조용히 원래 위치로 돌아간다면 여태까지의 일은 모두 눈감아 주겠다."
    "친위대" "그러나 만약 여기서 도망친다면, 그 앞엔 죽음뿐이다."
    "협박하는 건가? 인체실험에 대해서는 입을 싹 닫고 있다니 어이가 없었다."
    "지켜주기는커녕 멀쩡한 애들 가지고 이용해 먹기나 했으면서, 하, 니들 때문에 죽은 내 친구만 몇 명인데."
    "그리고 고아원 밖으로 한 발자국만 나가면 죽는다는 것도 모두 거짓 선동이다. 완충구역은..."
    stop music fadeout 1.0
    ""
    "...?"
    scene ecg ketsuichi 3
    with fade
    hanbyeol "누가...누굴 눈감아..."
    "한별이?!"
    "분명히 한별이의 목소리였다."
    "한별이는 비틀거리는 걸음으로 한 발자국씩 친위대의 앞으로 걸어나가고 있었다."
    "한별이의 얼굴에는 분노로 일그러진 웃음밖에 보이지 않았다."
    hanbyeol "더러운 것들. 애초에 너희는 여기 학생들을 생명으로 보고 있지 않아."
    hanbyeol "그저 필요한 데 쓰다가 버리는 소모품에 불과하겠지."
    hanbyeol "갈 곳 없는 애들인 거 아니까, 죽어도 누구 하나 몰라줄 고아니까, 데려다가 이것저것 실험하고 했겠지."
    hanbyeol "너희에게 이용당하다 죽느니 차라리 피폭당해 죽고 말겠어!!!"
    scene ecg ketsuichi 4
    with fade
    "친위대" "말을 잘 듣는다면 명령을 철회할까 했는데... 저항하는 자 앞엔 죽음뿐이다."
    "모든 총구가 일제히 한별이를 향해 기울었다."
    "잠깐... 이건..."
    yeongwon "안 돼!!!!!"
    play sound "effect/gunshot.ogg"
    scene ecg ketsuichi 5
    with vpunch
    "하늘에 총성 소리가 울렸다."
    stop sound fadeout 1.0
    scene ecg ketsuichi 6
    play music "music/L50.mp3"
    hanbyeol "꺄아아아아아아악!!!!"
    "가녀린 한별이의 몸이 바닥에 힘없이 떨어졌다."
    "쓰러져 있는 한별이의 모습이 흔들리며 뿌옇게 흐려졌다."
    "안 돼... 안 돼... 한별이마저..."
    scene background school
    with fade
    "뛰쳐나가려는 나를 갑자기 하늘이가 팔을 뻗어 강하게 막아섰다."
    "하늘이의 팔은 잘게 떨리고 있었다."
    "왜 이러는 거지...? 한별이에게 가야 하는데... 아무리 하늘이라도 이해가 안 갔다."
    "하늘이를 뿌리치고 한별이에게 달려가려는 순간 하늘이가 조용히 입을 열었다."

    show haneul serious at right
    show yeongwon shock at left
    with dissolve
    haneul "영원아... 움직이지 마. 뭔가 이상해."
    yeongwon "...?"
    hide yeongwon
    hide haneul
    with dissolve
    "주위는 공포에 지배당하고 있었다."
    "몇몇의 아이들은 항복했다는 듯이 친위대의 앞에서 무릎을 꿇고 있었다."
    stop music fadeout 1.0
    "그런데 갑자기, 친위대 인원들이 전부 총을 들었다."

    scene background black
    with fade
    with vpunch
    play sound "effect/gunshots.ogg"
    "총알이 빗발처럼 날아왔다."
    "도망쳐. 도망쳐. 도망쳐. 도망쳐. 도망쳐. 도망쳐야 해."
    "하늘이와 함께 꼭 손을 붙잡고 미친 듯이 뛰었다."
    "뒤조차 돌아볼 수 없었다."
    "도망치던 와중에 우리가 들을 수 있었던 것은 총소리와 친구들의 비명소리밖에 없었다."
    stop sound fadeout 1.0

#5 아지트
    scene background dayhideout
    with fade
    play music "music/L42.mp3"
    show yeongwon serious at left
    show haneul serious at right
    with dissolve
    yeongwon "하아... 하아..."
    "미친 듯이 달려 아지트까지 도착했다. 이제는 둘밖에 남아있지 않은 우리들의 아지트."
    "한별이... 고아원의 아이들... 같이 탈출하자 해놓고, 나는 아무것도 할 수 있는 것이 없었다."
    "빗발치는 총소리만이 머릿속을 맴돌았다."
    hide haneul
    show haneul serious at right
    with dissolve
    haneul "영원아. 지혈을 해야 할 것 같아."
    "하늘이의 목소리였다."
    "아, 그러고 보니 아까 도망치다가 총알에 팔을 살짝 스쳤었다. 자각하자마자 팔이 아려오기 시작했다."
    "피가 팔을 따라 손까지 흘러내려 바닥에 떨어지고 있었다."
    "하늘이는 자신의 와이셔츠를 찢어 내가 다친 부분에 묶어주었다."
    show yeongwon idle
    with dissolve
    yeongwon "아...!"
    "고개를 들어 하늘이를 쳐다보니 하늘이 또한 많이 지쳐 있는 표정이었다. 얼굴이 더 하얗게 질려 있었다."
    "자기도 아프면서..."
    haneul "영원아 우리... 탈출할 수 있겠지?"

    show yeongwon happy
    yeongwon "당연하지! 조금만 더 가면 완충구역이야!"
    "하늘이에게는 억지로 밝은 모습을 보이려 했다."
    "구교사 근처에 위치해 있는 아지트는 더 깊숙한 곳으로 가면 완충구역과 연결되어 있다."
    "일단 그쪽으로 빠져나가 멀리 도망치면 정부의 감시는 피할 수 있게 될 것이다."
    "이후의 일은 나중에 생각해야지. 일단은....."
    "가까운 곳에서 친위대의 걸음 소리가 들렸다."

    show yeongwon serious
    with dissolve
    yeongwon "하늘아, 나가자."
    haneul "응..."
    hide yeongwon
    hide haneul
    with dissolve
    scene background black
    with dissolve
    stop music fadeout 1.0
    "완충구역으로 떠날 시간이었다."

#6 완층구역
    play sound "effect/gunshot.ogg"
    "달려가는 내내, 이따금씩 총성이 들렸다."
    scene background wasteland
    with fade
    play music "music/L50.mp3"
    "우리 말고 도망친 애들이 더 있는 것 같았다."
    with vpunch
    "으아악!!!"
    "그리곤 총성마다, 그 뒤로 작지만 분명한 비명이 들렸다. 그 소리에 자꾸만 눈앞이 흐려져서 두 눈을 질끈 감았다."
    "내가 좋아했던, 혹은 친하지 않았더라도 얼굴만큼은 익숙했을 누군가가 하나둘 사라져갔다."
    show yeongwon shock
    with dissolve
    yeongwon "우욱..."
    hide yeongwon
    with dissolve
    "아까의 피바람이 다시 눈앞에 일렁였다."
    "뱃속의 장기가 묶인 것처럼 욱신거렸다. 관절 마디마디가 쓰라려왔다. 목까지 차오른 울음에 입술을 깨물며 버텼다."
    "참아야 돼. 지금 나만 힘든 게 아니야. 울어서 되는 건 없어. 계속 가야 돼!"
    "친위대" "거기 서!!"
    show yeongwon shock at left
    with dissolve
    yeongwon "으악...?"
    show haneul shock at right
    with dissolve
    haneul "...머... 멀리서 들린 것 같아."
    hide haneul
    hide yeongwon
    with dissolve
    "소스라친 나를 하늘이가 진정시켰다. 다행히 친위대는 생각보다 바짝 따라붙진 못 한 듯했다."
    "간간이 들리는 고함에 계속 경기하며, 우리는 걸레짝이 된 몸을 재촉했다."
    "그래도 갈수록 구도시의 흔적과 폐건물들이 띄엄띄엄 나오고 있어서, 안전구역을 꽤 벗어났음을 알 수 있었다."
    "둘 다 당장 쓰러져도 이상할 게 없는 상태라, 이쯤에서 사기를 북돋울 필요가 있다고 생각했다."
    show yeongwon idle at left
    with dissolve
    yeongwon "하늘아, 우리 이제 조금만 힘내자! 진짜... 많이 왔으니까...! 곧 탈출......!"
    "그 이상 말을 이을 수 없었다. 하늘이 낯빛이 꼭 시체 같았다."
    "씩씩한 척하려 했는데, 누가 들어도 우스꽝스러울 염소 울음소리가 나왔다."
    "그 목소리에 내가 울컥해서 한참 만에 열었던 입술을 다시 깨물었다."
    "이런 미친 상황에 희망적인 말을 짜내는 스스로가 너무 비참한데, 이마저도 없으면 걸음 뗄 의욕조차 잃을 것 같았다."

    show haneul serious at right
    with dissolve
    haneul "......"
    "하늘이는 아무 말이 없었다. 나는 눈물이 앞을 가렸다."
    "참고 또 참았지만 이제 걷잡을 수 없었다. 몸을 가눌 힘도 의지도 남아있지 않았다. 서로를 부축하던 팔에 힘은 점점 빠져갔다."

    show yeongwon sad
    with dissolve
    stop music fadeout 1.0
    yeongwon "하...늘아... 왜 대답이... 흑..."
    show haneul shock
    show yeongwon shock
    with dissolve
    play sound "effect/fall_ketsu1.ogg"
    "빠캉-!!"
    scene background black
    with fade
    "영원, 하늘" "으악!!!"
    "그렇게, 우리는 삭아빠진 맨홀 아래로 떨어졌다."
#7 보호소 내부
    scene background shelter
    with fade
    play music "music/L20.mp3"
    show yeongwon idle
    with dissolve
    yeongwon "이곳은...?"
    hide yeongwon
    with dissolve
    "정신을 차리니, 나는 이불을 덮고 어딘가에 누워 있었다."
    "깨끗하게 정돈된 방이 낯설었다."
    "분명 나는... 친위대로부터 도망치고 있었지.. 하룻밤 사이에 너무 많은 일이 일어났었다. 다른 사람들은...염소 고아원은 어떻게 됐으려나."
    "머리가 지끈 아파왔다. 완충구역에서 넘어져 기절한 이후로 이후로 아무 기억이 없다."
    "몸의 상처에는 정성스럽게 붕대가 감겨져 있었다. 누군가가 치료를 해 준 모양이었다."
    show yeongwon idle
    with dissolve
    yeongwon "으으음... 그런데 대체 누가..."
    show yeongwon shock
    with dissolve
    yeongwon "으헛!"
    "깜짝이야. 하늘이가 나와 살짝 떨어진 곳에 이불을 덮고 곤히 잠들어 있었다."
    "일단 이 방에는 둘만 있는 것이 분명하다. 꿈이 아니라면 이미 어디 잡혀간 것이어도 둘 다 목숨은 붙어있어서 다행이라고 해야 하나."
    "일단 일어나 상황을 탐색해보는 게 좋겠다고 결정을 내렸다."
    "좀 뻐근하긴 하지만 팔다리는 잘 움직인다. 걷는 데는 문제가 없겠군."
    "그때, 방문이 스르르 열리며 중년의 남자가 들어왔다."
    "보호소 남자" "오. 일어났니? 아직은 좀 더 휴식을 취하는 게 좋을 거야."
    show yeongwon idle
    with dissolve
    yeongwon "아... 네? 근데 누구...세요? 여긴 어디죠?"
    "보호소 남자" "여긴 완충구역에서 갈 곳 없는 사람들을 보호하는 보호소란다. 나는 여기서 가끔 오는 사람들을 치료하거나 보호하는 일을 맡고 있지."
    "보호소 남자" "고아원에서 일이 터진 것 같다길래, 탐색을 하다가 너희가 기절해 있는 걸 발견해서 데려왔어. 그때로부턴 이틀이 지났다."
    yeongwon "아아, 감사합니다..."
    "보호소 남자" "지금 있는 곳은 너희들이 있던 고아원에서는 꽤 먼 곳에 있을 거다."
    "보호소 남자" "국가의 감시를 피하기 위해 안전구역에서는 멀리 떨어져 있거든."
    "보호소 남자" "그래도 이 안에 있는 동안은 안전하니 환경오염이나 정부의 추격에 대해서는 크게 걱정하지 않아도 된단다."
    yeongwon "완충구역에 이런 곳이 있는지 전혀 몰랐어요. 아무도 없는 줄 알았는데."
    "보호소 남자" "생각보다 완충구역으로 오는 사람이 많다 보니... 이런 곳도 생겨났네."
    "보호소 남자" "나가면 병원이랑 식량 보급소, 작은 학교 등 사람 살 만한 건 다 있어."
    "신기하다. 이런 마을이 안전구역 외부에도 있었다니."
    yeongwon "그럼 여기 사는 사람들은 추방된 사람들인가요...?"
    "보호소 남자" "맞아. 추방된 사람. 세계정부 하는 짓이 지겨워서 제 발로 뛰쳐나온 사람도 있고."
    yeongwon "아아, 저 근데... 고아원은..."
    "제일 물어보고 싶은 것이었다. 그 참상을 직접 봤지만 믿을 수가 없었기 때문에."
    "머릿속에 있는 영상이 제발 사실이 아니었으면 좋겠다."
    "보호소 남자" "......"
    show yeongwon serious
    with dissolve
    yeongwon "...사실대로 말해 주세요."
    "보호소 남자" "나는... 고아원 근처엔 가까이 갈 수 없었단다. 운좋게 빠져나온 아이들을 몇 명 구해내긴 했지만..."
    show yeongwon sad
    with dissolve
    yeongwon "네..."
    "보호소 남자" "배고프지? 먹을 걸 가져오마."
    stop music fadeout 1.0
    "그 말을 끝으로 남자는 말을 피하려는 듯 나가 버렸다."

#8 보호소 내부
    scene background shelter
    with fade
    play music "music/Other01.mp3"
    "- 10일 후 -"
    "유난히도 햇볕이 강한 날이었다."
    "나, 그리고 깨어난 하늘이는 이제 체력을 완전히 회복했고 몸도 어느 정도 움직이기 편해졌다."
    "하늘이 또한 이곳에 대한 자세한 설명을 들었고, 우리 둘은 어느 정도 완충구역 마을에 적응하여 생활하고 있었다."
    "다만 우리 둘 중 누구도 고아원에 대한 언급을 하지 않았다."
    "나와 하늘이는 햇빛을 피하기 위해 보호소 안에 들어와 앉아 있었다."
    show haneul serious at left
    show yeongwon idle at right
    with dissolve
    haneul "영원아, 원장이 바뀌었대."
    yeongwon "응?"
    show yeongwon serious
    with dissolve
    yeongwon "...뭐라고...?"
    haneul "...사람들이 지나가면서 얘기하는걸 들었어. 염소고아원에 새로운 원장이..."
    "얘가 뭔 소리를 하는지 모르겠네. 무슨 원장...?"
    "원장. 바닥에 내동댕이쳐져 씁쓸한 미소를 지은 모습으로 차갑게 식어가던 원장의 모습이 떠올랐다."
    haneul "고아원에 우리가 알던 사람들은 이제 없어."
    show haneul sad
    with dissolve
    haneul "나도 믿을 수가 없었어...."
    "하늘이는 울고 있었다."
    "생소한 모습이다."
    "우는 하늘이는 어떻게 대해야 할지 모르겠다."
    haneul "영원아... 너도 이젠 쉬어도 돼."
    show yeongwon sad
    with dissolve
    yeongwon "흑...흑......"
    "눈앞이 흐려졌다."
    "손바닥으로 가릴 수 없을 정도로 눈물이 흘렀다."
    "다리가 젖어가는 것이 느껴졌다."
    yeongwon "우리... 이젠 어떻게 하지 하늘아? 아무도 없어 이젠."
    "하늘이는 대답 대신 내 손을 꼬옥 붙잡아주었다."
    scene background black
    with dissolve
    stop music fadeout 1.0
    "그래도 아무도 없진 않다고."

#9 완충구역(10년 후)
    scene background hospital
    with fade
    play music "music/L47.mp3"
    pause(1.0)
    "어린 아이" "감따합니다!"
    "조그마한 병원에서 한 아이가 걸어 나왔다."
    "이곳의 아이들은 안전구역의 아이들보다는 잔병치레를 자주 하는 편이다."
    "그래도 우리 마을에서 실력도 최고고, 잘생기기까지 한 명의가 있으니 완전 안심이다."
    show yeongwon adult
    with dissolve
    yeongwon "나 왔어!"
    hide yeongwon
    with dissolve
    "의자에 앉아 도구들을 정리하고 있던 하늘이가 놀란 표정으로 고개를 돌렸다."
    show yeongwon adult at left
    show haneul adult at right
    with dissolve
    haneul "어, 일찍 끝났네?"
    yeongwon "그냥, 오늘은 정리만 하고 일찍 나왔어."
    haneul "아아, 나도 일찍 가려고 했는데... 오늘은 조금 더 일을 좀 도와야 할 것 같아. 금방 들어갈게. 먼저 가 있어. 요즘따라 환자가 많아서..."
    yeongwon "그럼 먼저 가서 준비하고 있을게. 파이팅하고!"
    haneul "응, 고마워. 이따 봐~"
    scene background black
    with fade
    "기절한 이후 완충구역에 있는 마을에서 생활한지 10년. 나는 마을 내 작은 학교이자 고아원에서 선생님으로 일을 하고 있다. 그리고 앞서 보았듯이 하늘이는 의사가 되었고."
    "완충구역에는 우리가 온 이후 사람이 점점 늘어나고 있다."
    "세계정부에 염증을 느낀 과학자들과 기술자들이 많이 들어와서인지, 이곳엔 생각보다 많은 인프라가 충족되어 있다."
    "하나 안타까운 점은, 사람들의 노력에도 이곳은 아직 많은 환경오염에 노출되어 있어서 건강의 악화가 다소 있다는 점이다."
    "이런 곳에 한번 들어오면 다시는 돌아갈 수 없음에도 불구하고 안전구역 밖으로 사람들이 발을 내딛는 이유는, 당연하겠지."
    stop music fadeout 5.0
    "세계정부는 10년 동안 변하지 않았다. 아니, 그들의 독재와 횡포는 더 심해졌다."
    scene background house
    with fade
    play music "music/L23.mp3"
    "나와 하늘이가 같이 살고 있는 집에 도착했다."
    "책상 위에는 어렸을 때 나, 하늘이, 한설이, 한별이, 연우 다섯이서 같이 찍은 사진이 꽂혀 있는 액자가 놓여 있다."
    "액자에서 사진을 꺼내 주머니에 넣었다."
    "그리고, 성인이 된 이후로 귀찮기도 하고 유치하기도 해서 서랍에 처박아버린 빨간 리본을 꺼내 머리카락을 묶었다. 오늘은 왠지 그런 기분이었다."
    "...잘 어울리나?"
    stop music fadeout 1.0
    "생각보다 나쁘지 않은 느낌이다."
    scene ecg ketsuichi 7
    with fade
    play music "music/RainSound.mp3"
    pause(1.0)
    haneul "이제 가자."
    haneul "몸을 숨기기엔 좋은 날씨네."
    "검은 하늘에는 장대비가 쏟아지고 있었다."
    stop music fadeout 3.0
    "우리는 우산을 들고 고아원으로 향했다."
    show end1
    with fade
    with Pause(3)
    $ renpy.movie_cutscene("end1credit.webm")
    return
