import random

# 输入主题
subject = str(input("请输入主题："))

# 论述
discuss = [
    '既然如此，',
    '那么，',
    '我认为，',
    '一般来说，',
    '总的来说，',
    '经过上述讨论，',
    '解决{主题}的问题，首先要找到抓手。 所以，',
    '每个人都不得不复盘这些问题。 在拉通对齐这种问题时，',
    '而这些问题并不是痛点，而我们需要聚焦的关键是，',
    '带着这些问题，我们来聚焦一下——{主题}，',
    '{主题}的抓手是什么？方法论又该如何寻找？',
    '{主题}的打法，到底是怎样的，而聚焦{主题}本身，又会沉淀出什么样的方法论？',
    '要想清楚，{主题}，到底是对标一种什么样的存在？',
    '{主题}，到底到底该如何落地？',
    '了解清楚{主题}到底存在于哪条赛道，是解决一切问题的痛点。',
    '打造业务和数据的闭环对{主题}的解决意义重大。',
    '我们都必须串联相关生态，去思考有关{主题}的问题。',
    '我们认为，找到抓手，形成方法论，{主题}则会迎刃而解。',
    '所谓{主题}，关键是{主题}如何才能赋能目标，进而反哺目标生态。'
]

# 前引语
introduction = ['流传着这样一句话', '有着这样的共识']

# 后引语
postscript = [
    '这不禁令我深思。',
    '带着这句话，我们还要更加慎重的去对齐这个问题：',
    '这让我明白了问题的抓手，',
    '这句话语虽然很短，但沉淀之后真的能发现痛点。',
    '也许这句话就是最好的答案。'
]

# 名人名言
famousRemark = [
    '互联网产品经理间{前引语}，如何强化认知，快速响应，是非常值得跟进的。{后引语}',
    '互联网研发人员间{前引语}，在细分领域找到抓手，形成方法论，才能对外输出，反哺生态。{后引语}',
    '互联网大厂管理人员间{前引语}，找到正确的赛道，选择正确的商业模式，才能将项目落地。{后引语}',
    '互联网从业者间{前引语}，只有适度倾斜资源，才能赋能整体业务。{后引语}',
    '互联网间{前引语}，好的产品要分析用户痛点，击穿用户心智。{后引语}',
    '互联网运营人员间{前引语}，做精细化运营，向目标发力，才能获得影响力。{后引语}'
]


# 实际使用的名人名言
# Famous Remark Actually Used
def FRAU():
    FR = famousRemark[random.randint(0, len(famousRemark) - 1)]
    FR = FR.replace("{前引语}", introduction[random.randint(0, len(introduction) - 1)])
    FR = FR.replace("{后引语}", postscript[random.randint(0, len(postscript) - 1)])
    return FR


# 实际使用的论述
# Discuss Actually Used
def DAU():
    D = discuss[random.randint(0, len(discuss) - 1)]
    D = D.replace("{主题}", subject)
    return D


def main():
    bullShit = str()
    while (len(bullShit) < 1500):
        i = random.randint(1, 100)
        if i < 5:
            bullShit += "\r\n"
        elif i < 20:
            bullShit += FRAU()
        else:
            bullShit += DAU()
    print(bullShit)


main()
