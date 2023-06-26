init 20:
    image ecg shou 1 = "ecg/shou1.png"
    image ecg shou 2 = "ecg/shou2.png"
    image ecg shou 3 = "ecg/shou3.png"
    image ecg end3 = "ecg/end3.png"

    image report_frag = "sprite/report-fragment.png"

# S#1. 스즈미야 하늘이의 우울 (가)
label scene201:
    # Fade in/out
    scene background oldschool
    with fade
    play music "music/L52.mp3"
    "얼마 뒤, 다시 만나기로 한 날이 되어 한별이, 한설이와 같이 아지트로 향했다."
    "매일같이 비밀 쪽지가 도착했나 살펴봤지만 하늘이가 쓴 쪽지는 찾을 수 없었다."
    show hanseol idle at left
    show hanbyeol idle at center
    show yeongwon idle at right
    with dissolve
    hanseol "오늘 하늘이 오겠지...?"
    show yeongwon serious with dissolve
    yeongwon "글쎄... 무슨 일이 생긴 건 아닌지 매일 밤 걱정돼서 잠도 제대로 못 잤어."
    show hanseol sad with dissolve
    hanseol "그래서 그렇게 매일 죽은 생선 같은 눈빛이었구나? 너 몰골 장난 아니었어!"
    show yeongwon shock with dissolve
    yeongwon "그 정도야...?"
    show hanbyeol sad with dissolve
    hanbyeol "잠은 제대로 자라고 몇 번을 말해.\n오죽하면 선생님이 우리보고 너한테 무슨 일 있냐고 물어보셨겠어."
    show hanseol happy with dissolve
    hanseol "맞아! 아무리 네 애인이 걱정된다고 해도 말이야, 비밀 연애면 비밀 연애답게 좀 숨기면서 살아야지!"
    show yeongwon fury with dissolve
    yeongwon "누가 비밀 연애래!"
    with vpunch
    show hanbyeol shock
    show hanseol shock
    with dissolve
    hanbyeol "쉿!"
    hanbyeol "우리 밖이야! 잊고 있었어? 정신 차려!"
    stop music fadeout 1.0
    show yeongwon shock with dissolve
    yeongwon "아."
    hide yeongwon
    hide hanbyeol
    hide hanseol

    scene background oldhallway
    with dissolve
    "이야기를 나누다 보니 어느새 아지트에 도착했다."
    "문 틈으로 희미하게 불빛이 새어 나온다. 하늘이가 먼저 도착한 걸까?"
    play sound "effect/dooropen_hideout.ogg"
    "조심스레 문고리를 잡아당기자, 오래된 백열등 아래서 책을 읽고 있는 하늘이의 모습이 보였다."
    "책에 완전히 빠져 있는지 문이 열리는 소리를 듣지 못한 것 같았다."
    "따스한 오렌지색 불빛에 하늘이의 눈가가 반짝이고, 이윽고 자그마한 물방울이 되어 볼을 타고 흘러내렸다."

    scene background dayhideout
    play music "music/L20.mp3"
    show haneul sad at right
    with dissolve

    show hanseol shock at left
    show hanbyeol shock:
        xalign 0.25
    show yeongwon shock:
        xalign 0.5
    with dissolve

    yeongwon "(울고 있잖아...? 역시 무슨 일이 있었던 건가...?)"
    play sound "effect/hinge.ogg"
    "문을 조금 더 열려고 한 발짝 내딛은 순간, 오래된 경첩에서 끼이익 소리가 울려 퍼졌다."
    stop sound fadeout 1.0
    haneul "어...?"

    "하늘이가 놀라 동그래진 눈으로 우리 쪽을 바라본다."
    "괜히 훔쳐본 것 같아 머쓱해하며 방 안으로 들어갔다."

    show yeongwon happy with dissolve
    yeongwon "책 읽고 있었구나... 방해해서 미안."
    show haneul happy with dissolve
    haneul "아냐, 괜찮아~"
    "하늘이는 뺨과 눈가의 눈물자국을 소매로 쓱쓱 지우면서 미소지었다."
    "정말 괜찮은 건가?"

    show yeongwon shock with dissolve
    yeongwon "왜 울고 있어? 반에서 무슨 일 있었던 거야?"
    haneul "아니, 그냥 읽고 있던 책이 슬퍼서 그랬지. 별 거 아니니까, 걱정하지 마."
    show yeongwon idle with dissolve
    yeongwon "그렇게 울 정도로 슬픈 내용이야?"
    show haneul sad with dissolve
    haneul "응... 주인공이 다른 사람들을 위해 목숨 바쳐 세상을 구하는 내용이야..."
    stop music fadeout 3.0
    show hanseol idle with dissolve
    hanseol "그냥 듣기만 해서는 꽤 평범한 히어로 이야기 같은데?"
    play music "music/L23.mp3"
    show haneul serious with dissolve
    haneul "그치만... 주인공의 친구는 과연 어떤 생각으로 주인공을 떠나보냈을까?{w} 그런 생각을 하니까 괜히 슬퍼져서..."
    show yeongwon happy with dissolve
    yeongwon "주인공 없이 남겨진 친구는 어떻게 생각할까...\n모두를 위해 희생했으니까 나라면 자랑스러울 것 같기도 한데?"
    show hanseol sad with dissolve
    hanseol "그렇지. 자신을 희생해서 훨씬 더 많은 사람들을 살렸잖아!"
    show haneul serious with dissolve
    haneul "역시 그렇겠지...? 전혀 슬플 일이 아닌 거지...?"
    stop music fadeout 2.0
    "그렇게 잠시 동안 소매로 눈가를 훔치던 하늘이는 밝게 웃으며 말했다."
    play music "music/L42.mp3"
    show haneul happy with dissolve
    haneul "헤헤, 책에 너무 몰입했나봐. 걱정하게 해서 미안해."
    show hanbyeol happy with dissolve
    hanbyeol "하늘이 네가 그렇게 책을 열심히 읽는 줄은 몰랐네. 어울린다면 어울리지만."
    show haneul serious with dissolve
    haneul "아... 그... 자유시간이 줄어들어서 독서 말고는 하기 힘들더라..."
    stop music fadeout 2.0
    show hanseol happy with dissolve
    hanseol "하늘이 너 전에도 그렇게 귀여웠는데 그새 더 완벽해졌잖아?!"
    play music "music/G09.mp3"
    "갑자기 한설이가 나에게 할 말이 있다는 듯 손짓한다."
    show hanseol happy:
        linear 0.4 zoom 1.05
    "조금 심각한 표정이길래 한설이가 시키는 대로 귀를 가져다 대자, 한설이가 소곤소곤 이야기하기 시작한다."

    hanseol "영원이 너 긴장해라, 언제 어디서 누가 하늘이를 뺏어갈지 몰라~"

    "..."
    "아니나 다를까, 쓸데없는 이야기였다."

    show hanseol happy:
        linear 0.1 zoom 1.0
    show yeongwon fury with dissolve
    with vpunch
    yeongwon "시끄러워!"

    "한설이가 이상한 소리를 더 늘어놓기 전에 한설이 머리를 밀쳐냈다."

    show hanseol shock with dissolve
    hanseol "아야!"
    show hanseol sad with dissolve
    hanseol "언니이~ 쟤가 나 때렸어어~ 혼내줘~"
    show hanbyeol fury with dissolve
    hanbyeol "...이럴 때만 언니지 아주."
    show haneul happy with dissolve
    haneul "푸훗."
    show haneul happy2 with dissolve
    haneul "정말 너희는 하나도 바뀐 게 없구나. 아직도 그렇게 티격태격하는 거야?"
    show yeongwon idle with dissolve
    yeongwon "한설이만 아니면 이렇게 말다툼할 일도 없었어..."
    show hanseol happy
    show hanbyeol idle
    with dissolve
    hanseol "어허~ 왜 그래! 이것도 우리 사이의 우정의 증표 아니겠어?"
    show yeongwon fury with dissolve
    yeongwon "에휴."

    "일부러 모두에게 들리도록 크게 한숨을 내쉬었다."
    "살며시 옆을 돌아보자 새어 나오려는 웃음을 열심히 참는 하늘이가 보였다."
    "잠시 뒤, 너무 열심히 웃음을 참았는지 찔끔 새어나온 눈물을 닦으며 하늘이가 말했다."

    show haneul happy with dissolve
    haneul "하아... 역시 변한 게 없어. 너희들 정말 좋아!"
    show hanseol happy with dissolve
    hanseol "에헤이, 뭐 그 정도 가지고~ 헤헤."
    show yeongwon happy with dissolve
    yeongwon "자자, 이제 이상한 콩트는 그만하고 뭐 먹으면서 얘기라도 하자.\n오늘은 탕비실에서 쿠키를 조금 가져왔어."
    show hanbyeol sad with dissolve
    hanbyeol "직권 남용이야, 그거."
    yeongwon "뭐 어때, 어차피 다른 사람들도 조금씩 가져 가고 있는걸."
    show hanbyeol shock with dissolve
    hanbyeol "...! 그건 몰랐네..."
    "비닐 포장지에 담긴 싸구려 버터향 쿠키를 집으며 우리는 이야기를 나눴다."

    with fade

    show hanseol sad with dissolve
    hanseol "...그래서 쟤는 반장이라는 애가 맨날맨날 퀭~하니 있는 게 귀신인지 사람인지 분간이 안 간다니까!"
    show hanbyeol idle with dissolve
    hanbyeol "자라고 몇 번을 말해도 안 들어. 하늘이 네가 좀 얘기해줘봐."
    show haneul idle with dissolve
    haneul "아무리 할 일이 많아도 그렇지, 잠자는 건 중요해, 영원아. 아프면 여기로 놀러올 수도 없잖아?"
    show hanseol shock with dissolve
    hanseol "그래그래, 잘한다! 맨날 하늘이 생각하느라 정신이 빠져가지고 말이야. 얼마나 조마조마한지 알아!"
    "...어째서 내가 욕을 먹는 분위기가 된 거지?"
    "분명 서로 어떻게 지내는지 알려주자고 시작한 대화였는데 어느샌가 내가 대화의 주제가 되어 있었다."
    "차라리 칭찬이라도 해주지. 나빴어."

    show yeongwon serious with dissolve
    yeongwon "알았어, 알았어. 내가 다 미안해, 다음부터는 안 그럴게."
    show hanbyeol sad with dissolve
    hanbyeol "진짜 조심해, 너. 지난번에 여기 오고 난 뒤로 특히 더 심했어."
    hanseol "맞아! 네가 이상한 짓 하면 우리도 난감하다구!"
    show yeongwon fury with dissolve
    yeongwon "아잇, 알았다니까 그러네! 그래서 이틀 전부터 잠 많이 잤잖아!"
    show hanseol shock with dissolve
    hanseol "이익, 소 잃고 외양간 고치는 격이잖아! 처음부터 그렇게 하지 그랬냐!"
    show hanbyeol happy with dissolve
    hanbyeol "됐어, 한설아. 이번에도 설마 그러겠어? 이렇게까지 데이고 나서 한 번이라도 더 그러면 사람이게?"
    show hanseol happy with dissolve
    hanseol "너, 우리 별이 봐서 한 번 봐준다. 별아, 카드게임이나 하러 가자!"

    hide hanseol
    hide hanbyeol
    with dissolve

    show yeongwon idle:
        linear 0.3 xalign 0.3
    show haneul:
        linear 0.3 xalign 0.7

    "...한바탕 폭풍이 지나간 것 같다."

    show haneul happy with dissolve
    haneul "역시 소꿉친구란 건 좋네. 마음이 더 안정되는 느낌이야."
    yeongwon "......방금 대화는 전혀 마음이 안정되는 대화는 아니었던 것 같은데."
    haneul "쿡쿡. 난 그저 너희들이 보고 싶었을 뿐인걸. 옛날 생각이 나서 난 이쪽이 더 좋아."
    yeongwon "옛날부터 이렇게 맨날 싸웠는데. 하늘이 네가 없으니까 브레이크를 걸어줄 사람이 없더라."
    show haneul idle with dissolve
    haneul "너랑 한설이 둘이 만나면 그렇지 뭐. 그래도 이젠 나이 먹을 만큼 먹었잖아?"
    show yeongwon fury with dissolve
    yeongwon "한설이 쟤가 나한테 시비 거는 걸 어떡해!"
    show haneul happy with dissolve
    haneul "그래그래, 그래서 오늘은 왔잖아?"
    stop music fadeout 1.0
    yeongwon idle "연우도 같이 왔으면 좋았을 텐데. 몸 상태는 조금 어때?" with dissolve
    play music "music/G11.mp3"
    show haneul serious with dissolve
    haneul "아... 그..."
    show yeongwon shock with dissolve
    yeongwon "하늘아?"

    "하늘이는 뭔가를 꾹 참으려는 듯 몸을 떨었다."

    show haneul sad with dissolve
    haneul "아직 몸이 다 낫지 않아서... 바깥에 돌아다니기는 힘든 것 같아..."
    show yeongwon sad with dissolve
    yeongwon "앗... 미안해, 내가 너무 성급했네..."
    show haneul sad with dissolve
    haneul "아니... 괜찮아."
    show haneul happy with dissolve
    haneul "이미 익숙해졌어!"
    show yeongwon idle with dissolve
    yeongwon "...하늘아."
    show haneul idle with dissolve
    haneul "응?"
    show yeongwon happy with dissolve
    yeongwon "힘든 일이 있다면 혼자 담아두지는 마."
    yeongwon "나라도 괜찮다면 언제든지 들어줄 테니까."
    show yeongwon blush with dissolve
    yeongwon "나는 항상 네 편이니까... 알았지? 그러니까 그런 얼굴 하지 마."
    show haneul idle with dissolve
    haneul "......내 얼굴 많이 이상해?"
    show yeongwon happy with dissolve
    yeongwon "아, 아니 그냥. 슬픈 표정하니까... 저... 그 귀여운 얼굴이 다 망가지잖아."
    show haneul serious with dissolve
    haneul "......"

    "하늘이는 놀라 동그래진 눈으로 나를 바라보았다."
    "내가 미쳤나봐, 이런 말을 왜 했지?"
    "뒷감당은 어떻게 하려고?!"
    "하늘이는 멍하니 나를 바라보고 있지만 차마 눈을 맞출 자신이 없다."
    "결국 내 시선은 땅바닥으로 떨어지고 말았다."

    scene background black
    with dissolve

    "얼마나 지났을까, 나는 훌쩍이는 소리에 고개를 들었다."

    yeongwon "미, 미안해! 그렇게나 싫었어?"
    haneul "아니, 아니야... 그냥... 그냥... 훌쩍."
    haneul "정말 고마워... 정말로..."

    scene ecg shou 1
    with fade

    "하늘이는 소매로 눈물을 훔쳤지만 흘러나오는 눈물을 멈출 수는 없었다."
    "하늘이는 내 어깨에 기대어 작은 소리로 계속 울었다."
    "도대체 하늘이네 반에서는 어떤 공부를 시키길래 이렇게 힘들어 하는 걸까?"
    "싫어하는 일을 억지로 강요당하고 있는 건 아닐까?"
    "차라리 하늘이가 영재반을 그만두고 일반반으로 내려와줬으면, 하고 마음속으로 떼를 써 본다."
    "하늘이가 똑똑하고, 나중에 사회에 도움이 되는 일을 맡게 될 거라는 건 알지만, 그래도 하늘이가 힘들어 하는 모습은 보기 싫다."
    "아무것도 아닌 나는 그저 하늘이가 우는 모습을 바라보고, 등을 토닥여 주는 것밖에는 할 수 없었다."
    stop music fadeout 1.0
    scene background black
    with dissolve

    hanseol "별아, 저거 봐. 영원이가 하늘이 울렸어."
    hanbyeol "좋아한다면 좋아한다고 할 것이지, 또 꼬맹이처럼 이상한 짓 했겠지."
    "그런 거 아니야."

# S#2. 하늘이 보이지 않는 거리 (가)
label scene202:
    pause 1.0

    scene background oldhallway
    with dissolve
    play music "music/L44.mp3"
    "시간이 참 빠르다. 저번에 하늘이를 만난 게 엊그제 같은데."
    "한설이와 한별이에게 하늘이의 우는 모습을 들킨 뒤로 잔뜩 놀림받고, 그후로도 한동안 구박을 받아서 최대한 얌전히 지냈다."
    "잠도 억지로 자고 하늘이의 상황에 대해서도 최대한 긍정적으로 생각하려고 노력했더니 선생님께는 들키지 않았다."
    "하지만 한설이에게는 구박을 많이 받았다. 쳇, 나를 너무 잘 알아."

    show hanseol idle at left
    show hanbyeol idle at center
    show yeongwon idle at right
    with dissolve

    hanseol "영원아, 어제 비밀 우편함 확인해봤어?"
    yeongwon "응. 오늘 올 수 있을 것 같대."
    show hanseol idle2 with dissolve
    hanseol "또 하늘이 울리면 가만 안 둬?"
    show yeongwon fury with dissolve
    yeongwon "나 때문에 운 거 아니라고!"
    play sound "effect/dooropen_hideout.ogg"
    show background dayhideout dark
    with fade
    "소곤소곤 말다툼을 하면서 아지트 문고리를 잡고 돌렸다."
    stop sound fadeout 1.0
    "이상하게도 불이 꺼져 있었다. 보통은 하늘이가 먼저 와서 불 켜고 책을 보는데 말이다."

    hanbyeol shock "하늘이가 늦는다고? 별일이네." with dissolve
    yeongwon shock "그러게." with dissolve

    "문 옆을 더듬어 전등 스위치를 찾는다."

    show background dayhideout
    with dissolve
    play sound "effect/fluorescent.ogg"
    "스위치를 올리자 팔랑팔랑 종이 한 장이 스위치에서 떨어진다."
    stop sound fadeout 1.0
    "하늘이가 비밀 쪽지를 보낼 때 즐겨 사용하는 구름 모양 종이에 글이 적혀 있었다."

    call screen letter("""
갑자기 이렇게 쪽지만 남기고 사라져서 미안해.
원장 선생님께서 오늘 급히 부르셔서 도저히 만날 수 없을 것 같아.
학교 일 관련해서 조금 도와달라고 하시는 걸 보니 들킨 것 같지는 않아.
그래도 조금 신기한 일이네. 뭐든지 혼자 해결하실 것 같은 사람인데.
오늘 간다고 했는데 실망시켜 버려서 미안해... 다음에는 꼭 갈게!

P.S. 아까 얼핏 들었는데, 경비원 아저씨 몇 분이 휴가 갔다가 돌아오셨대.
그래서 오늘 밤에는 여기까지 순찰 돈다고 하셨으니까 되도록 빨리 기숙사로 돌아가!
절대 들키면 안 돼!
        """ \
    )

    show hanseol happy with dissolve
    hanseol "뭐야뭐야, 이 나이 먹고 러브레터야?"
    show yeongwon serious with dissolve
    yeongwon "아니, 오늘 원장한테 잡혀서 못 온대..."
    show hanbyeol shock with dissolve
    hanbyeol "원장 선생님이...?"
    show hanseol shock with dissolve
    hanseol "서, 설마 우리들이 여기서 만난 걸 들켰다던가...?!"
    yeongwon "그런 건 아닌데, 뭔가 도와달라고 하신 것 같아..."
    show hanseol sad with dissolve
    hanseol "응? 도와달라고? 별일이네, 그 무뚝뚝한 사람이 그랬다고?"
    yeongwon "......"
    show hanseol happy with dissolve
    hanseol "에이, 그렇게 삐지지 말고! 여기 다음에 꼭 온다고 했잖아, 그치?"
    stop music fadeout 1.0
    yeongwon "물론 그건 그렇지만..."
    play sound "effect/gate.ogg"
    "그때, 갑자기 들려오는 대문 소리."
    "녹슨 경첩이 맞물리며 찢어질 듯 비명을 지르고, 뒤이어 밝은 손전등 빛 여러 개가 구교사를 비춘다."
    stop sound fadeout 1.0
    "우리는 잽싸게 창틀 아래로 몸을 숙였다."
    pause(1.0)
    play music "music/G42.mp3"
    show yeongwon shock with dissolve
    yeongwon "아, 벌써 들어왔어?!"
    show hanseol shock
    hanseol "뭐야, 오늘은 안전한 날이라면서?!"
    show hanbyeol shock with dissolve
    hanbyeol "불심검문인가...? 곤란하네..."
    yeongwon "아니, 하늘이가 오늘은 대타가 온댔어!"
    hanseol "일단 여기는 창가라서 너무 눈에 띄어. 다른 곳으로 가야 해!"
    hanbyeol "뒷문 쪽은?"
    yeongwon "몇 명은 건물 뒤쪽으로 돌아간 걸 보니까 경계선 점검 나간 것 같아. 그쪽도 위험해."
    hanseol "아아아... 뭐야, 우리 구교사에 갇힌 거야?!"
    yeongwon "구조상 경비들이 나가기 전까지는 못 나갈 거야. 으으, 설마 오늘 기숙사 사감이 점호하는 건 아니겠지?"
    hanseol "점호?! 절대 안 돼!"
    show hanbyeol sad with dissolve
    hanbyeol "설아, 진정해. 점호 불참으로 사감한테 잔소리 듣는 게 경비한테 붙잡히는 것보단 나아."
    yeongwon "한별이 말이 맞아. 일단 나가자!"

    scene background oldhallway
    with fade
    play sound "effect/footstep_short.ogg"
    "우리는 읽던 책이나 중요한 물건을 챙겨서 밖으로 나왔다."
    stop sound fadeout 1.0
    "물론 혹시 아지트가 들키더라도 그냥 버려진 방처럼 보이도록 잊지 않고 가구를 조금 어지럽혀 뒀다."
    "이걸로 우리가 큰 소리를 내지 않는 이상 경비들이 누군가 있다는 생각은 하지 않을 거다."
    stop music fadeout 1.0
    "...아마도."

    scene background oldstairs
    with Fade(0.4, 0.7, 0.4)
    play music "music/G44.mp3"
    "경비 아저씨가 지하 순찰을 마치고 1층으로 올라오는 타이밍에 맞춰 비상계단을 통해 지하로 내려갔다."
    "이미 순찰을 끝냈으니 여기로 다시 돌아올 리는 없을 것 같고, 경비 아저씨가 돌아간 뒤 1층으로 나가면 될 것 같다."

    show hanseol sad at left
    show hanbyeol idle at center
    show yeongwon idle at right
    with dissolve

    hanseol "...나 여기 어두워서 무서운데."
    yeongwon "조금만 참아. 여기서 기다리다가 경비 아저씨 나갈 때 따라 나가면 되는 거야."
    yeongwon "그나저나 가방 들고 오길 잘했다. 아니었으면 지금쯤 아지트 들켜서 비상상황이 됐을걸."
    show hanbyeol shock with dissolve
    hanbyeol "새것 같아 보이는 책이나 카드 같은 거 전부 챙겨 온 거 맞지?"
    yeongwon "가구도 어지럽혀 놨어. 걱정하지 마."
    show hanseol happy with dissolve
    hanseol "맞아! 나도 내 웨이스트 백에 있는 거 빼고 보드게임 같은 거 넣어왔다구."
    hanbyeol "{cps=4}......{/cps}뭐라고?"
    hanseol "보드게임 챙겨왔어! 이거라도 지금 할래?"
    hanbyeol "아니 그게 아니라, 네 백에 원래 뭐 들어 있었는데?"
    show hanseol sad with dissolve
    hanseol "영원이가 준 쿠키가......"
    show hanseol shock with dissolve
    hanseol "아."
    show yeongwon shock with dissolve
    yeongwon "야, 이 바보야, 그걸 거기에 두고 오면 어떡해?!"

    "그때, 계단에 무전기 소리가 울려퍼졌다."
    play sound "effect/radionoise.ogg"
    "치직- 칙- 852호에서 최근에 사람이 있었던 흔적 발견. 경비태세를 강화하십시오- 치직-"
    stop sound
    ". . ."

    show hanseol shock with dissolve
    hanseol "이거 어떡해?!"
    yeongwon "잘 하는 짓이다. 계단 위에는 경비원 있어서 더 못 올라간다고!"
    hanbyeol "아, 저기 옆에 출입금지라고 써 있는 간이문, 저기라도 들어가 있자!"
    show hanseol sad with dissolve
    hanseol "그치만 출입금지인데?"
    show yeongwon serious with dissolve
    stop music fadeout 1.0
    yeongwon "지금 한시가 급하다구! 한별아, 문 열어!"
    play sound "effect/dooropen.ogg"
    show background labhallway dark
    with fade
    stop sound fadeout 1.0
    play music "music/G42.mp3"
    "지하 전기 제어실으로 향하는 듯 보이는 문을 열고 들어가자, 생각보다 긴 복도가 눈에 띄었다."
    "머뭇거리는 한설이를 억지로 끌고 들어오자, 한별이가 문을 닫고 걸어 잠갔다."

    show hanbyeol shock with dissolve
    hanbyeol "응...? 이상하네?"
    show yeongwon idle with dissolve
    yeongwon "왜?"
    hanbyeol "이거, 안에서 잠그면 바깥에서 열 수 없는 구조로 돼 있어."
    show yeongwon shock with dissolve
    yeongwon "무슨 소리야?"
    hanbyeol "바깥에 열쇠구멍 같아 보이는 게 없었잖아? 근데 안에서는 잠글 수 있게 돼 있네. 특이하다."
    show yeongwon serious with dissolve
    yeongwon "그러네? 의외로 여기는 제어실이 아니라 그냥 예전에 쓰이던 직원 휴게실일지도."
    show hanseol sad with dissolve
    hanseol "우우... 얘들아, 우리 불이라도 켜면 안 될까...?"
    show hanbyeol idle with dissolve
    hanbyeol "문 닫았어."
    show yeongwon idle with dissolve
    yeongwon "그러면 켜도 될 것 같아. 스위치를 찾자."
    stop music fadeout 1.0
    show background labhallway
    with dissolve
    play sound "effect/fluorescent.ogg"
    "달칵, 벽을 더듬어 찾은 스위치를 올리자, 복도 저 멀리 방 하나에 불이 깜빡깜빡 들어왔다."
    stop sound fadeout 1.0
    play music "music/L44.mp3"
    show hanseol sad with dissolve
    hanseol "정작 복도에 불이 안 들어오잖아아..."
    show yeongwon idle with dissolve
    yeongwon "일단 밝은 곳으로 가보자."

    show background hiddenlab
    with Fade(0.4, 0.7, 0.4)

    show hanbyeol serious with dissolve
    hanbyeol "버려진 실험실...?"

    "복도 너머 불빛을 따라 들어온 방은 마치 폭풍이 훑고 지나간 듯 어지럽혀진 방이었다."
    "분명 검정색일 터인 의자는 넘어진 채 먼지가 소복이 쌓여 회색으로 변해 있고, 바닥은 흩어진 종이다발으로 어지러웠다."
    "깜빡, 깜빡."
    "책상에 놓여진 컴퓨터는 자그마한 전구를 반짝이며 주인이 돌아오기를 기다리는 듯했다."

    show hanseol sad with dissolve
    hanseol "여기... 진짜로 우리 고아원 맞아?"
    show hanseol shock with dissolve
    hanseol "우리 어쩌면 와서는 안 되는 곳에 온 거 아닐까...?"
    show yeongwon fury with dissolve
    yeongwon "누구 탓에 우리가 출입금지 구역에 들어오게 됐을까, 한설아?"
    show hanseol shock with dissolve
    hanseol "......"
    show hanseol idle with dissolve
    hanseol "나 아니야."

    "너 맞아."

    show hanbyeol idle with dissolve
    hanbyeol "얘들아, 여기 노트 한 번 읽어봐."
    show yeongwon idle with dissolve
    yeongwon "어디 보자."

    show report_frag:
        zoom 0.4
        align (0.5, 0.5)
    with dissolve

    hanseol idle "앞부분이 하나도 안 보이는데? 다 노래졌고... 이거 뭐야?" with dissolve
    hanbyeol idle "모르겠어. 냄새도 많이 나지는 않는데... 곰팡이 이런 거 아닌가?" with dissolve
    hanseol shock "으악?! 내가 곰팡이를 만지고 있었던 거야?!" with dissolve

    show report_frag:
        linear 0.3 zoom 0.5

    yeongwon serious "아니, 그게 문제가 아니야. 이거 도대체 무슨 소리야?" with dissolve
    hanbyeol idle "몰라. 그래도 이 실험실...? 같은 곳에 뭔가 단서가 있겠지." with dissolve

    hide yeongwon
    hide hanbyeol
    hide hanseol
    hide report_frag
    with dissolve
    stop music fadeout 1.0
# Intermission. 심해소년
label scene204:
    scene background lab
    with dissolve
    play music "music/G01.mp3"
    "특별동 지하 깊숙한 곳 어딘가."
    "백색 할로겐 조명이 눈부시게 비추는 수술대 위에 두 개의 인영이 비친다."
    "건드리면 부서질 듯 백색투명한 피부를 가진 여자아이와\n하늘빛 단발 머리카락이 반짝이는 남자아이."
    "두 아이 모두 왼손목에 칙칙한 주황색 수액팩을 연결한 채 곤히 잠들어 있다."
    play sound "effect/footsteps_heel.ogg"
    "또각, 또각."
    show principal idle at center
    with dissolve
    "무균실 안으로 백색 실험복을 입은 여성이 걸어 들어온다."
    stop sound fadeout 1.0
    "한 고아원의 원장이라고는 생각할 수 없는 차가운 눈빛으로 두 아이를 지켜보는 여성."
    "한동안 지긋이 아이들을 바라보고는 수술대 옆의 테이블에서 핏빛 약병과 주사기를 손에 든다."
    "그녀는 익숙한 손길로 주사기 실린더를 채우고, 여자아이의 곁으로 향한다."
    "곧, 팔에 연결된 튜브에 주사기를 끼우고, 거침없이 실린더를 비워낸다."
    "여자아이는 주사바늘로부터 퍼져나가는 한기에 몸을 떨었다."
    scene ecg shou 3
    with fade
    "얼마나 시간이 지났을까."
    "삐, 삐, 규칙적으로 들려오던 심전도계 소리가 점점 빨라지고 여자아이의 호흡도 함께 빨라지기 시작했다."
    "고통스러운 듯 얼굴을 찡그리며 서서히 눈을 뜬다."

    "???" "콜록... 콜록... 워... 원장선생님...? 콜록...!"
    "???" "선...생님... 콜록... 숨... 숨이 잘 안 쉬어...져요..."
    principal "괜찮다. 약을 넣고 있으니까 곧 괜찮아질 거야."

    "그제서야 팔을 들어 정맥에 꽂힌 주사바늘을 보는 여자아이."

    "???" "몸이... 이상해요... 콜록, 쿨럭...!"

    "기침할 때마다 여자아이의 투명한 입가는 새빨간 피로 얼룩져갔다."
    "여자아이는 바들바들 떨리는 손을 원장에게로 향하지만 그 손이 원장에게 닿는 일은 없었다."
    "갑자기 경련하기 시작하는 팔."
    "팔에서부터 온몸으로 퍼진 발작은 미친 듯이 심전도계의 버저를 울렸고, 아이의 목은 힘없이 몸의 경련에 휘둘려 흔들린다."
    "산소를 원하는 몸은 죽을 힘을 다해 숨을 들이쉬지만 기도로 흘러 들어가는 건 공기가 아닌 입에 가득한 피고름과 거품이었다."

    "???" "컥... 커억....!"

    "강렬한 이물감에 들이쉰 것을 토해내지만 나오는 것은 불길할 정도로 새까만 핏덩이 뿐이었다."
    "아이의 새하얀 환자복은 점점 검붉은 색으로 물들어갔다."
    "그러나 원장은 수술대 옆에서 여자아이를 관찰할 뿐이었다."
    "아이의 각혈에 실험복과 얼굴에 피가 튀어도 덤덤히 자리를 지켰다."
    "아이가 도움을 바라며 뻗은 손마저 냉담하게 무시하고 그저 묵묵히 수술대 옆자리에서 가만히 여자아이를 지켜보았다."
    "삐. 삐. 삐. 아이의 경련과 함께 심전도계의 버저음도 잦아들었고, 이윽고 기나긴 버저음 말고는 들리지 않게 되었다."
    "그제서야 원장은 심전도계의 센서를 뽑으며 실망스러운 듯 내뱉었다."

    principal "......실패...군."

    "피투성이 수술대를 구석에 밀어놓고는 원장은 다시 품에서 핏빛 약병과 새로운 실린더를 꺼냈다."
    "이번에는 곤히 잠든 하늘빛 머리카락의 남자아이를 바라보고서."
    stop music fadeout 1.0

# S#3. 마지막 단서
label scene205:
    scene background dormlowchroma dark
    with fade
    play music "music/L44.mp3"
    "그 숨겨진 방은 깜짝 놀랄 만한 정보로 가득했었다."
    "아니, 학교에서 아무도 가르쳐주지 않는 일들로 가득했다."
    "한참 뒤, 우리는 경비원이 모두 퇴근한 사실을 확인하곤 서둘러 기숙사로 돌아갔다."
    "그렇지만 나는 그 방에서 읽은 것들에 관한 것을 잊어버릴 수가 없었다."
    "나는 지금까지 지구가 이렇게 된 것은 인간이 자원을 낭비해서 오존층이 파괴된 것이라고 배웠다."
    "그렇지만 그때 읽은 자료에서는 원인불명이라고 했다."
    "나는 지금까지 바깥에 나가면 몸이 불타는 듯 아프고, 병에 걸려 죽는다고 배웠다."
    "그렇지만 그때 읽은 노트에서는 그저 몸이 변하는 과정이라고 했다."
    "나는 지금까지 반사 패널 안에서만 사람이 살 수 있고, 바깥에 나가서 생긴 병은 치료할 수 없다고 배웠다."
    "그렇지만 그때 읽은 노트에서는 어려운 이름을 가진 치료약이 효과가 있을 것 같다고 했다."
    "내가 지금까지 알고 있었던 것은 뭘까?"
    "그럼 선생님들이나... 원장 선생님은 이 사실을 알고 있을까?"
    "나는 이런저런 생각을 하면서 잠들었다."

    scene background classday
    with Fade(0.4, 0.7, 0.4)

    "...어제 너무 늦게 잔 것 같다."
    "피곤해서 하나도 기운이 나지를 않는다."
    "아... 또 한설이랑 한별이가 뭐라고 하겠네..."

    show yeongwon serious
    with dissolve
    yeongwon "하아..."
    play sound "effect/dooropen_class.ogg"
    "작게 한숨을 쉬며 교실 문을 열었다."
    stop sound fadeout 1.0
    show yeongwon idle with dissolve
    yeongwon "안녕."

    "문을 열자 한설이와 한별이가 보였다."

    show hanseol sad at left
    show hanbyeol serious at right
    with dissolve

    hanseol "좋은 아침이야아..."
    hanbyeol "......"

    "...둘 다 피곤해 죽을 것 같은 표정이다."

    yeongwon "매일 나한테 잠 좀 자라면서 시끄럽게 굴면서 왜 그 모양이야?"
    hanseol "어제 그런 걸 알아냈는데 어떻게 잠을 자겠어어..."
    show yeongwon sad with dissolve
    yeongwon "그건 맞지... 나도 비슷한 생각하느라 잠 제대로 못 잤어."
    play sound "effect/dooropen_class.ogg"
    "드르륵."
    "문이 열리는 소리에 놀라 돌아보니 선생님이 들어오고 계셨다."
    stop sound fadeout 1.0
    show yeongwon idle with dissolve
    yeongwon "으아, 들키겠다. 이따가 점심 때 다시 얘기하자."
    stop music fadeout 2.0
    "서둘러 아무 일도 없었다는 듯 한별이와 한설이에게 손을 흔들고 자리로 향했다."
    scene background classday
    with fade
    play music "music/G17.mp3"
    "점심 시간."
    "계속된 수업에 질린 아이들은 모두 삼삼오오 모여 배급받은 도시락을 열었다."
    "한별이와 한설이가 도시락을 받아 오기를 기다리며 미리 슬쩍 메뉴를 확인했다."
    "인공육 함박 스테이크."
    "평소 음식보다 괜찮은 식사에 안도의 한숨을 내쉬었다."

    show yeongwon idle at left
    show hanbyeol idle at center
    show hanseol happy at right

    hanseol "히히, 오늘은 맛있는 거다!"
    hanbyeol "어차피 배양하고 남은 거 골라다가 갈아서 만든 거겠지..."
    hanseol "아니! 함박 스테이크야! 그럴 리가 없어!"
    hanbyeol "과연 그럴까...?"

    "열린 교실 문으로 한별이와 한설이가 들어왔다."
    "이 고기의 출처에 관해서 토론하고 있는 듯하다."
    "아마 한별이의 말이 정답일 텐데..."
    "굳이 알려줄 필요는 없으려나."

    yeongwon "얼른 와. 할 이야기가 있어."
    show hanseol idle with dissolve
    hanseol "아 맞다맞다, 그랬지."
    stop music fadeout 1.0
    yeongwon "일단 모여봐."

    "셋이서 머리를 맞대고 소곤소곤 이야기를 시작했다."
    play music "music/L19.mp3"
    show yeongwon serious with dissolve
    yeongwon "어제 그 방에서 읽은 문서 있잖아? 뭔가 수상해."
    show hanbyeol serious with dissolve
    hanbyeol "나도 그렇게 느꼈어. 어제 밤에 계속 생각해 봤는데 뭔가 위화감이 들어."
    yeongwon "응. 우리가 지금 배우고 있는 내용이랑 전혀 다른 이야기도 적혀 있었고..."
    yeongwon "그러면 어느 쪽이 맞는 거지? 지금 우리가 보고 있는 교과서? 아니면 어제 본 그 오래된 연구 노트?"
    hanseol "교과서가 정확하겠지! 지금까지 연구한 걸 모아서 책으로 정리한 게 교과서 아니야?"
    yeongwon "물론 교과서는 지금까지 연구한 것을 정리한 책이 맞아. 하지만 어제 본 내용이랑 너무나도 차이가 나는데?"
    yeongwon "거기다가 정보 통제에 관한 내용도 적혀 있었다고?"
    hanbyeol "어제 그 방에서 알아낸 정보가 사실이고, 선생님들이 우리에게 거짓말을 하고 있다는 거야?"
    yeongwon "그게 내 생각이야. 그치만 그때 본 노트가 오래된 거라서 지금 당장 그렇게 결론지을 수는 없어. 아직은."
    hanseol "그러면 어떻게 하려고?"
    yeongwon "더 최근의 연구 결과를 찾아봐야지. 반장 권한으로 이것저것 찾아보기는 하겠지만 아마 한계는 있을 거야."
    hanseol "으음.... 굳이 그렇게 하지 말고 차라리 교무실을 한번 털어보는 건 어때?"
    show yeongwon shock with dissolve
    yeongwon "미쳤어?! 그건 너무 위험하잖아!"
    hanbyeol "아니... 그거 괜찮은 방법일 수도 있어..."
    yeongwon "한별이 너까지?!"
    show hanbyeol idle with dissolve
    hanbyeol "아니, 생각해봐. 영원이 너는 반장이지만 네가 접근할 수 있는 정보는 기껏해야 학생 이름이랑 기숙사 위치 뿐일 거고, 선생님들이 네 이름을 아는 정도밖에 안 돼."
    hanbyeol "나도 마찬가지야. 아무리 일반반 학생이라지만 듣는 수업 내용을 결정할 수 있는 것도 아니고, 바깥 세상이랑 접점도 우리한테는 없어."
    hanbyeol "그러면 직접 발로 뛰어서 찾을 수밖에 없지."
    show yeongwon serious with dissolve
    yeongwon "그건 맞는 말이긴 한데..."
    show hanseol happy with dissolve
    hanseol "그거 재밌겠다! 나도 할래~"
    yeongwon "......"

    "한별이의 말이 맞다."
    "지금 상황에서는 우리가 할 수 있는 일이 하나도 없다."
    "그때 적혀있던 치료약에 대한 정보를 조금이라도 더 얻어야 한다."
    "어째서 선생님들은 치료약이 있을 수도 있는데도 우리에게 알려주지 않는지 알아야만 한다."

    yeongwon "...알았어."
    show yeongwon idle with dissolve
    yeongwon "하는 수 없지. 조금 더 정보를 얻을 방법은 그것 뿐인 것 같다."
    yeongwon "그러면 연구 결과 같은 걸 찾을 수 있을 만한 곳은 어디어디 있을까?"
    show hanbyeol idle with dissolve
    hanbyeol "일단 도서관이 먼저겠지. 만약 실제로 정보조작이 진행되고 있다면 별 수확은 없겠지만 너는 반장이니까 이것저것 핑계를 대면 쉽게 들어갈 수 있을 거야."
    yeongwon "교무실도 한번 가봐야지. 여러 선생님들이 계시니까 뭔가 비밀 폴더 같은 것도 있을 법한데."
    hanseol "원장 선생님 방도 있어! 원장 선생님은 맨날 흰 실험복을 입고 계시는데 뭔가 방에서 실험을 하고 계시지 않을까?"
    yeongwon "으음... 일리 있네."
    yeongwon "그러면 도서관, 교무실, 원장실, 이렇게 세 군데를 조사해보는 거지?"
    hanbyeol "그 정도면 완벽하기까지는 아니어도 선생님들이 우리에게 뭔가를 숨기고 있다는 결정적 증거는 찾을 수 있을 거야."
    yeongwon "그러면 나는..."
    menu:
        "어디로 가야 할까?"
        "도서관":
            jump scene216
        "교무실":
            jump scene226
        "원장실":
            jump scene236

label scene216:
    yeongwon "그러면 나는 도서관에 가볼게. 아까도 말했듯이, 학습자료를 복사하러 왔다고 말하면 제한구역까지는 사서 선생님이 데려다 줄 거야."
    hanseol "그러면 나는 원장실에 갈래! 항상 거기를 지나다니니까 경비원이 언제 나오는지 정도는 알고 있어!"
    hanbyeol "...그러면 나는 교무실이겠네. 선생님들이 안 계실 때 한번 둘러보고 올게."
    yeongwon "좋아, 그럼 각자의 역할도 결정된 거네?"
    yeongwon "그러면 오늘 각자 정해진 곳에 가 보기로 하자."
    hanseol "알았어!"

    hide yeongwon
    hide hanseol
    hide hanbyeol
    with dissolve

    "그리고 우리는 얘기하는 사이에 스테이크가 식어버린 것을 눈치채지 못했다."
    "함박스테이크를 잘라 입에 넣었다."
    "음, 이거 싸구려 배양육이 분명해. 웩."

    scene background schoolhallway
    with Fade(0.4, 0.7, 0.4)

    "해가 뉘엿뉘엿 넘어가는 저녁."
    "다음날 수업 준비라는 핑계로 평소 갈 수 없는 도서관 깊숙한 서고에 들어가 봤다."
    "갈색 봉투에 가득 담긴 서류가 책장에 빽빽하게 채워져 있었다."
    "기후 변화, 치료약, 패널, 등..."
    "수많은 자료를 꺼내어 훑어보았지만 현재 교과서를 뒷받침하는 논문만 잔뜩 쌓여있을 뿐이었다."
    "아쉬운 마음으로 제한구역을 뒤로하며 사서 선생님께 여쭤보았다."
    "그곳이 제한구역인 이유는 그저 원본 논문을 소장하고 있기 때문에 훼손되면 안 되기 때문이라고 했다."
    "......"
    "괜히 헛걸음을 한 것 같다."
    "대충 골라잡은 논문을 한 묶음 복사한 뒤 나는 터덜터덜 만나기로 한 장소로 향했다."
    stop music fadeout 1.0
    jump scene300

label scene226:
    yeongwon "그러면 나는 교무실에 가볼게. 반장이니까 교무실에서 여기저기 기웃거려도 그렇게 이상하게 보지는 않을 거야."
    hanseol "그러면 나는 원장실에 갈래! 항상 거기를 지나다니니까 경비원이 언제 나오는지 정도는 알고 있어!"
    hanbyeol "...그러면 나는 도서관이겠네. 너한테 부탁받아서 자료 검색이랑 복사 좀 하러 왔다고 할게."
    yeongwon "좋아, 그럼 각자의 역할도 결정된 거네?"
    yeongwon "그러면 오늘 각자 정해진 곳에 가 보기로 하자."
    hanseol "알았어!"

    hide yeongwon
    hide hanseol
    hide hanbyeol
    with dissolve

    "그리고 우리는 얘기하는 사이에 스테이크가 식어버린 것을 눈치채지 못했다."
    "함박스테이크를 잘라 입에 넣었다."
    "음, 이거 싸구려 배양육이 분명해. 웩."

    scene background schoolhallway
    with Fade(0.4, 0.7, 0.4)

    "방과후."
    "친구들 모두 기숙사에 돌아가려고 주섬주섬 가방을 챙길 때, 나는 선생님을 따라 교무실에 들어갔다."
    "질문이 있는 척, 노트와 연필을 들고 여러 선생님께 달려가 몰래 선생님 책상을 엿보았다."
    "여러 파일철이 주욱 정리되어 있었지만 대부분 생활기록부나 출석부, 성적표 등 공부와 전혀 관계없는 것들 뿐이었다."
    "과학 선생님의 책상에는 조금 흥미로워 보이는 두꺼운 책을 발견해서 선생님께 보여달라고 했지만, 교과서에서 배우는 내용이 엄청 어려운 말로 적혀 있었다."
    "공부를 열심히 한다고 옆 반 담임 선생님께서 사탕을 주셨지만, 별로 기쁘지는 않았다."
    "결국, 질문에 대한 대답을 받아적은 노트만을 들고 나는 터덜터덜 한별, 한설이와 만나기로 한 장소로 향했다."
    stop music fadeout 1.0
    jump scene300

label scene236:
    yeongwon "그러면 나는 원장실에 가볼게. 선생님께 부탁받았다고 하면 되지 않을까?"
    hanseol "나는 그럼... 교무실로 할게. 도서관처럼 책 냄새 나는 곳은 싫어..."
    hanbyeol "에휴. 그럼 나는 도서관이겠네. 너한테 부탁받아서 자료 검색이랑 복사 좀 하러 왔다고 할게."
    yeongwon "좋아, 그럼 각자의 역할도 결정된 거네?"
    yeongwon "그러면 오늘 각자 정해진 곳에 가 보기로 하자."
    hanseol "알았어!"

    hide yeongwon
    hide hanseol
    hide hanbyeol
    with dissolve

    "그리고 우리는 얘기하는 사이에 스테이크가 식어버린 것을 눈치채지 못했다."
    "함박스테이크를 잘라 입에 넣었다."
    "음, 이거 싸구려 배양육이 분명해. 웩."

    scene background schoolhallwaynight
    with Fade(0.4, 0.7, 0.4)

    "방과후."
    "가방을 주섬주섬 챙겨들고 선생님께 가서 결재서류 전달을 대신해드리겠다고 이야기했다."
    "선생님은 이전에 본 시험지 채점으로 많이 바쁘셨는지, 그래주면 고맙겠다고 말씀하셨다."
    "가방을 메고 원장실으로 향한다."
    "원장실에 도착하자, 원장 선생님이 두꺼운 서류철과 약병을 들고 서둘러 원장실을 나가고 계셨다."
    play sound "effect/beepbeep.ogg"
    "삐빅."
    "원장실 문고리를 잡아 비틀기 직전에 자동으로 문이 잠겨버렸다."

    show yeongwon shock with dissolve
    yeongwon "으으.. 조금만 더 빨랐으면..."

    "일단 결재 서류는 전달해 드려야 하고, 혹시 저 약병이 치료약일지도 모르니 조심스레 원장 선생님을 따라갔다."
    stop music fadeout 1.0
    scene ecg shou 2
    with Fade(0.4, 0.7, 0.4)
    play music "music/L39.mp3"
    "잠시 후, 원장 선생님이 도착한 곳은 그때의 오래된 실험실과 비슷한 느낌의, 아니, 거의 똑같은 실험실이었다."
    "자동문 사이로 안을 엿보던 나는 수술대에 누워 있는 둘을 보았다."
    "하나는... 하얗고 긴 머리의 여자아이."
    "그리고 다른 하나는... 하늘색 머리의 예쁘장한 아이..."
    "마치 하늘이 같은..."
    yeongwon "하늘아?!"

    "원장 선생님이 흰 머리의 여자아이에게 들고 온 약병에서 약을 꺼내서 주사한다."
    "얼마 지나지 않아, 흰 머리의 여자아이는 무척 괴로워하기 시작했고, 이윽고 피를 토하기 시작했다."
    "고통에 발버둥치는 그 아이를 보며 나는 올라오려는 구토를 손으로 억눌렀다."
    "더 이상 볼 수 없을 것 같다."

    "토할 것 같아..."

    "결국 실험실에서 눈을 돌리고, 그 자리에 주저앉는다."

    "미쳤어..."
    "저게 그 리포트에서 말했던 \"실험\"이란 말이야...?!"

    "눈물이 핑 돌았다."

    "삐이이이이."

    "끊임없이 지속되는 전자음에 화들짝 놀라 다시 실험실 안을 들여다봤다."
    "깨끗했던 실험실 바닥은 이미 피바다로 변해 있었고, 여자아이의 팔은 실험대 바깥으로 추욱 늘어져 움직이지 않았다."
    "원장선생님은 다시 약병을 꺼내들더니 하늘이 곁으로 갔다."
    "안돼, 하늘이만은 안 돼! 저런 꼴으로 죽게 할 수는 없어!"

    scene background black
    with dissolve

    "???" "학생, 더 이상은 안 돼."

    "갑자기 뒤에서 어떤 남성의 목소리가 들려왔다."
    "뒤를 돌아보려 하자, 그 남자가 커다란 천으로 눈, 코, 입을 막아냈다."
    "앞이 보이지 않아...!"

    yeongwon "읍... 읍읍...?!"
    "???" "이미 넌 너무 많은 걸 봤어."
    "???" "너희 넷이 만나도록 내버려두는 게 아니었는데 말이야."

    "조금씩 남자의 목소리가 멀어진다."
    "조금씩... 조금씩 정신이 아득해지는 것이 느껴진다."

    "???" "너는 이미 살아있는 것 자체가 리스크야."
    "???" "불화의 싹은 미리 잘라 버리는 게 좋겠지?"

    "도대체... 뭘... 하려는...?"
    "무슨 소리를... 하는 거지...?"

    "???" "괜찮아, 아프지는 않게 해줄게. 나도 사람이야?"
    "???" "그러려고 가져온 고성능 마취제거든."

    "나... 마취제에...?"
    "가슴팍에 무엇인가가 꽂히는 듯한 느낌."
    "아파... 아니, 아프지 않아...?"
    "뭔가 계속해서 흘러내린다."
    "아, 다시 뽑혔다."
    "어쩐지 가슴에서 액체가 뿜어져 나오는 듯한 느낌을 받으며"
    "나는 조금씩 눈을 감았다."
    "눈물 한 방울이 뺨을 타고 흘러내렸다."
    stop music fadeout 1.0
    scene end3
    with fade
    with Pause(5)
    return
