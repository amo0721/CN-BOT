import asyncio, discord, setting, os, sys, random, datetime

client = discord.Client()
Setting = setting.Settings()
now = datetime.datetime.now()
afk = []

@client.event
async def on_ready():
     print("정상 작동중..." % ())
     print("Playing setting is sucessful." % ())

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="환영해요!", description = None, color=0x0000ff)
    embed.add_field(name="유저 닉네임 : " + (member.name), value="유저 아이디 : " + (member.id))
    await client.send_message(client.get_channel(Setting.welcome_channel), embed=embed)

@client.event
async def on_member_remove(member):
    embed = discord.Embed(title="잘가요...ㅜㅜ", color=0x00ff00)
    embed.add_field(name="유저 닉네임 : " + (member.name), value="유저 아이디 : " + (member.id))
    await client.send_message(client.get_channel(Setting.welcome_channel), embed=embed)

@client.event
async def on_message(message):
                id = message.author.id

                if message.author.id == Setting.bot_id:
                    return None

                if message.author.id == Setting.ban_user_id:
                    await client.send_message(message.channel, "당신은 봇관리자에 의해 차단된 유저입니다! \n 문의는 봇관리자 개인메세지로 주세요.\n Jenon{Xenon} 제논 [Melon™]")
                    await client.send_message(client.get_channel(Setting.err_loging_channel), "차단된 유저가 명령어 사용을 시도하였습니다.\n유저 이름 : %d\n유저 아이디 : %d\n사용 서버 : %d\nCN Bot Logger")
                
                if id in afk:
                    embed = discord.Embed(title="잠수 상태가 해제되었어요!", description=str(message.author.name) + "님께서 잠수 상태가 해제되셨습니다.", color=0x0000ff)
                    await client.send_message(message.channel, embed=embed)
                    afk.remove(id)

                if message.content.startswith('/잠수'):
                    learn = message.content.replace('/잠수', "")
                    a = datetime.datetime.today().year
                    b = datetime.datetime.today().month
                    c = datetime.datetime.today().day
                    d = datetime.datetime.today().hour
                    e = datetime.datetime.today().minute
                    afk.append(id)
                if learn == '':
                    embed = discord.Embed(title="잠수 시작!", color=0x00ff00)
                    embed.add_field(name=(message.author.name) + "님의 잠수 상태가 시작되었습니다!!!", value="잠수 시작 시간 : " + str(a) + "년" + str(b) + "월" + str(c) + "일" + str(d) + "시" + str(e) + "분")
                    await client.send_message(message.channel, embed=embed)
                else:
                    embed = discord.Embed(title="잠수 시작!", color=0x00ff00)
                    embed.add_field(name=(message.author.name) + "님의 잠수 상태가 시작되었습니다!!!", value="잠수 시작 시간 : " + str(a) + "년" + str(b) + "월" + str(c) + "일" + str(d) + "시" + str(e) + "분")
                    embed.add_field(name="사유", value=learn)
                    await client.send_message(message.channel, embed=embed)

                if message.content.startswith('/게임'):
                    if message.author.server_permissions.administrator:
                        learn = message.content.replace('/게임', "")
                        await client.change_presence(game=discord.Game(name=learn))
                        await client.send_message(message.channel, "봇의 게임을 변경하였습니다.")

                if message.content.startswith("/온라인"):
                    embed=discord.Embed(title="CN BOT 온라인 상황", description=None, color=0x00ff00)
                    embed.add_field(name="I'm online!", value="이 메세지가 발신되지 않으면 Offline 입니다.")
                    embed.add_field(name="요청자", value="<@" + str(message.author.name) + ">")
                    await client.send_message(message.channel, embed=embed)  
                
                if message.content.startswith("/초대"):
                    await client.send_message(message.channel, str(message.author.name)+" 죄송합니다.이 봇은 CN 전용 봇으로 초대할 수 없습니다.")

                if message.content.startswith("/상태"):
                    if message.author.id == Setting.owner_id:
                        embed = discord.Embed(title="CN Bot 서버 상태", color=0x00ff00)
                        embed.add_field(name="Owner id", value=Setting.owner_id, inline=True)
                        embed.add_field(name="classic log channel id", value=Setting.err_loging_channel, inline=True)
                        embed.add_field(name="Bot Notice Channel", value=Setting.notice_channel, inline=True)
                        embed.add_field(name="Welcome Channel", value=Setting.welcome_channel, inline=True)
                        embed.add_field(name="Ban User id", value=Setting.ban_user_id, inline=True)
                        await client.send_message(message.channel, embed=embed)
               
                if message.content.startswith('/도움말'):
                    a = datetime.datetime.today().year
                    b = datetime.datetime.today().month
                    c = datetime.datetime.today().day
                    d = datetime.datetime.today().hour
                    e = datetime.datetime.today().minute
                    f = datetime.datetime.today().second
                    embed=discord.Embed(title='`CN Bot 도움말 목록`', description=None, color=0xb2ebf4)
                    embed.add_field(name='`/온라인`', value='봇이 온라인인지 확인할 수 있습니다.', inline=False)
                    embed.add_field(name='`/도움말`', value='CN Bot 도움말을 출력합니다.', inline=False)
                    embed.add_field(name='`/초대`', value='CN Bot 초대링크를 출력하나, 이 봇은 BN 전용 봇으로 쓸모없는 커맨드((퍽퍽', inline=False)
                    embed.add_field(name='`/길드정보`', value='CN 길드정보를 출력합니다.', inline=False)
                    embed.add_field(name='`/규칙`', value="CN 서버 규칙을 출력합니다.", inline=False)
                    embed.add_field(name='`/서버정보`', value="서버 정보를 출력합니다.", inline=False)
                    embed.add_field(name='`/잠수`', value="잠수 상태에 돌입합니다.", inline=False)
                    embed.add_field(name='`인증`', value='처음 온 유저에게 인증이 필요합니다.그 인증 절차를 위한 명령어입니다.자동화는 추후 업데이트로 활성화시키겠습니다.', inline=False)
                    embed.add_field(name='`/관리자 소개`', value="CN Server | Guild의 관리자들을 소개합니다!!!(봉사위원 제외)")
                    embed.set_footer(text="관리자 명령어는 '/관리자 도움말' 입력! | " + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초")
                    await client.send_message(message.channel, embed=embed)

                if message.content.startswith('/관리자 도움말'):
                    embed=discord.Embed(title='`CN Bot 관리자 도움말 목록`', color=0x00ff00)
                    embed.add_field(name='/공지 [공지 분류] [내용]', value="공지 채널에 내용을 공지로 전송합니다.공지 분류는 긴급 패치 | 업데이트 | 일반 이 있습니다.")
                    embed.add_field(name='/기능 종료 [모듈이름]', value='해당 모듈을 종료합니다. 모듈에는 메인, 잠수, 공지, 로그 가 있습니다.')
                    embed.add_field(name='/게임 [게임내용]', value='플레이중 상태를 [게임내용]으로 변경합니다.')
                    await client.send_message(message.channel, embed=embed)
                
                if message.content.startswith("/길드정보"):
                    embed=discord.Embed(title="CN 길드정보", description=None, color=0x00ff00)
                    embed.add_field(name="CNN 길드는 하이픽셀 배드워즈 길드입니다.", value="CN 길드는 한국 배드워즈 랭킹 2위를 목표로 삼고있는 길드입니다.", inline=True)
                    embed.add_field(name="길드장 : _C*", value="길드 가입 많이많이 해주세요!")
                    await client.send_message(message.channel, embed=embed)

                if message.content.startswith("/규칙"):
                    embed=discord.Embed(title="CN Guild Community 규칙입니다.본 사항을 지켜주세요.", color=0x00ff00)
                    embed.add_field(name="1. 욕설 및 분쟁 유발, 저속한 단어들, 성드립&패드립 사용 금지", value="1-1. 상대방이 기분이 나쁘다고 판단할 정도가 기준입니다.")
                    embed.add_field(name="2. 명령어는 명령어 채널에서만 입력해 주세요.", value="모든 명령어는 <#576600326044647443>에서 입력해 주셔야 합니다.")
                    embed.add_field(name="3. 도배 금지-뮤트 5일[심하면 벤]", value="3-1. 할말이 있어서 장문을 입력하는 것이 아니면 10줄 이상 입력할 시 도배로 간주합니다.")
                    embed.add_field(name="4. 하이픽셀의 모든 규칙을 준수할 것", value="4-1. 핵, 욕설, 도배\n4-2. 핵인 것이 증명될 경우 벤처리 합니다.")
                    embed.add_field(name="5. 길드원은 길드 규칙을 준수할 것", value="<#576600589648003092>")
                    embed.add_field(name="6. 특정인 비하 혹은 언급 금지", value="이 경우 킥입니다.")
                    embed.add_field(name="7. 관리자 혹은 역할 구걸 금지", value="단, 역할 신청은 제외되며 타 채널 혹은 관리자 개인메세지로 관리자 역할 이상의 역할을 구걸할 경우 추방 제재를 가합니다.")
                    embed.add_field(name="8. 통화방에서 욕설, 혹은 성드립&패드립 비하 등등 금지", value="통화방에 2인 이상의 사람이 있을 경우 적용되는 규칙입니다.")
                    embed.add_field(name="9. Everyone 멘션 금지", value="모두에게 멘션이 가는 행동은 금지합니다.")
                    embed.add_field(name="10. 이 서버에서 계정판매 혹은 거래는 불가능합니다.", value="만약 구입자가 있을 경우 구입자까지 추방합니다.")
                    embed.add_field(name="11. 각 채널에서 목적에 맞지 않는 텍스트는 입력하지 말아주세요.", value="Ex)장난으로 질문답변방에 게임과 관련없는 질문을 한다.")
                    embed.add_field(name="12. 홍보 연속 3회 이상은 금지해 주세요!경고 1회 제재 처리합니다.", value="홍보는 홍보 채널에서만 가능하며 이외의 채널에서 디스코드 서버 초대가 보일 경우 즉시 추방하겠습니다.")
                    embed.add_field(name="기타로 서버에 해가 되는 행동은 처벌되며 경고 7회 누적시 30일 벤이라는 것을 명심해 주시기 바랍니다.", value="규칙은 계속 변경될 수 있습니다.")
                    await client.send_message(message.channel, embed=embed)

                if message.content.startswith("/서버정보"):
                    embed = discord.Embed(title="\"%s\" 서버정보!" % (message.server.name), description=None, color=0X00ff00)
                    embed.add_field(name="서버 소유자", value="<@%s>" % message.server.owner.id, inline=False)
                    embed.add_field(name="서버 생성일", value="%s (UTC)" % (message.server.created_at), inline=False)
                    embed.add_field(name="서버 보안등급", value=message.server.verification_level, inline=False)
                    embed.add_field(name="서버 위치", value=message.server.region, inline=False)
                    embed.add_field(name="서버 잠수채널", value="%s (%s분 이상 잠수이면 이동됨)" % (message.server.afk_channel, message.server.afk_timeout/60), inline=False)
                    embed.set_thumbnail(url=message.server.icon_url)
                    await client.send_message(message.channel, embed=embed)

                if message.content.startswith("/추방"):
                    if message.author.server_permissions.administrator:
                        learn = message.content.split(' ')
                        member = discord.utils.get(client.get_all_members(),id=learn[1])
                        await client.kick(member)
                        await client.send_message(message.channel, "추방 완료!")
        
                if message.content.startswith("/벤"):
                    if message.author.server_permissions.administrator:
                        learn = message.content.split(' ')
                        member = discord.utils.get(client.get_all_members(),id=learn[1])
                        await client.ban(member, 1)
                        await client.send_message(message.channel, "추방 완료!")

                if message.content.startswith('/종료'):
                    embed = discord.Embed(title="봇이 종료됨.", color=0xff0000)
                    embed.add_field(name="봇이 종료되었습니다.", value="요청자 : " + str(message.author.name))
                    await client.send_message(client.get_channel(Setting.err_loging_channel), embed=embed)
                    embed = discord.Embed(title="This Bot is turn off.", color=0xff0000)
                    embed.add_field(name="This Bot is turned off.", value="message author : " + str(message.author.name))
                    await client.send_message(client.get_channel(Setting.err_loging_channel), embed=embed)
                    quit()

                if message.content.startswith('/관리자 소개'):
                    embed = discord.Embed(title="CN의 관리자들을 소개합니다!", color=0xff0000)
                    embed.add_field(name="_C*", value="학급 회장")
                    embed.add_field(name="김비서 Rick_Moo", value="반장")
                    embed.add_field(name="내 밑 댕청 김비서 (Gambeul)", value="반장")
                    embed.add_field(name="Jenon C (제논) [Melon™] & Jenon P (제논) [Melon™]", value="부반장")
                    embed.add_field(name="네온(InNeon)", value="부반장")
                    embed.add_field(name="블루베어", value="부반장")
                    embed.set_footer(text="CN Project Bot : CN Guild Bot | 똥개")
                    await client.send_message(message.channel, embed=embed)

                if "/" in message.content:
                    a = datetime.datetime.today().year
                    b = datetime.datetime.today().month
                    c = datetime.datetime.today().day
                    d = datetime.datetime.today().hour
                    e = datetime.datetime.today().minute
                    f = datetime.datetime.today().second
                    embed=discord.Embed(title="CN Bot Command log", description=str(message.author.name), color=0x0000ff)
                    embed.add_field(name="메세지 내용", value=(message.content))
                    embed.add_field(name="메세지 채널", value="<#" + str(message.channel.id) + ">")
                    embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초에 발신됨.")
                    await client.send_message(client.get_channel(Setting.err_loging_channel), embed=embed)

                if message.content.startswith("/공지 긴급패치"):
                    learn = message.content.replace('/공지 긴급패치', "")
                    if message.author.server_permissions.administrator:
                        a = datetime.datetime.today().year
                        b = datetime.datetime.today().month
                        c = datetime.datetime.today().day
                        d = datetime.datetime.today().hour
                        e = datetime.datetime.today().minute
                        f = datetime.datetime.today().second
                        g = message.author.name
                        embed = discord.Embed(title=str(g) + "님의 긴급패치 공지", color=0x00ff00)
                        embed.add_field(name=learn, value="Module by Mary")
                        embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 | 발신자 : " + str(message.author.name))
                        await client.send_message(client.get_channel(Setting.notice_channel), embed=embed)
                        await client.send_message(message.channel, "완료!")
    
                if message.content.startswith("/공지 업데이트"):
                    learn = message.content.replace('/공지 업데이트', "")
                    if message.author.server_permissions.administrator:
                        a = datetime.datetime.today().year
                        b = datetime.datetime.today().month
                        c = datetime.datetime.today().day
                        d = datetime.datetime.today().hour
                        e = datetime.datetime.today().minute
                        f = datetime.datetime.today().second
                        g = message.author.name
                        embed = discord.Embed(title=str(g) + "님의 봇 업데이트 공지", color=0x00ff00)
                        embed.add_field(name=learn, value="Module by Mary")
                        embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 | 발신자 : " + str(message.author.name))
                        await client.send_message(client.get_channel(Setting.notice_channel), embed=embed)
                        await client.send_message(message.channel, "완료!")

                if message.content.startswith("/공지 일반"):
                    learn = message.content.replace('/공지 일반', "")
                    if message.author.server_permissions.administrator:
                        a = datetime.datetime.today().year
                        b = datetime.datetime.today().month
                        c = datetime.datetime.today().day
                        d = datetime.datetime.today().hour
                        e = datetime.datetime.today().minute
                        f = datetime.datetime.today().second
                        g = message.author.name
                        embed = discord.Embed(title=str(g) + "님의 공지", color=0x00ff00)
                        embed.add_field(name=learn, value="Module by Mary")
                        embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 | 발신자 : " + str(message.author.name))
                        await client.send_message(client.get_channel(Setting.notice_channel), embed=embed)
                        await client.send_message(message.channel, "완료!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
