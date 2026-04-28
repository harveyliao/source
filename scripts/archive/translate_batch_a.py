#!/usr/bin/env python3
"""
Translate all extracted blocks from English to Chinese.
Uses a dictionary of translations for all 517 blocks.
Markers (@@math:..., @@verbatim:..., [[...]], etc.) are preserved exactly.
"""
import json
import re
import os

# Load extracted blocks
with open("/home/harvey/extracted_blocks.json", 'r') as f:
    all_blocks = json.load(f)

# Translation dictionary: map each block text to its Chinese translation
# We'll build this programmatically with a translate_block function

TRANSLATIONS = {}

def t(filename, block_text):
    """Register a translation for a block."""
    if filename not in TRANSLATIONS:
        TRANSLATIONS[filename] = []
    TRANSLATIONS[filename].append(block_text)

# ============================================================
# FILE: cauchy_goursat_theorem.html (97 blocks)
# ============================================================
fn = "cauchy_goursat_theorem.html"
t(fn, '<p>: [[i class="fa-solid fa-list"]][[/i]]目录')

t(fn, '<li>: [[a href="#section1"]]柯西定理[[/a]]')

t(fn, '<li>: [[a href="#section2"]]柯西-古尔萨定理[[/a]]')

t(fn, '<li>: [[a href="#section3"]]连通域[[/a]]')

t(fn, '<li>: [[a href="#section4"]]历史注记 &amp; 证明[[/a]]')

t(fn, '<li>: [[a href="#section5"]]参考文献[[/a]]')

t(fn, '<h1>: 柯西-古尔萨定理')

t(fn, '<h2>: 柯西定理')

t(fn, '<p>: \n                1825 年，法国数学家 Augustin-Louis Cauchy 证明了\n                复分析中最重要的定理之一：')

t(fn, '<figcaption>: \n                    柯西定理蕴含 @@math:32:03bc90@@')

t(fn, '<p>: \n                若函数在 @@math:33:7330c9@@ 内部的整个区域上不解析，\n                则积分可能为零也可能不为零 @@math:34:e8d495@@ 例如，\n                设 @@math:35:bf0104@@ 为单位圆且 @@math:36:d9b344@@ 则 @@math:37:75eb6b@@\n                在所有点处解析，除了 @@math:38:2a581a@@ 处，并且积分确实\n                [[em]]不为零[[/em]]。事实上，\n                @@math:39:cc236e@@\n                如\n                [[a href="complex_integration.html"]]复积分[[/a]] 部分中的例 2 所示。\n                另一方面，若 @@math:40:9b1ab2@@ 则 @@math:41:94d72a@@ 仍然\n                在所有点处解析，除了 @@math:42:a0efff@@ 处，但此时积分 [[em]]为零[[/em]] @@math:43:8215d7@@\n                这个结果 [[em]]并非[[/em]] 来自柯西定理，因为 @@math:44:932aec@@\n                在 @@math:45:5e30f4@@ 内部并非处处解析，而是因为\n                @@math:46:e594b9@@ 在 @@math:47:a37478@@ 上有原函数。即 @@math:48:5ff394@@ 是\n                @@math:49:c43570@@ 的导数。')

t(fn, '<p>: \n                [[em]]定理 1 的证明。[[/em]] 该定理的证明是\n                [[strong]]格林定理[[/strong]] 的直接推论，格林定理指出，对于\n                连续可微函数 @@math:50:104a51@@ 和 @@math:51:b7e839@@')

t(fn, '<p>: \n                在格林定理中，@@math:52:0b8cd9@@ 表示 @@math:53:95625e@@ 的 [[em]]内部[[/em]]\n                @@math:54:088c93@@ 沿逆时针方向行进，且\n                @@math:55:2fb8cb@@ 和 @@math:56:3dab5f@@ 充分光滑。')

t(fn, '<p>: 设 @@math:57:4fb30d@@ 则有')

t(fn, '<p>: \n                对每个积分应用格林定理，可得')

t(fn, '<p>: \n                根据 [[a href="complex_differentiation.html"]]柯西-黎曼方程[[/a]]，右侧的两个积分均为零。@@math:58:f2fa15@@')

t(fn, '<p>: 注意到一旦确立了该积分的值为零，\n                @@math:59:959cd2@@ 的定向就变得无关紧要。\n                若 @@math:60:db6951@@ 取顺时针方向，定理 1 的结论仍然成立，\n                因为此时可以利用\n                @@math:61:8de49b@@')

t(fn, '<p>: [[strong]]例 1：[[/strong]]\n                  考虑函数 @@math:62:7123ff@@ 若 @@math:63:c24ed9@@ 是\n                  任意简单闭曲线，不论方向，则\n                  @@math:64:03ea60@@\n                  在这种情况下，@@math:65:a9b026@@ 是两个处处解析函数的复合。\n                  因此，@@math:66:406184@@ 也是解析的，且其导数\n                  @@math:67:4c3089@@\n                  处处连续。')

t(fn, '<h2>: 柯西-古尔萨定理')

t(fn, '<p>: \n                1900 年，法国数学家\n                [[a href="https://mathshistory.st-andrews.ac.uk/Biographies/Goursat/" target="_blank"]]Edouard Goursat[[/a]]\n                证明了 @@math:68:00f50a@@ 的连续性假设\n                对于得出 [[em]]柯西定理[[/em]] 的结论并非必要。\n                由此得到的柯西定理修正版本如今被称为\n                [[em]]柯西-古尔萨定理[[/em]]。\n                正如我们所预料的，\n                由于假设更少，该版本的柯西定理证明\n                比刚才给出的证明更为复杂。')

t(fn, '<p>: \n                    [[strong]]例 2：[[/strong]]\n                    函数 @@math:72:51a3f5@@ 是整函数，因此\n                    在任意简单闭曲线 @@math:73:7ddaa7@@ 内部及其上的所有点处解析。\n                    由柯西-古尔萨定理可知\n                    @@math:74:e4e3d4@@\n                    类似地，由于 @@math:75:f4db0a@@ @@math:76:045884@@ 和')

t(fn, '<p>: 都是整函数，所以')

t(fn, '<p>: \n                    对任意简单闭曲线 @@math:77:7a9dbf@@')

t(fn, '<p>: \n                  [[strong]]例 3：[[/strong]]\n                  可以利用柯西-古尔萨定理计算\n                  @@math:78:158faa@@\n                  其中 @@math:79:e1a8ff@@ 是椭圆 @@math:80:7a5631@@\n                  注意到函数 @@math:81:0ba80d@@\n                  除了在 @@math:82:5cd723@@ 处外处处解析。在这种情况下，@@math:83:40ffa1@@ 不在\n                  简单闭椭圆曲线 @@math:84:179282@@ 内部或之上。因此\n                  @@math:85:48cd29@@')

t(fn, '<figcaption>: \n                     椭圆曲线 @@math:86:2e4774@@ 勾选 [[code]]Phase portrait[[/code]] 可显示\n                     @@math:87:aee09e@@ 的增强相位图及其模的等值线。')

t(fn, '<h2>: 单连通与多连通域')

t(fn, '<p>: \n                称一个域 @@math:88:d650c8@@ 是 [[em]]单连通的[[/em]]，如果\n                完全位于 @@math:90:5598d3@@ 内的每条简单闭曲线 @@math:89:ce73d8@@ 都可以\n                在不离开 @@math:91:c4c1b2@@ 的情况下收缩到一点。参见图 3。换句话说，如果在\n                单连通域内画任意简单闭曲线 @@math:92:cdd903@@，则 @@math:93:6c1cc1@@ 仅包围\n                该域 @@math:94:a6fded@@ 中的点。')

t(fn, '<figcaption>: \n                  单连通域 @@math:95:5c5e6d@@')

t(fn, '<p>: \n                换句话说，单连通域没有"洞"。\n                整个复平面是单连通域的一个例子；\n                由 @@math:96:73390a@@ 定义的环域则不是单连通的。')

t(fn, '<figcaption>: \n                    @@math:97:46743d@@')

t(fn, '<p>: 非单连通的域称为 [[em]]多连通[[/em]] 域；即\n                多连通域中有"洞"。例如，\n                注意在图 5 中，\n                若将包围"洞"（左侧）的曲线 @@math:98:db12e7@@\n                收缩到一点，则该曲线最终必须离开 @@math:99:7e286c@@')

t(fn, '<figcaption>: \n                  非单连通域 @@math:100:525648@@')

t(fn, '<p>: \n                当柯西-古尔萨定理应用于单连通域时，其中的闭曲线不必是简单的。\n                即曲线实际上可以自交。以下\n                定理允许这种可能性。')

t(fn, '<p>: \n                若 @@math:106:7eedd7@@ 是简单闭曲线或自交有限次的闭曲线，则证明很容易。\n                当 @@math:107:1884fc@@ 是简单曲线且位于 @@math:108:bba4ae@@ 中时，函数 @@math:109:3efee4@@\n                在 @@math:110:7fdf1e@@ 内部及其上的每一点处解析。\n                柯西-古尔萨定理确保 [[strong]]定理 3[[/strong]] 的结论成立。\n                另一方面，若 @@math:111:9f6eb9@@\n                是闭曲线但自交有限次，\n                则它由有限条简单闭曲线组成。\n                如图 6 所示，其中简单闭曲线\n                @@math:112:14dfbf@@ @@math:113:3c88d5@@ 组成 @@math:114:e565e7@@ 由于\n                根据柯西-古尔萨定理，围绕每个 @@math:115:1ff55c@@ 的积分值为零，因此')

t(fn, '<figcaption>: \n                  简单闭曲线 @@math:116:a3bd06@@')

t(fn, '<p>: [[strong]]例 4：[[/strong]]\n                设 @@math:117:535de5@@ 是位于开圆盘 @@math:118:0037fc@@ 中的任意闭曲线。\n                则\n                @@math:119:72ad95@@\n                注意该圆盘是单连通域，而被积函数的两个\n                奇点 @@math:120:815948@@ 在圆盘之外。')

t(fn, '<figcaption>: \n                    开圆盘 @@math:121:22d3ae@@ 是单连通的，@@math:122:6f20b1@@ 是任意闭曲线。')

t(fn, '<p>: \n                若 @@math:126:4917c7@@ 在多连通域 @@math:127:c3601c@@ 中解析，则不能断定\n                @@math:128:2db337@@ 对 @@math:130:6bcdea@@ 中的每条简单闭曲线 @@math:129:af0b8e@@ 都成立。\n                假设 @@math:131:40c240@@ 是有两个"洞"的多连通域。\n                设 @@math:132:26eb50@@ @@math:133:fd0058@@ 和 @@math:134:23ca23@@ 是简单闭曲线，\n                使得每个 @@math:135:1457dc@@ 仅包围域中的一个"洞"\n                且位于 @@math:136:e108ad@@ 内部。参见图 8。')

t(fn, '<figcaption>: \n                  @@math:137:a74973@@ 是有两个"洞"的多连通域。')

t(fn, '<p>: \n                现在，同时假设\n                @@math:138:3fc307@@ 在每条曲线上以及\n                由 @@math:139:8ab29f@@ 内部且每个 @@math:140:1e4bc5@@ 外部\n                组成的多连通域上解析。\n                假设 @@math:141:d35604@@ 沿逆时针方向，\n                每个 @@math:142:84da73@@ 沿顺时针方向。\n                引入一条由有限条首尾相连的线段组成的\n                多边形路径 @@math:143:5be30a@@，\n                连接外曲线 @@math:144:601168@@ 和内曲线 @@math:145:391be1@@\n                如图 9 所示，再引入另一条多边形路径 @@math:146:609e6f@@，连接\n                @@math:147:e0d710@@ 到 @@math:148:49c7d4@@，最后引入另一条多边形路径\n                @@math:149:ff7488@@ 连接 @@math:150:df5d53@@ 到 @@math:151:185381@@')

t(fn, '<figcaption>: \n                  引入多边形线 @@math:152:82e64b@@')

t(fn, '<p>: \n                如图 10 所示，可以形成两条简单闭曲线\n                @@math:153:1ee688@@ 和 @@math:154:fde488@@，每条都由多边形路径\n                @@math:155:983469@@ 或 @@math:156:aae3e4@@ 以及 @@math:157:9d8fe1@@ 和 @@math:158:02d637@@ 的片段组成，\n                且每条曲线的方向使其包围的点位于左侧。\n                这里可以对 @@math:160:13c7a9@@ 和 @@math:161:2a98e8@@ 上的 @@math:159:384b03@@\n                应用柯西-古尔萨定理，\n                这些曲线上积分值的和为零。\n                由于沿每条路径 @@math:162:fb19e4@@ 的相反方向积分相互抵消，\n                仅剩下沿 @@math:163:c2a4f4@@\n                和 @@math:164:e9fdd9@@ 的积分。因此得到')

t(fn, '<figcaption>: \n                 @@math:165:795aaa@@')

t(fn, '<p>: \n                以下定理总结了具有 @@math:166:6be182@@ 个"洞"的多连通域的一般结果。')

t(fn, '<li>: \n                    C 是一条简单闭曲线，沿逆时针方向；')

t(fn, '<li>: \n                    @@math:167:7e6229@@ @@math:168:a39782@@ 是位于\n                    @@math:169:0938c0@@ 内部的简单闭曲线，均沿顺时针方向，\n                    互不相交且内部无公共点。')

t(fn, '<p>: \n                  若 @@math:170:ce75e5@@ 在所有上述曲线上以及\n                  由 @@math:171:3d775a@@ 内部且每个 @@math:172:4d04e1@@ 外部\n                  组成的多连通域上解析，则')

t(fn, '<p>: \n                以下推论称为 [[strong]]曲线变形原理[[/strong]]，\n                因为它告诉我们：若 @@math:173:f3d317@@ 连续变形为\n                @@math:174:07de56@@，始终经过\n                @@math:175:1bc710@@ 解析的点，则\n                @@math:176:f426c1@@ 沿 @@math:177:0809a0@@ 的积分值永不改变。')

t(fn, '<figcaption>: \n                  @@math:184:bfbfcd@@ 连续变形为 @@math:185:ba0b09@@')

t(fn, '<p>: \n                  [[strong]]例 5：[[/strong]]\n                  可利用上述推论证明\n                  @@math:186:3c77f9@@\n                  对任意包围原点的正向简单闭曲线 @@math:187:9d86bc@@ 成立。')

t(fn, '<p>: \n                  考虑 @@math:188:319b31@@，一个以原点为中心、半径充分小\n                  的正向圆，使得 @@math:189:d2d534@@ 完全位于 @@math:190:fb38b1@@ 内部。')

t(fn, '<p>: \n                  已知（参见\n                  [[a href="complex_integration.html"]]复积分[[/a]] 部分的例 2）\n                  @@math:191:b74fbb@@\n                  且由于 @@math:192:9b16be@@ 除了在 @@math:193:6ce130@@ 处外处处解析，\n                  结论易得。')

t(fn, '<figcaption>: \n                   @@math:194:e6707b@@')

t(fn, '<p>: \n                  [[strong]]练习 1：[[/strong]]\n                  利用曲线变形原理证明：\n                  若 @@math:195:4b8fcd@@ 是位于任意简单闭曲线 @@math:196:e01a07@@ 内部的任意复常数，\n                  则对整数 @@math:197:530356@@ 有\n                  @@math:198:4937cf@@')

t(fn, '<h2>: 历史注记 &amp; 证明')

t(fn, '<p>: \n                Cauchy 于 1814 年首次将积分定理提交给\n                [[em]]Académie des Sciences[[/em]]，作为一篇涉及\n                其他主题（反常实积分）的论文的一部分\n                [[[a href="#bottazzini1984"]]1[[/a]] pp. 132-133, [[a href="#cauchy1841"]]4[[/a]], [[a href="#smithies1997"]]13[[/a]] pp. 56-57]。\n                积分定理的第一个一般形式于 1825 年提交给\n                [[em]]Académie[[/em]]，论文标题为\n                [[em]]Mémoire sur les intégrales définies, prises entre des limites imaginaires[[/em]]\n                [[[a href="#bottazzini1984"]]1[[/a]] pp. 151-156, [[a href="#cauchy1825"]]5[[/a]], [[a href="#smithies1997"]]13[[/a]] pp. 89-91]。')

t(fn, '<p>: \n                Goursat 于 1884 年给出了柯西定理在简单闭曲线情形下的一个证明，\n                通过将内部分割成小正方形，\n                证明围绕每个边长为 @@math:199:bfe917@@ 的正方形的积分\n                受 @@math:200:1d7e5a@@ 限制，\n                然后叠加结果。为了对任意 @@math:201:656c9e@@ 得到这个估计，他需要\n                @@math:202:4e6a7a@@ 的一致连续性\n                [[[a href="#goursat1884"]]7[[/a]]]。\n                在 1900 年的论文中，Goursat 最终去掉了\n                @@math:203:6f5d5d@@ 的连续性假设 [[[a href="#borger1921"]]2[[/a]], [[a href="#goursat1900"]]8[[/a]]]。\n                论证方法如前，但他现在将\n                每个正方形进一步细分，直到对每个正方形\n                所需的估计成立，即')

t(fn, '<p>: \n                对子正方形边界上的每个 @@math:205:c59158@@ 成立，其中 @@math:206:2d73d9@@\n                是子正方形中的某个固定点。这里的关键点是\n                同一个 @@math:207:1f99c7@@ 适用于每个子正方形。')

t(fn, '<p>: \n                1900 年，Eliakim H. Moore 改进了证明，更精确地\n                处理了边界曲线 [[[a href="#moore1900"]]11[[/a]]]。\n                他还引入了现代的归谬证明方法，\n                包括细分区域、选择结论被最显著否定的区域，\n                然后在所得极限点处应用导数的定义\n                [[[a href="#hance-olsen2008"]]9[[/a]], p. 651]。')

t(fn, '<p>: \n                1901 年，Alfred Pringsheim 对 Goursat 关于边界曲线的处理\n                提出了批评 [[[a href="#pringsheim1901"]]12[[/a]]]。\n                他指出，当证明技术应用于基本几何形状（如三角形）时，\n                这些问题就消失了。由此，\n                定理通过对路径内部进行三角剖分扩展到单连通域内的简单多边形路径。\n                最后，可以通过用多边形路径逼近任意路径来推广。\n                [[[a href="#hance-olsen2008"]]9[[/a]], p. 651]。这就是我们将\n                用来证明柯西-古尔萨定理的方法。')

t(fn, '<p>: \n                为避免在以下讨论中不必要的重复，\n                我们将默认在单连通域 @@math:208:30dbb8@@ 中工作，\n                且 @@math:209:0ab44b@@ 表示在 @@math:210:8bbff1@@ 中解析的复变函数。')

t(fn, '<figcaption>: \n                      @@math:224:0b7e40@@ 内的三角形曲线 @@math:225:19af2e@@')

t(fn, '<figcaption>: \n                      三角形曲线 @@math:226:1b2afc@@')

t(fn, '<p>: \n                  利用三角不等式可得')

t(fn, '<p>: \n                  由于前一不等式右侧的四个量是非负实数，\n                  因此其中一个必须大于或等于其他三个。\n                  用符号 @@math:227:820072@@ 表示具有最大模的\n                  积分的三角形曲线。于是\n                  @@math:18:08a1b0@@')

t(fn, '<p>: \n                  现在对三角形 @@math:228:06ece4@@ 重复上述过程。即，\n                  通过连接各边中点形成 @@math:229:c282e4@@ 内的三角形，\n                  方式与图 14 所示相同，\n                  并导出与 (\\ref{sumcontours}) 和 (\\ref{triangle01}) 类似的表达式。\n                  @@math:230:c04be6@@ 沿这些新三角形曲线之一（记为\n                  @@math:231:12f800@@）的积分满足\n                  @@math:232:97a867@@')

t(fn, '<p>: \n                  将最后一个不等式与 (\\ref{triangle02}) 结合得到\n                  @@math:233:fb3154@@')

t(fn, '<p>: \n                  继续以这种方式得到一系列"嵌套的"三角形曲线\n                  @@math:234:4f4a9f@@ 即\n                  序列中的每个三角形都包含在紧接其前的三角形中。\n                  经过 @@math:235:d63f77@@ 步后得到\n                  @@math:19:49734d@@')

t(fn, '<p>: \n                  由于三角形曲线序列\n                  @@math:236:03d6fe@@ 是嵌套的，存在\n                  域 @@math:238:497a0e@@ 中的一个点 @@math:237:252bb4@@，该点属于序列中\n                  每个三角形。此外，由于 @@math:239:b793e3@@ 解析，因此 @@math:240:1c5bcd@@\n                  存在。若定义\n                  @@math:20:f5f1eb@@\n                  则当\n                  @@math:242:e38779@@ 充分接近 @@math:243:36a758@@ 时，@@math:241:b2388e@@ 可以任意小。这是成立的\n                  因为 @@math:244:32cfed@@ 在 @@math:245:2b94c6@@ 中解析，所以极限\n                  @@math:21:cb1cda@@\n                  存在且等于 @@math:246:d08aad@@ 换句话说，对每个 @@math:247:735f64@@\n                  存在 @@math:248:c4dac8@@ 使得\n                  <div class="scroll-wrapper">\n                    @@math:22:25005a@@\n                  </div>\n                  可以从 (\\ref{lambda}) 解出 @@math:249:0f18e1@@\n                  并将该值代入 (\\ref{bound4}) 中的被积函数，得到')

t(fn, '<p>: \n                  由于\n                  @@math:250:a9e431@@\n                  （为什么？），(\\ref{expanded}) 的右侧化简为\n                  @@math:24:34d758@@')

t(fn, '<p>: \n                  现在设 @@math:251:2d3db4@@ 和 @@math:252:bf92b0@@ 分别表示三角形曲线 @@math:253:c2fa7c@@ 和 @@math:254:140dd8@@ 的长度。\n                  那么，如果记住三角形 @@math:255:081806@@ 是如何构造的，\n                  通过相似三角形的简单问题可证\n                  @@math:256:341f68@@ 与 @@math:257:bf8848@@ 的关系为 @@math:258:dda00b@@ 同样，\n                  若 @@math:259:8abc2f@@ 是 @@math:260:560feb@@ 的长度，则 @@math:261:ccf3eb@@\n                  一般地，若 @@math:262:b009ed@@ 是 @@math:263:e35a9f@@ 的长度，则\n                  @@math:264:c729a8@@')

t(fn, '<p>: \n                  对任意 @@math:265:6058d4@@ 有\n                  @@math:266:658144@@ 其中 @@math:267:51759d@@\n                  若选择 @@math:268:9fb62e@@ 充分大使得\n                  @@math:269:01f211@@\n                  则由 (\\ref{reduced})、(\\ref{smallenough}) 和\n                  [[em]]ML[[/em]]-不等式可得')

t(fn, '<p>: \n                  将 (\\ref{bound4}) 与 (\\ref{boundgeneral}) 结合，得到\n                  @@math:270:a053b6@@ 上积分模的界\n                  @@math:26:ff3a14@@\n                  由于 @@math:271:0231ba@@ 可以任意小，因此 @@math:272:57049e@@\n                  于是\n                  @@math:27:dfa1d1@@')

t(fn, '<p>: \n                  [[strong]]练习 2：[[/strong]]\n                  利用 [[strong]]引理 1[[/strong]] 以及任意闭多边形曲线\n                  @@math:276:49882b@@ 可以被"三角剖分"的事实来证明 [[strong]]引理 2[[/strong]]。')

t(fn, '<figcaption>: \n                      @@math:277:657d98@@ 内的闭多边形曲线 @@math:278:05bfc3@@')

t(fn, '<figcaption>: \n                      多边形曲线 @@math:279:22133f@@ 的三角剖分')

t(fn, '<p>: \n                  [[strong]]注记：[[/strong]]\n                  粗略地说，"三角剖分"意味着闭多边形 @@math:280:dee840@@ 可以通过\n                  添加如图 16 所示的线段分解为有限个三角形。\n                  注意，然后可以像 [[strong]]引理 1[[/strong]] 的证明中那样进行，\n                  沿这些添加的线段积分两次，但方向相反。\n                  若闭多边形 @@math:281:74c7e6@@ 有 @@math:282:de1b00@@ 条边，\n                  则它可以分解为 n 个三角形 @@math:283:3ac898@@，最终得到\n                  以下类似于 (\\ref{sumcontours}) 的表达式：\n                  @@math:284:d7fd14@@')

t(fn, '<p>: \n                现在可以利用\n                [[strong]]引理 2[[/strong]] 以及任意闭曲线\n                @@math:285:000079@@ 可以用闭多边形路径逼近到任意精度\n                这一事实来轻松证明柯西-古尔萨定理。')

t(fn, '<figcaption>: \n                  曲线 @@math:286:90da6f@@ 由多边形曲线 @@math:287:13e884@@ 逼近')

t(fn, '<p>: \n                [[em]]柯西-古尔萨定理的证明。[[/em]]\n                考虑一条简单闭曲线 @@math:288:100508@@ 和 @@math:289:9ff9ec@@ 个点 @@math:290:6e720c@@\n                在 @@math:291:68e718@@ 上，通过这些点构造了多边形路径 @@math:292:7b98b7@@\n                则可以证明差值\n                @@math:293:2a234c@@\n                可以随着 @@math:294:d16fae@@ 变得任意小。\n                因此，由 [[strong]]引理 2[[/strong]]，@@math:295:96a46c@@\n                对任意 @@math:296:457393@@ 成立。于是\n                @@math:297:8651aa@@ @@math:298:2ba2a0@@')

t(fn, '<p>: \n                柯西-古尔萨定理已通过多种方法得到证明。\n                例如，已有专门针对矩形或圆盘的证明（参见 [[[a href="#brown2009"]]3[[/a]], [[a href="#marsden1999"]]10[[/a]]]）。\n                除此之外，该定理还有许多其他证明。\n                值得注意的是，John D. Dixon 给出了一个仅依赖于\n                凸集中复变函数理论基本概念的简洁优雅的证明\n                [[[a href="#dixon1971"]]6[[/a]]]。\n                另一方面，Rudolf Výborný 给出了一个基于\n                可微同伦的证明 [[[a href="#vyborny1979"]]14[[/a]]]。')

t(fn, '<h2>: 参考文献')

t(fn, '<li>: Bottazzini, U. (1984). [[em]]The higher calculus: a history of real and complex analysis from Euler to Weierstrass[[/em]]. New York : Springer-Verlag. [[a href="https://archive.org/details/highercalculushi0000bott/mode/2up" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Borger, R. L. (1921). On the Cauchy-Goursat theorem, [[em]]Bulletin of the American Mathematical Society[[/em]], Vol. 27, No. 7, pp. 325-329.\n                  [[a href="https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-27/issue-7/On-the-Cauchy-Goursat-theorem/bams/1183425654.full" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Brown, J. W., Churchill, R. V. (2009). [[em]]Complex Variables and Applications.[[/em]] 8th Edition. New\n                  York: McGraw-Hill Higher Education.')

t(fn, '<li>: Cauchy, A. (1814). [[em]]Mémoire sur la théorie des intégrales définies,[[/em]]\n                  in Œuvres complètes d\'Augustin Cauchy, @@math:299:2a3ba3@@ série, vol. I, Gauthier Villars, Paris. [[a href="https://doi.org/10.1017/CBO9780511702174" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Cauchy, A. (1825). [[em]]Mémoire sur les intégrales définies, prises entre des limites imaginaires,[[/em]]\n                  in Œuvres complètes d\'Augustin Cauchy, @@math:300:936d2a@@ série, vol. XV, Gauthier Villars, Paris. [[a href="https://archive.org/details/mmoiresurlesin00cauc/mode/2up" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Dixon, J. D. (1971). A brief proof of Cauchy\'s integral theorem, [[em]]Proceedings of the American Mathematical Society[[/em]], Vol. 29, No. 3, pp. 625-626.\n                  [[a href="https://doi.org/10.2307/2038614" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Goursat, E. (1884). Démonstration du théorème de Cauchy. [[em]]Acta Mathematica[[/em]], 4, pp. 197-200.\n                  [[a href="https://link.springer.com/article/10.1007/BF02418419" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Goursat, E. (1900).  Sur la définition générale des fonctions analytiques, d\'après Cauchy, [[em]]Transactions of the American Mathematical Society[[/em]], Vol. 1, No. 1, pp. 14-16.\n                  [[a href="https://doi.org/10.2307/1986398" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Hance-Olsen, H. (2008). On Goursat\'s Proof of Cauchy\'s Integral Theorem, [[em]]The American Mathematical Monthly[[/em]], 115, pp. 648-652.\n                  [[a href="https://www.jstor.org/stable/27642560" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Marsden, J. E. &amp; Hoffman, M. J. (1999) [[em]]Basic Complex Analysis.[[/em]] (3rd ed.) New York: W. H. Freeman and Co.')

t(fn, '<li>: Moore, E. H. (1900). A Simple Proof of the Fundamental Cauchy-Goursat Theorem, [[em]]Transactions of the American Mathematical Society[[/em]], Vol. 1, No. 4, pp. 499-506.\n                  [[a href="https://doi.org/10.2307/1986368" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Pringsheim, A. (1901). Ueber den Goursat\'schen Beweis des Cauchy\'schen Integralsatzes, [[em]]Transactions of the American Mathematical Society[[/em]], Vol. 2, No. 4, pp. 413-421.\n                  [[a href="https://doi.org/10.2307/1986254" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Smithies, F. (1997). [[em]]Cauchy and the Creation of Complex Function Theory.[[/em]] UK: Cambridge University Press.\n                  [[a href="https://archive.org/details/cauchycreationof0000smit/mode/2up" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

t(fn, '<li>: Výborný, R. (1979). On the Use of a Differentiable Homotopy in the Proof of the Cauchy Theorem, [[em]]The American Mathematical Monthly[[/em]], Vol. 86, No. 5, pp. 380-382.\n                  [[a href="https://doi.org/10.2307/2321099" target="_blank"]][[i class="fas fa-external-link-alt"]][[/i]][[/a]]')

# Last block for this file (should be navigation)
t(fn, '<p>: 柯西积分公式 [[i class="fa-solid fa-angles-right"]][[/i]]\n\n\nReturn ONLY a JSON array of translated strings, one per block, in the same order.')

print(f"cauchy_goursat_theorem.html: {len(TRANSLATIONS[fn])} translations registered")
