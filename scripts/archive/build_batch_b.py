#!/usr/bin/env python3
"""Build batch_b.json with translations for all 10 files."""

import json, re

def get_blocks(filename):
    with open(f'prompts/{filename}.json') as fh:
        data = json.load(fh)
    user = data['user']
    blocks = re.findall(r'\[block_\d+\].*?(?=\[block_\d+\]|\Z)', user, re.DOTALL)
    result = []
    for b in blocks:
        m = re.match(r'\[block_\d+\]\s*\S+:\s*(.*)', b, re.DOTALL)
        result.append(m.group(1).strip() if m else '')
    return result

# ============================================================
# TRANSLATIONS
# ============================================================

translations = {}

# --- topology_complex_plane.html (45 blocks) ---
t = []
t.append('[[i class="fa-solid fa-list"]][[/i]]目录')
# block_1
t.append('[[a href="#section1"]]邻域[[/a]]')
# block_2
t.append('[[a href="#section2"]]点的分类[[/a]]')
# block_3
t.append('[[a href="#section3"]]拓扑空间[[/a]]')
# block_4
t.append('复平面的拓扑')
# block_5
t.append('邻域')
# block_6
t.append("""\
                    复数 @@math:15:d94de1@@ 的一个 @@math:14:f9054e@@ [[em id="neighborhood"]]邻域[[/em]]，也称为\
                    [[em]]开球[[/em]]或[[em]]开圆盘[[/em]]，由所有满足条件的点\
                    @@math:16:31677c@@ 组成，这些点位于以 @@math:17:eb32bb@@ 为圆心、半径为\
                    @@math:18:9a6bbd@@ 的圆内部（不在圆周上），其表达式为\
                <div class="scroll-wrapper">\
                    @@math:6:4f2ca3@@\
                </div>\
                @@math:20:fa8ea6@@ 的[[em id="closed-neighborhood"]]闭[[/em]] @@math:19:1d270b@@ [[em]]邻域[[/em]]\
                表示为\
                <div class="scroll-wrapper">\
                    @@math:7:fd6df4@@\
                </div>\
                最后，@@math:22:3beae2@@ 的[[em id="deleted-neighborhood"]]去心[[/em]] @@math:21:6a73b3@@ [[em]]邻域[[/em]]，\
                也称为[[em]]去心球或去心圆盘[[/em]]，表示为\
                <div class="scroll-wrapper">\
                    @@math:8:17700b@@\
                </div>\
                图 1 展示了以下例子的几何表示：\
                """)
# block_7
t.append('@@math:23:8b28ca@@')
# block_8
t.append(""" $\\overline{B}_{\\frac{7}{8}}\\left(-1-\\sqrt{2}i\\right)=\\left\\{z:|z-\\left(-1-\\sqrt{2}i\\right)|\\leq\
                            \\frac{7}{8}\\right\\}$""")
# block_9
t.append(""" $\\overline{B}_{\\frac{1}{2}}\\left(2+\\sqrt{3}i\\right)\\setminus\\left\\{2+\\sqrt{3}i\\right\\}=\\left\\{z:0<|z-\\left(2+\\sqrt{3}i\\right)|\\leq\
                            \\frac{1}{2}\\right\\}$""")
# block_10
t.append('邻域的几何表示。')
# block_11
t.append('点的分类')
# block_12
t.append("""\
                    点 @@math:24:3afaaf@@ 称为集合 @@math:25:f281af@@ 的[[em id="interior-point"]]内点[[/em]]，如果存在 @@math:26:5306e0@@ 的一个邻域\
                    包含于 @@math:27:dbff5b@@ 中。\
                    点 @@math:28:356710@@ 称为集合 @@math:29:106c23@@ 的[[em id="exterior-point"]]外点[[/em]]，如果存在 @@math:30:d6b7b6@@ 的一个邻域\
                    与 @@math:31:f4662e@@ 不相交。\
                    如果 @@math:32:c9fdf7@@ 既不是 @@math:33:cf6d84@@ 的内点也不是外点，则称其为[[em id="boundary-point"]]边界点[[/em]]。\
                    @@math:34:2b0a4e@@ 的所有边界点的集合记为 @@math:9:2cefb6@@\
                """)
# block_13
t.append('本文中将使用以下记号：')
# block_14
t.append('@@math:35:f6b95c@@')
# block_15
t.append('@@math:36:46fd45@@')
# block_16
t.append('@@math:37:c6438d@@')
# block_17
t.append('集合 @@math:38:e66175@@ 的内部、边界和外部。')
# block_18
t.append("""\
                    考虑前面的邻域例子，令\
                    @@math:39:b540cd@@\
                    @@math:40:652f66@@\
                    那么：\
                """)
# block_19
t.append('对于 @@math:43:35d97c@@，有：')
# block_20
t.append('@@math:44:657900@@')
# block_21
t.append('@@math:45:2d8069@@')
# block_22
t.append('@@math:46:53fa29@@')
# block_23
t.append('最后，对于 @@math:47:976684@@，有：')
# block_24
t.append('@@math:48:ac77d2@@')
# block_25
t.append('@@math:49:0dca75@@')
# block_26
t.append('@@math:50:58e58d@@')
# block_27
t.append('拓扑空间')
# block_28
t.append("""\
@@verbatim:2:04c3c8@@

                    集合 @@math:51:629e42@@ 称为[[em id="open-set"]]开集[[/em]]，如果对于每个 @@math:52:068206@@ 都存在一个 @@math:53:0e4acd@@ 的邻域\
                    完全包含于 @@math:54:6b7b24@@ 中。\
                    集合 @@math:55:f55ad7@@ 称为[[em]]闭集[[/em]]，如果它在 @@math:56:a63957@@ 中的补集是开集。\
                """)
# block_29
t.append("""\
                    集合 @@math:57:6add98@@ 连同其子集的收集 @@math:58:5f75bc@@ 构成一个[[em]]拓扑空间[[/em]]，如果满足以下条件：\
                    [[br]]\
                    - @@math:59:0be592@@ 和 @@math:60:3e48d5@@ 属于 @@math:61:3ac40b@@\
                    [[br]]\
                    - @@math:62:fe6c44@@ 中任意多个集合的并集仍在 @@math:63:87cf54@@ 中。\
                    [[br]]\
                    - @@math:64:919343@@ 中有限多个集合的交集仍在 @@math:65:8eb2fd@@ 中。\
                """)
# block_30
t.append("""\
[[strong]]注：[[/strong]] 拓扑空间的技术定义有点超出本文的范围。\
                    然而，需要指出的是集合 @@math:66:dbaca9@@ 的收集满足上述所有三个条件，\
                    因此 @@math:10:ff76ff@@ 是一个拓扑空间。\
                """)
# block_31
t.append("""\
                    集合 @@math:67:54a21e@@ 的[[em id="closure"]]闭包[[/em]]是包含 @@math:68:25de6b@@ 的所有闭集的交集，\
                    记为 @@math:11:2c5f96@@ 因此，@@math:69:67a2ce@@ 是包含 @@math:70:cf4144@@ 的最小闭集。\
                """)
# block_32
t.append("""\
                    一般来说，如果一个集合不能表示为两个不相交的非空开子集的并集，则称其为连通的。\
                    在复平面中，一个开集是连通的当且仅当其中任意两点都可以用完全位于该集合内的折线连接。\
                """)
# block_33
t.append('多边形连通的开集。')
# block_34
t.append('例如，注意开集 @@math:76:ad8636@@ 是连通的，因为其内部任意两点都可以用一条折线连接。')
# block_35
t.append('@@math:78:d0d8f6@@')
# block_36
t.append('@@math:79:ccd694@@')
# block_37
t.append("""\
                    一个非空且连通的开集称为[[em]]区域[[/em]]。\
                    可将其视为由内部点组成且任意两点可用折线连接的集合。\
                """)
# block_38
t.append('有界集。')
# block_39
t.append("""\
[[strong]]练习：[[/strong]] 在复平面中画出集合 @@math:82:5ae38f@@\
                    并指出其中的点 @@math:12:1bd642@@\
                """)
# block_40
t.append('@@math:83:ee673d@@')
# block_41
t.append('@@math:84:7c006f@@')
# block_42
t.append('@@math:85:634f44@@')
# block_43
t.append('@@math:86:6608e6@@')
# block_44
t.append('复变函数 [[i class="fa-solid fa-angles-right"]][[/i]]')
translations['topology_complex_plane.html'] = t

# --- classification_of_singularities.html (41 blocks) ---
t = []
t.append('[[i class="fa-solid fa-list"]][[/i]]目录')
t.append('[[a href="#section1"]]分类[[/a]]')
t.append('[[a href="#section2"]]极点[[/a]]')
t.append('[[a href="#section3"]]可去奇点[[/a]]')
t.append('[[a href="#section4"]]本性奇点[[/a]]')
t.append('[[a href="#section5"]]最后说明[[/a]]')
t.append('奇点的分类')
t.append("""\
                    [[a href="laurent_series.html#laurent-series-theorem"]]洛朗级数[[/a]]中\
                    涉及 @@math:16:e67a88@@ 的负幂次的部分\
                    @@math:4:508637@@\
                    称为 @@math:17:39cfee@@ 在 @@math:18:d63b4a@@ 处的\
                    [[a href="laurent_series.html#principal-part"]][[em]]主要部分[[/em]][[/a]]。\
                    方程 (\\ref{principal}) 中的系数 @@math:19:10b92b@@ 在复分析中起着非常特殊的作用。\
                    它有一个特殊的名称：函数 @@math:20:c17057@@ 的[[em]]留数[[/em]]。\
                    本节将重点讨论主要部分，以将孤立奇点 @@math:21:32dc1c@@ 识别为三种特殊类型之一。\
                """)
t.append('极点')
t.append("""\
                    如果 @@math:22:7dc7a1@@ 在 @@math:23:1a8ca3@@ 处的主要部分至少包含一个非零项，但这样的项的数量是有限的，\
                    则存在整数 @@math:24:f421c4@@ 使得\
                    @@math:11:8384c8@@\
                    在这种情况下，孤立奇点 @@math:25:72f8fb@@ 称为[[em]]@@math:26:a60506@@ 阶极点[[/em]]。\
                    一阶极点通常简称为[[em]]简单极点[[/em]]。\
                """)
t.append('例子')
t.append("""\
                    考虑函数\
                    <div class="scroll-wrapper">\
                        @@math:12:e1d0f5@@\
                    </div>\
                    其中 @@math:28:c551d7@@ 是整数。还考虑函数\
                    <div class="scroll-wrapper">\
                        @@math:13:af2ba1@@\
                    </div>\
                """)
t.append('@@math:31:ecc44a@@')
t.append('@@math:32:52eb97@@')
t.append('@@math:33:7189c0@@')
t.append("""\
                    现在从 [[a href="domain_coloring.html#enhanced-phase-portraits"]]增强相位图[[/a]]可以看出，\
                    @@math:34:72f7ae@@ 是奇点。特别地，@@math:35:d700c0@@ 是 @@math:36:53055e@@ 阶极点，\
                    @@math:37:ac524d@@ 是 @@math:38:c08553@@ 阶极点，而 @@math:39:f8fcad@@ 不是孤立奇点。\
                    在图 2 中 @@math:40:2be3c5@@，我们可以看到零点（所有颜色交汇处）和极点（也是所有颜色交汇处，但颜色顺序相反）。\
                """)
t.append('可去奇点')
t.append("""\
                    当每个 @@math:42:fd0c6f@@ 都为零时，使得\
                    @@math:43:757262@@\
                    在 @@math:44:20c140@@ 处的主要部分为零，那么孤立奇点 @@math:45:1b48ad@@ 称为[[em]]可去奇点[[/em]]。\
                    在这种情况下，洛朗级数中的每个 @@math:46:f19f98@@ 都为零，从而洛朗级数就是泰勒级数。\
                """)
t.append('例子')
t.append("""\
                    考虑函数\
                    <div class="scroll-wrapper">\
                        @@math:16:1cfce7@@\
                    </div>\
                    和\
                    <div class="scroll-wrapper">\
                        @@math:17:90eade@@\
                    </div>\
                """)
t.append('@@math:53:5cd69d@@')
t.append('@@math:54:f11d3b@@')
t.append('@@math:55:9acc4e@@')
t.append("""\
                    注意到 @@math:56:0199b7@@ 在 @@math:57:ae5a20@@ 处有一个奇点，但从图 4 来看，\
                    这个奇点似乎是可去的。可以很容易地在 @@math:58:083221@@ 处重新定义函数，使得 @@math:59:1ed736@@\
                """)
t.append("""\
                    这个断言可以很容易地从洛朗级数表示中确认：\
                    @@math:60:ceb949@@\
                    在这种情况下，当 @@math:62:d78fba@@ 时，@@math:61:663afd@@ 的值趋近于 @@math:63:34e92a@@\
                """)
t.append('[[strong]]练习 1：[[/strong]] 求 @@math:65:742458@@ 在 @@math:66:e23d02@@ 处的洛朗级数展开。')
t.append('本性奇点')
t.append("""\
                    如果有无穷多个系数 @@math:67:d08131@@ 非零，则 @@math:68:5eedf6@@ 称为 @@math:69:ba150f@@ 的[[em]]本性奇点[[/em]]。\
                """)
t.append('例子')
t.append('函数 @@math:14:9447e6@@ 在 @@math:70:888a6a@@ 处有一个本性奇点。')
t.append("""\
                    图 7 展示了 @@math:71:92f53f@@ 在区域 @@math:72:3ad9a6@@ 中的增强相位图。\
                    在原点附近，我们看到颜色以复杂的方式变化，表明该函数的行为非常复杂。\
                """)
t.append('@@math:76:7bc7e3@@ 定义在 @@math:77:13b518@@ 上。')
t.append("""\
                    事实上，@@math:78:5e0227@@ 的一个邻域与函数 @@math:79:3f599a@@ 的值域相交无穷多次（Picard 定理），\
                    这表明本性奇点附近的行为是非常奇特的。\
                """)
t.append('简单相位图：本性奇点的近距离观察。')
t.append('另一个在原点处有本性奇点的例子是函数 @@math:82:ce1850@@')
t.append('@@math:83:aae489@@')
t.append('[[strong]]练习 2：[[/strong]] 求 @@math:85:9b1961@@ 在 @@math:86:0fe0cd@@ 处的洛朗级数展开。')
t.append('最后说明')
t.append("""\
                    相位图对于理解函数在其奇点附近的行为非常有用。\
                    特别是当与模的等值线结合使用时，增强相位图为可去奇点、极点和本性奇点提供了清晰的视觉区分。\
                    然而，值得注意的是，仅靠相位图可能不足以完全确定奇点的类型。\
                    例如，函数 @@math:87:34265f@@ 看起来在原点处有一个简单极点，\
                    但实际上它有 @@math:18:5b6c10@@ 阶极点。这就是为什么在可能的情况下，将相位图与模的等值线结合起来使用更好的原因。\
                """)
t.append('@@math:88:fda6d8@@ 其中 @@math:89:e9bd97@@')
t.append('Mandelbrot 集合 [[i class="fa-solid fa-angles-right"]][[/i]]')
translations['classification_of_singularities.html'] = t

# --- complex_differentiation.html (41 blocks) ---
t = []
t.append('[[i class="fa-solid fa-list"]][[/i]]目录')
t.append('[[a href="#section1"]]复微分[[/a]]')
t.append('[[a href="#section2"]]柯西-黎曼方程[[/a]]')
t.append('[[a href="#section3"]]充分条件[[/a]]')
t.append('[[a href="#section4"]]解析函数[[/a]]')
t.append('复微分')
t.append("""\
                    复导数的概念是复变函数理论的基础。\
                    复导数的定义与实函数的导数类似。\
                    然而，尽管表面上相似，复微分却是一个深刻不同的理论。\
                """)
t.append("""\
                    复变函数 @@math:44:0644b0@@ 在点 @@math:45:16cd0b@@ 处[[em]]可微[[/em]]，当且仅当以下极限差商存在\
                <div class="scroll-wrapper">\
                    @@math:5:0e3cae@@\
                </div>\
                """)
t.append("""\
                    或者，令 @@math:46:e83cce@@，可以写成\
                <div class="scroll-wrapper">\
                    @@math:6:bf2a8f@@\
                </div>\
                """)
t.append("""\
                    通常省略 @@math:47:4387ce@@ 的下标，并引入数\
                    @@math:48:d61db8@@\
                    它表示值 @@math:49:9c6794@@ 的变化，对应于 @@math:51:e5ebf2@@ 的求值点改变了 @@math:50:283ebd@@。\
                    那么方程 (\\ref{diff02}) 可以写成\
                    @@math:52:c0b21a@@\
                """)
t.append("""\
                    尽管导数公式 (\\ref{diff01}) 在形式上与实值函数的导数公式相同，但一个关键的区别是\
                    @@math:53:a4e52d@@ 可以沿着无穷多种方向趋近于 @@math:54:f46e2a@@，如\
                    图 1 所示。\
                """)
t.append('趋近 @@math:56:0dbc75@@ 的方向有无穷多种。')
t.append("""\
                    复微分的一个显著特点是，可微函数在某一点处的导数存在\
                    对所有趋近方向都施加了限制。事实上，在某个点处满足柯西-黎曼方程是可微的必要条件。\
                """)
t.append('柯西-黎曼方程')
t.append("""\
                    现在来看看定义 (\\ref{diff01}) 的一个显著推论。\
                    首先设 @@math:57:965efd@@ 趋近于 @@math:58:bc00b5@@ 沿着水平线的方向。这意味着\
                    @@math:59:b76baa@@ 且 @@math:60:46c0b5@@\
                    那么 @@math:61:8146e4@@，导数变为\
                    @@math:7:0ac47e@@\
                    另一方面，如果 @@math:62:18cdd0@@ 趋近于 @@math:63:fdc6fe@@ 沿着垂直线方向，则\
                    @@math:64:0a874f@@ 且 @@math:65:2663b1@@\
                    那么导数变为\
                    @@math:8:00c46b@@\
                    如果导数 @@math:66:f3c76e@@ 存在，则这两个极限必须重合。因此，令实部和虚部相等，得到著名的[[em]]柯西-黎曼方程[[/em]]：\
                    @@math:9:8cc3b8@@\
                    这个结果可以形式化为以下定理：\
                    <div class="theorem" id="cauchy-riemann-equations">\
                        @@math:10:efbc33@@\
                    </div>\
                """)
t.append("""\
[[strong]]例 1：[[/strong]] 考虑函数 @@math:72:cf3b13@@ 验证 @@math:73:ba2e68@@ 在 @@math:74:0c283b@@ 处可微，但在任何其他点都不可微。\
                """)
t.append("""\
                    幸运的是，复导数具有通常的所有求导法则，这些法则在实分析中已经确立。例如：\
                    @@math:77:64996b@@\
                """)
t.append("""\
                    等等。在这种情况下，幂 @@math:87:f043b0@@ 可以是复数，\
                    因此该函数实际上是多值的。在接下来的章节中，将讨论处理这类函数所需的工具。\
                """)
t.append("""\
                    如果 @@math:90:e6d761@@ 和 @@math:91:e7fdf6@@ 的偏导数在 @@math:92:5c5fb1@@ 处连续，且满足柯西-黎曼方程，\
                    则 @@math:93:d1acea@@ 在 @@math:94:b1ef62@@ 处可微。\
                """)
t.append('可微的充分条件')
t.append("""\
                    在点 @@math:95:e42dce@@ 处满足柯西-黎曼方程本身并不足以保证在该点处可微。\
                    还需要偏导数在该点处连续。然而，如果偏导数存在且连续，并且满足柯西-黎曼方程，则可微性得以保证。\
                """)
t.append("""\
[[strong]]例 2：[[/strong]] 考虑指数函数\
                    @@math:99:e2c7d0@@\
                    由于 @@math:100:1396b7@@ 可以写成\
                    @@math:101:2a38e4@@\
                    那么\
                    @@math:102:52cb56@@\
                    因此，@@math:103:27a808@@ 和 @@math:104:2c2fb8@@ 的偏导数处处存在且连续，并且满足柯西-黎曼方程。\
                    因此 @@math:105:43bac8@@ 在复平面上的每一点都可微。\
                """)
t.append("""\
                    由于 @@math:116:d8ad46@@ 和 @@math:117:872260@@ 的偏导数处处连续，且满足柯西-黎曼方程，\
                    因此 @@math:118:c481f8@@ 是处处可微的。此外，\
                    @@math:11:198128@@\
                """)
t.append('注意 @@math:119:1c8a9b@@ 对所有 @@math:120:a592b4@@ 成立。')
t.append("""\
                    柯西-黎曼条件的一个推论是，可微函数的水平曲线 @@math:127:0cf38a@@ 和 @@math:128:1b52ec@@ 是[[em]]正交的[[/em]]。\
                    也就是说，通过取 @@math:129:633fdd@@ 和 @@math:130:15ad4d@@ 的梯度的点积，可以看到\
                    @@math:12:8eb584@@\
                    因此，只要 @@math:13:96a2c0@@ 非零，水平曲线 @@math:131:a6609b@@ 和 @@math:132:adfe39@@ 就是正交的。\
                """)
t.append('因此，可微函数的二维水平曲线 @@math:131:a6609b@@ 和 @@math:132:adfe39@@ 是正交的。')
t.append("""\
[[strong]]例 3：[[/strong]] 对于函数 @@math:133:20223f@@，我们有\
                    @@math:134:ffce4a@@\
                    因此水平曲线 @@math:135:ad23db@@ 和 @@math:136:e2e2fd@@ 是正交的，如图 2 所示。\
                """)
t.append('实部和虚部分量的正交水平曲线。')
t.append('解析函数')
t.append("""\
                    设 @@math:137:58b552@@ 其中 @@math:138:979807@@ 是一个开集。如果 @@math:139:b97ae0@@ 在 @@math:140:b1c8ea@@ 的每一点都可微，\
                    则称 @@math:141:5964c2@@ 在 @@math:142:0c6ce9@@ 上[[em]]解析[[/em]]。\
                    如果 @@math:143:e9594c@@ 在 @@math:144:73f38e@@ 的某个邻域中的每一点都可微，则称 @@math:14:4c7394@@ 在 @@math:15:65dec2@@ 处解析。\
                """)
t.append('[[strong]]整函数[[/strong]]是在整个复平面上解析的函数。')
t.append('如果函数 @@math:145:4d69f6@@ 在点 @@math:146:734717@@ 处不解析，但在 @@math:147:d1a735@@ 的每个邻域中至少存在一个解析点，则称 @@math:148:4c5811@@ 为 @@math:149:227fea@@ 的[[em]]奇点[[/em]]。')
t.append("""\
[[strong]]例 4：[[/strong]]\
                        函数 @@math:150:53f23b@@ 在除 @@math:16:dc263c@@ 外的每一点都解析。\
                """)
t.append('点 @@math:151:23a965@@ 显然是 @@math:152:e5cb65@@ 的一个奇点。')
t.append("""\
                    如果两个函数在一个区域 @@math:153:3ed0c6@@ 上解析，则它们的和、积和商（分母非零）在 @@math:154:4f32e7@@ 上也解析。\
                    同样地，如果一个函数在区域 @@math:155:5ae2ba@@ 上解析，则其复合在 @@math:156:ab4ff1@@ 上也解析。\
                """)
t.append("""\
                    此外，由导数的链式法则，\
                    解析函数的复合函数也是解析的。\
                """)
t.append("""\
[[strong]]例 5：[[/strong]]\
                        多项式函数\
                        @@math:157:5faf2d@@\
                        在整平个面上都是解析的。\
                """)
t.append('当一个函数由其分量函数给出时，可以通过验证柯西-黎曼方程和偏导数的连续性来验证其解析性。')
t.append("""\
[[strong]]例 6：[[/strong]]\
                        函数\
                        @@math:158:bfa20e@@\
                        在 @@math:159:3c8c7f@@ 处解析，\
                        因为 @@math:160:92f2c2@@ 的分量函数是连续的且满足柯西-黎曼方程。\
                """)
t.append('后面会用到的另一个有用性质如下：')
t.append('对数函数 [[i class="fa-solid fa-angles-right"]][[/i]]')
translations['complex_differentiation.html'] = t

# --- cauchy_integral_formula.html (33 blocks) ---
t = []
t.append('柯西积分公式')
t.append("""\
        如果 @@math:19:0b7972@@ 在单连通区域 @@math:20:9f8227@@ 上解析且\
        @@math:21:e2c2e3@@，则商 @@math:22:ef67e7@@\
        在 @@math:23:190de4@@ 处无定义，因而在 @@math:24:d9ed2a@@ 中非解析。\
        因此，柯西-Goursat 定理不允许\
        得出积分\
        @@math:25:8e87e3@@\
        沿包含 @@math:27:d6e39a@@ 的简单闭曲线 @@math:26:9bbd4c@@ 为零的结论。\
        然而，将会看到，这个积分的值为 @@math:28:baee5c@@。这个结果是两个卓越公式中的第一个。\
      """)
t.append("""\
            曲线 @@math:43:a950ff@@ 内部的圆 @@math:42:7ae5ac@@\
          """)
t.append("""\
          我们希望证明右侧积分的值为 @@math:44:c4d2d4@@。为此，在被积函数的分子中加上和减去\
          常数 @@math:45:852f14@@\
        """)
t.append("""\
          已知 @@math:46:7976ec@@（参见 [[a href="cauchy_goursat_theorem.html"]]柯西-Goursat 定理[[/a]] 部分的 [[strong]]练习 1[[/strong]]），因此\
          (\\ref{formula-01}) 变为\
        """)
t.append("""\
          现在，@@math:47:26cad3@@ 在 @@math:48:3d28a0@@ 处解析（因而连续）\
          这一事实保证了对每个 @@math:49:fccb65@@\
          存在 @@math:50:277aa2@@ 使得\
        """)
t.append("""\
          选择圆 @@math:52:dd35ab@@ 的半径 @@math:51:92b41c@@ 小于第二个不等式中的数\
          @@math:53:601a5c@@。由于\
          当 @@math:55:056186@@ 在 @@math:56:019ca4@@ 上时 @@math:54:9bfd4b@@，因此\
          当 @@math:55:056186@@ 在 @@math:56:019ca4@@ 上时，(\\ref{formula-03}) 中的第一个不等式成立。\
        """)
t.append('因此，由方程 (\\ref{formula-02})，有')
t.append("""\
          由于这个不等式的左边是一个非负常数（不依赖于 @@math:57:513403@@），\
          而 @@math:58:faf41b@@ 可以取任意小，因此左边必须为零。这就得到了柯西积分公式。\
        """)
t.append("""\
[[strong]]例 1：[[/strong]]\
          设 @@math:59:2da8b6@@ 计算积分\
          @@math:60:810f25@@\
          其中 @@math:61:43ebc2@@ 是如图 3 所示的曲线。\
        """)
t.append('曲线 @@math:67:381ef5@@ 激活复选框 [[code]]Phase portrait[[/code]] 以观察被积函数。')
t.append("""\
[[strong]]练习 1：[[/strong]]\
          证明 @@math:68:7d3b94@@\
        """)
t.append('柯西积分公式的推广')
t.append("""\
        [[strong]]定理 1[[/strong]] 中的柯西积分公式可以推广到导数的积分表示。\
        如果 @@math:69:69db8e@@ 在单连通区域 @@math:70:58dd58@@ 上解析且\
        @@math:71:b6e8e5@@，那么 @@math:72:6955c0@@ 的所有阶导数都在 @@math:73:bd0ec5@@ 上解析，\
        并且其导数可以由下式给出\
        @@math:74:a52233@@\
      """)
t.append("""\
[[strong]]练习 2：[[/strong]]\
          用导数的形式定义来证明公式 (\\ref{general-derivative})。\
        """)
t.append('注意可以写成')
t.append('也可以利用 @@math:84:99f917@@ 在 @@math:85:56de90@@ 上连续的事实。')
t.append('一般来说，可以用归纳法得到第二个卓越公式：')
t.append('可以改写为')
t.append('验证 (\\ref{general-derivative}) 比验证原公式更复杂，但思路是类似的。')
t.append("""\
[[strong]]例 2：[[/strong]]\
          计算\
          @@math:90:5ed569@@\
          其中 @@math:91:5238cb@@ 是如图所示的曲线。\
        """)
t.append('注意被积函数在 @@math:94:84efa7@@ 处非解析。')
t.append('曲线 @@math:97:4c4c2c@@ 激活复选框 [[code]]Phase portrait[[/code]] 以观察被积函数。')
t.append("""\
        将被积函数改写为\
          @@math:99:690142@@\
          注意到 @@math:100:10d9d8@@ 在 @@math:101:ab92fb@@ 围成的区域上解析，\
          因此由广义柯西积分公式，有\
          @@math:102:a3019c@@\
        """)
t.append("""\
[[strong]]练习 3：[[/strong]]\
          设 @@math:105:3049e3@@ 计算积分\
          @@math:106:5f6af4@@\
        """)
t.append('推广的一些推论')
t.append('推广的一个直接且卓越的推论是：如果一个复变函数在某个点处解析，则它在该点处无穷可微。')
t.append("""\
          可以对解析函数 @@math:112:bd61b1@@ 应用类似的论证，\
          得出该函数的所有导数都存在且连续。\
        """)
t.append("""\
          因此，当函数 @@math:129:14e055@@\
          在点 @@math:130:11626b@@ 处解析时，其所有导数 @@math:131:db5235@@ 都存在且连续。\
          这比实分析中的情况要强得多，在实分析中，函数的可微性并不能保证其导数甚至存在（更不用说连续了）。\
        """)
t.append('')
t.append('最后，柯西积分公式的另一个推论是柯西不等式：')
t.append('因此，由 (\\ref{general-derivative}) 和 ML 不等式，')
t.append('代数基本定理[[i class="fa-solid fa-angles-right"]][[/i]]')
translations['cauchy_integral_formula.html'] = t

# --- mandelbrot_set.html (33 blocks) ---
t = []
t.append('[[i class="fa-solid fa-list"]][[/i]]目录')
t.append('[[a href="#section1"]]Mandelbrot 集合[[/a]]')
t.append('[[a href="#section2"]]构造 Mandelbrot 集合[[/a]]')
t.append('[[a href="#section3"]]彩色 Mandelbrot 集合[[/a]]')
t.append('[[a href="#section4"]]进一步阅读[[/a]]')
t.append('Mandelbrot 集合')
t.append("""\
                    Mandelbrot 集合本质上是通过在复平面的点上迭代一个简单函数生成的。\
                    产生循环（反复得到相同的值）的点属于该集合，而发散（给出不断增长的值）的点位于集合之外。\
                    当在计算机屏幕上以多种颜色绘制时（不同的发散速度对应不同的颜色），\
                    集合外的点可以产生非常美丽的图像。\
                    Mandelbrot 集合的边界是一条具有无限复杂性的分形曲线，\
                    其任何部分都可以被放大以揭示越来越多的惊人细节，\
                    包括整个集合本身的微型复制品。\
                """)
t.append("""\
                    Mandelbrot 集合无疑是最流行的分形，\
                    也许也是当代数学中最流行的对象。\
                    自从 [[a href="https://users.math.yale.edu/mandelbrot/" target="_blank"]]Benoît B.\
                        Mandelbrot[[/a]]\
                    (1924-2010) 在 1979-1980 年研究映射 @@math:11:c69a20@@ 时发现它以来，\
                    它已被全世界成千上万的人（包括我自己）复制过。\
                """)
t.append('构造 Mandelbrot 集合')
t.append("""\
                    以下是 Mandelbrot 集合的构造方法。取一个起始值 @@math:12:7fab8e@@\
                    并构造序列 @@math:13:19ad62@@\
                    这个序列中的点集称为 @@math:14:616ea4@@ 在 @@math:15:fe8d14@@ 下的迭代轨道。\
                """)
t.append("""\
                    如果轨道 @@math:18:e42348@@ 不趋于无穷大，则称起始点 @@math:19:cf1cd2@@ 属于\
                    Mandelbrot 集合，记为 @@math:20:fb16a7@@ 如果轨道趋于无穷大，则称该点不属于 Mandelbrot 集合。\
                """)
t.append("""\
                    以 @@math:24:1b273f@@ 为例。那么有\
                    @@math:25:a82ce3@@\
                    因此 @@math:26:d0f4c9@@\
                """)
t.append("""\
                    手工计算 Mandelbrot 集合的元素是非常有趣的，而且对处理复数来说也是一种很好的练习。\
                    然而，这个序列是无限的，因此实际上需要借助计算机来确定一个点是否属于 Mandelbrot 集合。\
                """)
t.append("""\
                    如果轨道 @@math:36:a81ad5@@ 最终位于半径为 @@math:37:9ce1e1@@ 的圆盘之外，那么可以证明该轨道将趋于无穷大。\
                    因此，计算轨道的一个有用准则是：一旦 @@math:38:96f9fe@@ 就停止迭代，并断定该序列发散。\
                """)
t.append('现在在小程序中探索迭代轨道。观察其行为，同时在右侧观察 Mandelbrot 集合中对应的点。')
t.append('彩色 Mandelbrot 集合')
t.append("""\
                    在前面的小程序中，Mandelbrot 集合是仅用两种颜色绘制的。然而，使用多种颜色可以产生更引人注目的图像。\
                    一种常见的着色方案是为集合外的点分配不同的颜色，颜色取决于其轨道发散的速度。\
                """)
t.append("""\
                    在下面的小程序中，\
                    [[a\
                        href="https://en.wikipedia.org/wiki/Mandelbrot_set" target="_blank"]]Mandelbrot 集合[[/a]]\
                    用红色和白色着色，而集合外的点则根据其轨道发散的速度用不同的颜色着色。\
                """)
t.append('现在探索 Mandelbrot 集合。在不同的区域放大或缩小。享受吧！')
t.append('进一步阅读')
t.append("""\
                    尽管 Mandelbrot 集合由一个非常简单的规则定义，但它具有有趣而复杂的性质，\
                    这些性质可以通过更严格的论证来研究。这里不想深入探讨这些论证，\
                    但推荐以下文献以获取更详细的讨论和 Mandelbrot 集合的美丽图像。\
                """)
t.append('Mandelbrot 集合已被广泛研究，这里不打算深入探讨其数学细节。然而，以下书籍是极好的资源：')
t.append('[[a href="https://www.amazon.com/Fractal-Geometry-Nature-Benoit-Mandelbrot/dp/0716711869" target="_blank"]]Benoît B. Mandelbrot，《大自然的分形几何》[[/a]]')
t.append('[[a href="https://www.springer.com/gp/book/9780387201580" target="_blank"]]Heinz-Otto Peitgen 和 Peter H. Richter，《分形的美丽》[[/a]]')
t.append('还推荐以下 [[em]]Numberphile[[/em]] 视频：')
t.append('[[a href="https://www.youtube.com/watch?v=NGMRB4O922I&list=PLt5AfwLFPxWJ3dmDk_YgG_vb_OWac-Asn" target="_blank"]]Numberphile：Mandelbrot 集合[[/a]]')
t.append('[[a href="https://youtu.be/FFftmWSzgmk" target="_blank"]]Numberphile：Mandelbrot 集合是什么样的？[[/a]]')
t.append("""\
                    这些小程序是用 [[a href="https://www.geogebra.org/" target="_blank"]]GeoGebra[[/a]] 制作的。\
                    它们的源代码可以在这里找到：\
                """)
t.append('[[a href="https://www.geogebra.org/material/show/id/xtgsqyka" target="_blank"]]Mandelbrot 迭代轨道[[/a]]')
t.append('[[a href="https://github.com/complex-analysis/complex-analysis.github.io/tree/master/applets/p5js" target="_blank"]]GitHub 上的 p5.js 小程序[[/a]]')
t.append('[[a href="https://thecodingtrain.com/CodingChallenges/021-mandelbrot-p5.html" target="_blank"]]Coding Train：Mandelbrot 集合编程挑战[[/a]]')
t.append('最后，如果擅长编程，那么可以很容易地将 Mandelbrot 集合翻译成任何编程语言。网上有很多现成的代码示例。')
t.append('Julia 集合 [[i class="fa-solid fa-angles-right"]][[/i]]')
translations['mandelbrot_set.html'] = t

# --- taylor_series.html (32 blocks) ---
t = []
t.append('[[i class="fa-solid fa-list"]][[/i]]目录')
t.append('[[a href="#section1"]]对实函数[[/a]]')
t.append('[[a href="#section2"]]对复函数[[/a]]')
t.append('[[a href="#section3"]]动态探索[[/a]]')
t.append('[[a href="#section4"]]Maclaurin 级数[[/a]]')
t.append('泰勒级数')
t.append('对实函数')
t.append("""\
                    设 @@math:22:a431bc@@ 且 @@math:23:1ac8aa@@ 是在包含 @@math:25:0dae20@@ 的区间 @@math:24:7000c6@@ 上无穷可微的函数。\
                    则 @@math:26:486cdd@@ 在 @@math:27:6341a0@@ 处的一维泰勒级数为\
                <div class="scroll-wrapper">\
                    @@math:28:9c5adf@@\
                </div>\
                    可以写成最紧凑的形式：\
                <div class="scroll-wrapper">\
                    @@math:29:f1445c@@\
                </div>\
                """)
t.append("""\
                    回顾实分析中，泰勒定理通过 @@math:31:34d072@@ 阶泰勒多项式给出了 @@math:30:b78c73@@ 次可微函数在给定点附近的近似。\
                """)
t.append("""\
                    例如，@@math:32:0f18be@@ 的最佳线性近似是\
                    @@math:20:38854d@@\
                    这个线性近似用通过 @@math:34:72f35b@@ 且与 @@math:35:09e4b6@@ 在 @@math:36:6d7782@@ 处的斜率匹配的直线来拟合 @@math:33:cbefe0@@\
                """)
t.append("""\
                    为了获得更好的近似，可以在展开式中添加其他项。例如，最佳二次近似是\
                        @@math:21:d4755b@@""")
t.append('下面的小程序显示了泰勒级数的部分和。拖动滑块以查看更多项。')
t.append('对复函数')
t.append("""\
                    假设函数 @@math:37:f5b14d@@ 在圆盘 @@math:38:7c5f2b@@ 上解析，\
                    其中 @@math:39:e560e7@@ 则 @@math:40:8baa90@@ 在 @@math:41:0a2b89@@ 上有幂级数表示\
                    @@math:42:ead2b6@@\
                    其中 @@math:43:6b4fcd@@\
                """)
t.append("""\
                    每个复幂级数 (\\ref{seriefunction}) 都有一个收敛半径 @@math:44:92734c@@，\
                    它是满足以下条件的最大数：当 @@math:45:acecf1@@ 时级数收敛，当 @@math:46:81a08e@@ 时级数发散。\
                    收敛半径可以是：\
                """)
t.append('@@math:53:2011ab@@（此时 (\\ref{seriefunction}) 仅在 @@math:54:e0ff3e@@ 处收敛）')
t.append('@@math:55:b6a0ab@@ 是一个有限正数（此时 (\\ref{seriefunction}) 在 @@math:56:629189@@ 时收敛）')
t.append('@@math:57:4df807@@（此时 (\\ref{seriefunction}) 对所有 @@math:58:f5dd0a@@ 收敛）')
t.append('收敛半径可以用比率检验法计算：')
t.append('@@math:59:c2468b@@ 收敛半径是')
t.append('@@math:61:afc778@@ 收敛半径是')
t.append('@@math:63:055869@@ 收敛半径是')
t.append('动态探索')
t.append('使用以下小程序探索泰勒级数表示及其部分和。')
t.append("""\
                    在下面小程序的左侧，显示了一个复函数的相位图。在右侧，可以看到该函数的泰勒多项式近似的相位图。\
                    可以拖动点 @@math:64:27e648@@ 来改变中心点，也可以增加或减少近似的项数。\
                """)
t.append("""\
                    也可以从以下列表中选择一个函数：[[br]]\
                    - @@math:10:3674e5@@\
                    [[br]]\
                    - @@math:11:c6563a@@\
                    [[br]]\
                    - @@math:12:3e2d22@@\
                    [[br]]\
                    - @@math:13:8c4e88@@\
                """)
t.append('Maclaurin 级数')
t.append("""\
                    中心在 @@math:68:79e012@@ 的泰勒级数称为 [[em]]Maclaurin 级数[[/em]]。\
                """)
t.append("""\
                    一些重要的 Maclaurin 级数有：\
                    <div class="scroll-wrapper">\
                        @@math:14:89b04d@@\
                    </div>\
                """)
t.append('[[strong]]练习：[[/strong]] 求 @@math:69:a43812@@ 的 Maclaurin 级数展开。')
t.append("""\
[[strong]]注意：[[/strong]] 该小程序最初由 David Bau 编写。原始版本可在 [[a href="http://davidbau.com/conformal/#z" target="_blank"]]此处[[/a]] 找到。\
                """)
t.append('洛朗级数 [[i class="fa-solid fa-angles-right"]][[/i]]')
translations['taylor_series.html'] = t

# --- fundamental_theorem_of_algebra.html (31 blocks) ---
t = []
t.append('代数基本定理  [[br]]')
t.append("""\
              考虑多项式\
            """)
t.append("""\
              [[strong]]代数基本定理[[/strong]]指出：\
              [[em]]每个具有复系数的非常数多项式在复数中都有一个根。[[/em]]\
            """)
t.append("""\
                  @@math:9:87f9f6@@ 的增强相位图及\
                  @@math:10:650b16@@ 的等值线\
                  [[a href="https://complex-analysis.com/applets/p5js/domain-coloring/?expression=el44LTJ6XjcrMnpeNi00el41KzJ6XjQtMnpeMy01el4yKzR6LTQ=" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]\
              """)
t.append("""\
              图 1 显示了 (\\ref{example-001}) 中定义的多项式的 [[a href="domain_coloring.html"]]增强相位图[[/a]]，\
              以及模的等值线。\
              从这张图中首先注意到的是，代数基本定理确实对 @@math:11:3b9886@@ 成立。\
              回顾一下，使用增强相位图可以很容易地发现复变函数的根或零点。只需寻找所有颜色交汇的点。\
              在图 1 中可以清楚地看到有六个所有颜色交汇的点，这意味着\
              @@math:12:f9c437@@ 有 6 个根。\
              [[strong]]为什么 @@math:13:4b96a1@@ 作为一个八次多项式只有六个根？[[/strong]] 原因是其中两个根是[[em]]二重根[[/em]]\
              （也称其[[em]]重数为二[[/em]]），\
              这一事实在图像中也显而易见。[[em]]单根[[/em]]\
              出现在颜色以简单的有序方式交汇的地方（如点 @@math:14:eb2f2a@@），而二重根出现在颜色以双重的、更复杂的方式交汇的地方（如点 @@math:15:9f12ce@@）。\
            """)
t.append("""\
              多项式 \\ref{example-001} 的另一个迷人性质是，如果沿一个非常大的圆（例如 @@math:16:e0b78c@@）绘制其相位图，\
              那么颜色会绕着圆周交替变化八次，这正好对应于多项式的次数。\
            """)
t.append('证明与历史注记')
t.append("""\
              [[a href="cauchy_integral_formula.html#cauchy-inequality"]]柯西不等式[[/a]]可以用来证明 [[em]]Liouville 定理[[/em]]：\
              如果一个函数在整个复平面上解析且有界，则它必为常数。\
            """)
t.append('现在借助 Liouville 定理，可以轻松证明代数基本定理。')
t.append("""\
              按照通常的方法可以推出，任何多项式 @@math:53:b96f10@@ 都可以分解为一次因式的乘积\
              @@math:54:2b9212@@\
              其中 @@math:55:18eec9@@ 是 @@math:56:35bab4@@ 的零点，且这些零点不必互异。\
            """)
t.append("""\
              根据 B. Fine 和 G. Rosenberger\
              [[a href="https://link.springer.com/book/10.1007/978-1-4612-1928-6" target="_blank"]] [[em]]代数基本定理[[/em]][[/a]]，\
              代数基本定理的已知证明不少于 111 种。\
              其中第一个证明是由 Carl Friedrich Gauss 于 1799 年发表的，\
              当时他 22 岁。然而，Gauss 的原始证明假设了代数曲线的某些性质，\
              这些性质在 1799 年尚未被证明。后来，他发表了另外三种不同的证明，\
              最后一次是在 1849 年。\
            """)
t.append("""\
[[strong]]Gauss 原始证明的概要：[[/strong]]\
              设 @@math:57:d2ce61@@ 是一个多项式。将 @@math:58:8ef024@@ 的实部和虚部设为零，即\
              @@math:59:fa23f8@@ 和 @@math:60:7f7b47@@\
              然后证明曲线 @@math:61:5c6acc@@ 和 @@math:62:f8051a@@ 至少有一个交点。\
            """)
t.append('例如，图 2 展示了曲线 @@math:77:85581e@@ 和 @@math:78:4d1ae9@@')
t.append('曲线 @@math:80:090ac1@@（红色）和 @@math:81:c4335f@@（蓝色）。')
t.append("""\
              尽管有人认为 Gauss 对代数基本定理的第一个证明在拓扑基础上存在某些漏洞，\
              但他的论证中仍有一些相当深刻的思想。后来的证明由 Argand、Cauchy 等人完成。\
            """)
t.append('参考文献')
t.append('Abian, A. (1986). A new proof of the fundamental theorem of algebra. [[em]]Caribbean Journal of Mathematics[[/em]], 5(1), 1-6.')
t.append('Bennish, J. (1992). Another proof of the fundamental theorem of algebra. [[em]]American Mathematical Monthly[[/em]], 99(5), 426-428.')
t.append('Boas, Jr., R. P. (1935). A proof of the fundamental theorem of algebra. [[em]]American Mathematical Monthly[[/em]], 42(8), 501-502.')
t.append('Boas, Jr., R. P. (1964). Yet another proof of the fundamental theorem of algebra. [[em]]American Mathematical Monthly[[/em]], 71(2), 180.')
t.append('Byl, J. (1999). A simple proof of the fundamental theorem of algebra. [[em]]International Journal of Mathematical Education in Science and Technology[[/em]], 30(4), 602-603.')
t.append('Fefferman, C. (1967). An easy proof of the fundamental theorem of algebra. [[em]]American Mathematical Monthly[[/em]], 74(7), 854-855.')
t.append('Fine, B. &amp; Rosenberger. G. (1997). [[em]]The Fundamental Theorem of Algebra[[/em]]. Springer.')
t.append('Gauss, C. F. (1799). [[em]]Demonstratio nova theorematis omnem functionem algebraicam rationalem integram unius variabilis in factores reales primi vel secundi gradus resolvi posse[[/em]]. Helmstedt.')
t.append('Gauss, C. F. (1850). Beiträge zur Theorie der algebraischen Gleichungen. [[em]]Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen[[/em]], 4.')
t.append('Redheffer, R. M. (1964). What! Another note just on the fundamental theorem of algebra? [[em]]American Mathematical Monthly[[/em]], 71(2), 180-185.')
t.append('Sen, A. (2000). Fundamental theorem of algebra—yet another proof. [[em]]American Mathematical Monthly[[/em]], 107(9), 842-843.')
t.append('Stillwell, J. (1989).  [[em]]Mathematics and its History[[/em]]. Springer.')
t.append('Velleman, D. J. (1997). Another proof of the fundamental theorem of algebra. [[em]]Mathematics Magazine[[/em]], 70(3), 201-203.')
t.append('Vellemen, D. J. (2015). The Fundamental Theorem of Algebra: A Visual Approach. [[em]]The College Mathematics Journal[[/em]], 46(1), 17-24.')
t.append('级数[[i class="fa-solid fa-angles-right"]][[/i]]')
translations['fundamental_theorem_of_algebra.html'] = t

# --- continuity.html (30 blocks) ---
t = []
t.append('连续性')
t.append("""\
                函数 @@math:10:503453@@ 在点 @@math:11:497bb2@@ 处[[strong]]连续[[/strong]]，如果满足以下条件：\
            """)
t.append("""\
                    @@math:12:ceb171@@ 存在，\
                """)
t.append("""\
                    @@math:13:87be65@@ 存在，且\
                """)
t.append("""\
                    @@math:14:321c68@@\
                """)
t.append("""\
                注意 [[strong]]陈述 3[[/strong]] 实际上包含了\
                [[strong]]陈述 1[[/strong]] 和 [[strong]]2[[/strong]]，因为等式中每边的量都必须存在。\
            """)
t.append("""\
                [[strong]]陈述 3[[/strong]]\
                表明对每个正数 @@math:15:3db7ee@@，存在正数 @@math:16:179884@@ 使得\
            """)
t.append("""\
                称一个复变量函数在区域 @@math:17:24d5cc@@ 中[[strong]]连续[[/strong]]，如果它在 @@math:18:170520@@ 中的每一点都连续。\
            """)
t.append("""\
                如果函数 @@math:19:cb1ae1@@ 在点 @@math:20:cec7b7@@ 处不连续，\
                则称 @@math:21:06b63a@@ 在 @@math:22:20754b@@ 处不连续。\
                例如，函数\
                @@math:23:ec395b@@\
                在 @@math:24:bc581c@@ 和 @@math:25:190832@@ 处不连续。\
            """)
t.append("""\
                    [[strong]]例 1：[[/strong]]\
                    断言函数 @@math:26:f204c4@@ 对每个 @@math:27:33e1e9@@ 都连续。\
                """)
t.append("""\
                    为证明这一点，固定 @@math:28:1991c1@@ 如果 @@math:29:1ec09d@@\
                    那么\
                    @@math:30:db476a@@\
                    因此\
                    @@math:31:636d02@@\
                """)
t.append("""\
                    因此，通过选择 $\\delta = \\min\\left\\{ \\dfrac{\\abs{z_0}^2}{2}, \\dfrac{\\abs{z_0}^2}{2}\\epsilon \\right\\}$，\
                    可得 @@math:32:4a3abb@@\
                """)
t.append("""\
[[strong]]注：[[/strong]]\
                一个[[em]]有用的事实[[/em]]是，如果函数在某个点处可微，则它在该点处必然连续。\
                """)
t.append('在前面的例子中，证明了函数 @@math:34:c7c6f0@@ 是连续的，但没有使用定义。事实上，该函数是可微的，因此连续。')
t.append("""\
[[strong]]例 2：[[/strong]]\

                    考虑函数 @@math:35:be29f0@@ 其在 @@math:36:bcc2d7@@ 处连续吗？\
                """)
t.append("""\
                    使用 [[a href="license.html#limits-properties"]]极限的性质[[/a]]，有\
                    @@math:37:ee6cb7@@\
                """)
t.append("""\
                    此外，对于 @@math:47:33a096@@，有\
                """)
t.append("""\
                    由于 @@math:49:39bd3c@@，得出\
                """)
t.append("""\
                    现在假设 @@math:61:f802e8@@ 在 @@math:62:fbedfc@@ 处连续且 @@math:63:b6a313@@ 在 @@math:64:99b6b9@@ 处连续。\
                    则复合函数 @@math:65:1ac49d@@ 在 @@math:66:cbf55b@@ 处连续。\
                """)
t.append('函数复合的几何解释。')
t.append("""\
                    由于 @@math:70:29de0f@@ 在 @@math:71:1c6b98@@ 处连续，\
                    存在 @@math:72:adc367@@ 使得\
                """)
t.append("""\
                    由于 @@math:82:dde645@@，可以取 @@math:83:edc2ec@@\
                """)
t.append("""\
                    还注意到\
                    @@math:90:68af1a@@ 的连续性可以从 [[a href="limits.html#limits-properties"]]极限的性质[[/a]] 直接推出。\
                    特别是，如果 @@math:91:12c2b3@@ 和 @@math:92:390148@@ 在 @@math:93:10d96b@@ 处连续，则\
                """)
t.append('代数 [[a href="limits.html#limits-properties"]]极限的性质[[/a]] 如下：')
t.append('@@math:109:9c6d43@@ 其中 @@math:110:1ec293@@ 是复常数，')
t.append('@@math:111:295345@@')
t.append('@@math:112:e8951f@@ 且')
t.append('@@math:113:4e3b4c@@ 如果 @@math:114:75f33c@@')
t.append("""\
[[strong]]练习：[[/strong]]\
                    证明函数 @@math:115:5d7c55@@ 在任意点 @@math:116:11b4ac@@ 处连续。\
                """)
t.append('复微分 [[i class="fa-solid fa-angles-right"]][[/i]]')
translations['continuity.html'] = t

# --- domain_coloring.html (30 blocks) ---
t = []
t.append('[[i class="fa-solid fa-list"]][[/i]]目录')
t.append('[[a href="#section1"]]复相位图[[/a]]')
t.append('[[a href="#section2"]]探索复变函数[[/a]]')
t.append('[[a href="#section3"]]注意！[[/a]]')
t.append('[[a href="#section4"]]函数画廊[[/a]]')
t.append('区域着色')
t.append('复相位图')
t.append("""\
                    可视化复变函数 @@math:9:3d7d74@@ 的一种方法是使用相位图。一个复数可以根据其辐角/相位赋予一种颜色。\
                    正数着红色；负数着青色，具有非零虚部的数按图 1 所示着色，\
                    该图展示了函数 @@math:10:d4211b@@ 的相位图。\
                """)
t.append("""\
                        @@math:11:87b29d@@ 的相位图\
                    """)
t.append("""\
                    在其著作 [[a href="http://www.springer.com/de/book/9783034801799" target="_blank"]] [[em]]Visual Complex\
                            Functions[[/em]][[/a]] 中，\
                    Elias Wegert 使用带有相位和模的等值线的相位图（[[em]]增强相位图[[/em]]）来研究复变函数理论。\
                    例如，参见图 2 和图 3 中函数 @@math:12:723253@@ 的图像。\
                """)
t.append('相位的等值线。')
t.append('模的等值线。')
t.append("""\
                    称复变函数 @@math:13:f9dee1@@ 在 @@math:14:139159@@ 处有[[em]]根（或零点）[[/em]]，\
                    如果 @@math:15:a4125f@@ 还称 @@math:16:df98ca@@ 在 @@math:17:98ca48@@ 处有一个[[em]]极点[[/em]]，\
                    如果 @@math:18:f2789e@@\
                """)
t.append('在 @@math:19:97c9d2@@ 处的根。')
t.append('在 @@math:20:fba8ef@@ 处的极点。')
t.append("""\
                    现在考虑函数\
                    @@math:5:2d6770@@\
                """)
t.append('图 6 展示了 (\\ref{eq1}) 的增强相位图，其中包含模的等值线。')
t.append('@@math:22:761a40@@ 的图像，带有模的等值线。')
t.append('探索复变函数')
t.append('使用下面的小程序探索各种复变函数的增强相位图。')
t.append('注意！')
t.append("""\
                    如果不施加额外的限制条件，\
                    如等值线，则很难从相位图推断出函数的解析性质。\
                """)
t.append("""\
                    事实上，解析函数（几乎）由其相位图唯一确定：\
                    如果两个解析函数在一个区域上具有相同的相位图，则它们仅相差一个正实常数因子。\
                """)
t.append('由于纯相位图并不总能显示足够的信息来区分函数，因此使用增强相位图（带有等值线）通常更有帮助。')
t.append('@@math:27:94814d@@（左）和 @@math:28:81e505@@（右）的增强相位图。')
t.append("""\
                    两个图像之间的一个显著区别是等值线的形状。在 @@math:29:2fb83f@@ 的图像中，等值线是圆形的，\
                    而在 @@math:30:d8570b@@ 的图像中，等值线不是圆形的。这表明两个函数之间存在本质区别。\
                """)
t.append('函数画廊')
t.append("""\
                    如果想使用增强相位图探索更多复变函数，\
                    可以使用以下小程序。只需输入任何复变函数表达式，即可看到其增强相位图。\
                """)
t.append('函数画廊。')
t.append('复幂函数 [[i class="fa-solid fa-angles-right"]][[/i]]')
translations['domain_coloring.html'] = t

# --- index.html (29 blocks) ---
t = []
t.append('[[b]]复分析[[/b]]')
t.append("""\
                    [[span style="font-size: 0.5em;"]]可视化与交互式导论[[/span]]\
                """)
t.append("""\
Juan Carlos Ponce Campuzano  [[br]] \
                    2019 -\
                    @@verbatim:2:fd73a9@@\
                     [[br]] \
                    [[span class="dark-mode-button" id="dark-mode-toggle"]]\
                        <i class="fa-solid fa-moon"></i>\
                    [[/span]]\
                """)
t.append("""\
Juan Carlos  [[br]]  Ponce Campuzano\
                     [[br]] \
                    2019 -\
                    @@verbatim:3:23e2e4@@\
                     [[br]] \
                    [[span class="dark-mode-button" id="dark-mode-toggle"]]\
                        <i class="fa-solid fa-moon"></i>\
                    [[/span]]\
                """)
t.append("""\
                复分析的学习对工程和物理科学的学生很重要，也是数学的核心学科。\
                除了数学上的优雅之外，复分析为解决那些用其他方法非常困难或几乎不可能解决的问题提供了强大的工具。\
                """)
t.append('在本书中，可以找到例子、问题和小程序，通过计算机（或平板电脑）视觉交互的力量来探索复分析。')
t.append("""\
[[strong]]更新！[[/strong]]\
                为庆祝本站五周年，采用了新的设计。\
                还更新了许多 JavaScript 小程序以获得更好的性能。\
                别忘了加入我在\
                [[a href="https://www.patreon.com/posts/celebrating-5-of-99495115?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link" target="_blank"]]Patreon[[/a]]\
                以获取更多更新！\
                """)
t.append('准备好开始了吗？跳到 [[a href="content/table_of_contents.html"]]目录[[/a]]。')
t.append('本书内容')
t.append("""\
                本书是对复变函数理论和应用的交互式导论。\
                它旨在帮助读者以直观和互动的方式理解复分析的基本概念。\
                书中有许多可视化和交互式小程序，用于说明所讨论的概念。\
                """)
t.append('本书涵盖的主题包括复数的基本算术、复变函数、复微分、复积分、级数、留数理论等。')
t.append("""\
                这本在线书籍与传统教材的区别在于，它广泛使用交互式可视化，\
                这些可视化旨在帮助读者发展对复分析中涉及的数学对象的几何直觉。\
                """)
t.append("""\
                尽管提倡使用计算机作为获得几何洞察力的辅助工具，\
                但同样重要的是要记住，这些工具不能替代严格的数学推理。\
                在每种情况下都提供了正式的论证。\
                """)
t.append('把计算机想象成物理学家的实验室。它可以用来探索和实验，但最终，正式的论证才是证实猜想的手段。')
t.append('[[strong]]注意！[[/strong]] 如果在移动设备上，某些小程序可能无法正常工作。建议使用台式机或笔记本电脑以获得最佳体验。')
t.append("""\
                本书被收录在\
                [[a href="https://open.umn.edu/opentextbooks/textbooks/complex-analysis-a-visual-and-interactive-introduction" target="_blank"]]开放教科书图书馆[[/a]] 中。\
                """)
t.append('问题？')
t.append('当然，任何这样的项目都难免有错误和不完整之处。如果发现任何问题，请在 [[a href="https://github.com/complex-analysis/complex-analysis.github.io/issues" target="_blank"]]GitHub[[/a]] 上提交 issue。')
t.append('设计鸣谢')
t.append('本站的初始设计灵感来自以下精美的项目：')
t.append('[[a href="https://github.com/vincentdoerig/latex-css" target="_blank"]]LaTeX.CSS[[/a]]')
t.append('[[a href="https://github.com/davidrzs/latexcss" target="_blank"]]latexcss[[/a]]')
t.append('[[a href="https://github.com/magicbookproject" target="_blank"]]Magic Book 项目[[/a]]')
t.append('支持本项目')
t.append('如果喜欢我的工作，可以通过以下链接支持：')
t.append('感谢你的支持！❤️')
t.append('导航')
t.append('好，让我们开始吧！点击页面底部的链接，或者目录中的链接。')
t.append('目录 [[i class="fa-solid fa-angles-right"]][[/i]]')
translations['index.html'] = t

# ============================================================
# WRITE OUTPUT
# ============================================================
with open('batch_b.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print("Written batch_b.json successfully.")
for k, v in translations.items():
    print(f"  {k}: {len(v)} translations")
