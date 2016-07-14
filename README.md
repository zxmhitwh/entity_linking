# entity-linking
---
实体链接(命名实体消歧)
---
目标: 针对document或者query中的名实体(name mention)确定其具体的含义
# candidate entity generation(候选实体生成)
1.getcanbywiki:使用维基百科API返回与输入字符串相似度高的entity
2.getcanbyRule: 采用基于搜索规则的方法生成候选实体集
3.getcanbyPrior：采用基于先验概率的方法生成候选实体集
# graph construction(实体图构建)
1.每两个候选实体之间构建关联对
2.使用DFS在DBpedia中探索关联对之间的路径
3.所有路径与实体构成graph
# candidate entity ranking(候选实体排名)
1.利用PageRank计算图节点(代表实体)的值
2.选择得分最高的作为该name mention对应的知识库中的链接实体
