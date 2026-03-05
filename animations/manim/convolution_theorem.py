"""
畳み込み演算がシフト演算子の固有ベクトルによって対角化され、
計算量が O(n^2) から O(n log n) に削減される様子を視覚的かつ数学的な過程を追って表現するアニメーション。
"""

from manim import *

class ConvolutionDiagonalization(Scene):
    def construct(self):
        # --------------------------------------------------
        # 1. イントロダクション
        # --------------------------------------------------
        # タイトルの配置を少し下げて余裕を持たせます
        title = Text("Convolution Theorem", font_size=40).to_edge(UP, buff=0.3)
        subtitle = Text("Diagonalizing the Convolution with the Shift Operator", font_size=20, color=BLUE).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Write(subtitle))
        self.wait(1.5)

        # ベクトルの配置（全体的に少し上に引き上げつつ、横の広がりを少し調整します）
        vec_p = Matrix([["p_0"], ["p_1"], ["\\vdots"], ["p_n"]]).scale(0.8).shift(LEFT * 4.0 + UP * 1.5)
        vec_q = Matrix([["q_0"], ["q_1"], ["\\vdots"], ["q_n"]]).scale(0.8).shift(RIGHT * 4.0 + UP * 1.5)

        lbl_p = MathTex("p \\in \\mathbb{C}^{n+1}").scale(0.8).next_to(vec_p, UP, buff=0.2)
        lbl_q = MathTex("q \\in \\mathbb{C}^{n+1}").scale(0.8).next_to(vec_q, UP, buff=0.2)

        self.play(Create(vec_p), Create(vec_q), Write(lbl_p), Write(lbl_q))
        self.wait(1)

        # --------------------------------------------------
        # 2. 直接畳み込み (O(N^2))
        # --------------------------------------------------
        conv_text = Text("1. Direct Convolution", font_size=32).move_to(title.get_center())
        self.play(
            ReplacementTransform(title, conv_text),
            FadeOut(subtitle)
        )

        cross_lines = VGroup()
        entries_p = vec_p.get_entries()
        entries_q = vec_q.get_entries()

        for p_elem in [entries_p[0], entries_p[1], entries_p[3]]:
            for q_elem in [entries_q[0], entries_q[1], entries_q[3]]:
                line = Line(p_elem.get_right(), q_elem.get_left(), color=YELLOW, stroke_opacity=0.3)
                cross_lines.add(line)

        self.play(Create(cross_lines, run_time=2))
        complex_direct = Text("Cross Multiplications (Sliding Window): O(n²)", color=RED, font_size=24).shift(DOWN * 0.2)
        self.play(Write(complex_direct))
        self.wait(2)

        # --------------------------------------------------
        # 3. Fourier Matrixによる基底変換の説明
        # --------------------------------------------------
        self.play(FadeOut(cross_lines), FadeOut(complex_direct), FadeOut(conv_text))

        shift_text = Text("2. Basis Change (Fourier Matrix)", font_size=32).move_to(conv_text.get_center())
        self.play(Write(shift_text))

        # 行列の成分表示（ω^(i·j)形式で(i,j)成分を明示）
        f_matrix_comp = MathTex(
            "F = \\begin{bmatrix} "
            "\\omega^{0 \\cdot 0} & \\omega^{0 \\cdot 1} & \\cdots & \\omega^{0 \\cdot n} \\\\ "
            "\\omega^{1 \\cdot 0} & \\omega^{1 \\cdot 1} & \\cdots & \\omega^{1 \\cdot n} \\\\ "
            "\\vdots & \\vdots & \\ddots & \\vdots \\\\ "
            "\\omega^{n \\cdot 0} & \\omega^{n \\cdot 1} & \\cdots & \\omega^{n \\cdot n} "
            "\\end{bmatrix} "
            "\\quad \\left( \\omega = e^{i \\frac{2\\pi}{n+1}} \\right)"
        ).scale(0.65).move_to(ORIGIN).shift(UP * 0.2)

        # 背景のボックスで読みやすくする
        f_box = SurroundingRectangle(f_matrix_comp, color=WHITE, fill_color=BLACK, fill_opacity=0.9, buff=0.28)

        self.play(Create(f_box), Write(f_matrix_comp))
        self.wait(3.5)

        # 成分表示から列ベクトル表示への切り替え
        f_matrix_col = MathTex(
            "F = \\begin{bmatrix} | & | & & | \\\\ v_0 & v_1 & \\cdots & v_n \\\\ | & | & & | \\end{bmatrix}"
        ).scale(0.85).move_to(f_matrix_comp.get_center())

        f_matrix_sub = Text(
            "v_k : Eigenvectors of the Shift Operator",
            font_size=20,
            color=BLUE_B
        ).next_to(f_box, DOWN, buff=0.2)  # f_box の下に配置して枠線との重なりを防ぐ

        self.play(
            ReplacementTransform(f_matrix_comp, f_matrix_col),
            Write(f_matrix_sub)
        )
        self.wait(3.5)
        self.play(FadeOut(f_box), FadeOut(f_matrix_col), FadeOut(f_matrix_sub))

        # --------------------------------------------------
        # 3.5. What is Shift Operator? (補足アニメーション)
        # --------------------------------------------------
        # Fの矢印を出す前に、Sの役割を解説する
        so_title = Text("What is the Shift Operator S ?", font_size=32, color=YELLOW).move_to(ORIGIN).shift(UP * 0.5)
        self.play(Write(so_title))

        # pベクトルを複製して中央に持ってくる
        p_demo = vec_p.copy().move_to(ORIGIN).shift(DOWN * 1.5 + LEFT * 1.5)
        p_demo_label = MathTex("p =").scale(0.8).next_to(p_demo, LEFT)

        # S(p)のベクトル（中身がシフトしている）を作成
        sp_demo = Matrix([["p_n"], ["p_0"], ["\\vdots"], ["p_{n-1}"]]).scale(0.8).next_to(p_demo, RIGHT, buff=1.5)
        sp_demo_label = MathTex("Sp =").scale(0.8).next_to(sp_demo, LEFT)

        self.play(Create(p_demo), Write(p_demo_label))
        self.wait(1)

        # Sを適用するアニメーション
        # 各要素がどう移動するかを矢印で示す
        p_entries = p_demo.get_entries()
        sp_entries = sp_demo.get_entries()

        shift_arrows = VGroup()
        # p_0 -> 2番目, p_1 -> 3番目...
        shift_arrows.add(Arrow(p_entries[0].get_right(), sp_entries[1].get_left(), color=BLUE, buff=0.1, max_tip_length_to_length_ratio=0.15))
        shift_arrows.add(Arrow(p_entries[1].get_right(), sp_entries[2].get_left(), color=BLUE, buff=0.1, max_tip_length_to_length_ratio=0.15))
        # p_n (最後) -> 1番目 (先頭)
        shift_arrows.add(Arrow(p_entries[3].get_right(), sp_entries[0].get_left(), color=RED, buff=0.1, path_arc=-1.5, stroke_width=3))

        self.play(Write(sp_demo_label), Create(sp_demo), Create(shift_arrows))

        so_desc = Text("Cyclic shift of indices", font_size=24, color=WHITE).next_to(sp_demo, DOWN, buff=0.5)
        self.play(Write(so_desc))
        self.wait(3.5)

        self.play(
            FadeOut(so_title), FadeOut(p_demo), FadeOut(p_demo_label),
            FadeOut(sp_demo), FadeOut(sp_demo_label), FadeOut(shift_arrows), FadeOut(so_desc)
        )

        # --------------------------------------------------
        # 新しい基底でのベクトル Fp, Fq の表現 (線形結合)
        # --------------------------------------------------
        arrow_p = Arrow(vec_p.get_bottom(), vec_p.get_bottom() + DOWN * 1.5, color=BLUE)
        arrow_q = Arrow(vec_q.get_bottom(), vec_q.get_bottom() + DOWN * 1.5, color=BLUE)

        lbl_fp = MathTex("F").scale(1.2).next_to(arrow_p, RIGHT)
        lbl_fq = MathTex("F").scale(1.2).next_to(arrow_q, LEFT)

        self.play(GrowArrow(arrow_p), GrowArrow(arrow_q), Write(lbl_fp), Write(lbl_fq))

        # Fによる変換後のベクトル表現と、各列ベクトル（基底）の線形結合としての解釈
        vec_fp = Matrix([["\\hat{p}_0"], ["\\hat{p}_1"], ["\\vdots"], ["\\hat{p}_n"]]).scale(0.8).next_to(arrow_p, DOWN, buff=0.1)
        vec_fq = Matrix([["\\hat{q}_0"], ["\\hat{q}_1"], ["\\vdots"], ["\\hat{q}_n"]]).scale(0.8).next_to(arrow_q, DOWN, buff=0.1)

        # それぞれ Fp, Fq であり、C^(n+1) の元であることを明示
        lbl_fp_def = MathTex("Fp \\in \\mathbb{C}^{n+1}").scale(0.8).next_to(vec_fp, LEFT, buff=0.3)
        lbl_fq_def = MathTex("Fq \\in \\mathbb{C}^{n+1}").scale(0.8).next_to(vec_fq, RIGHT, buff=0.3)

        eq_p = MathTex("\\hat{p} = \\sum_{k=0}^n p_k v_k").scale(0.65).next_to(vec_fp, DOWN, buff=0.2)
        eq_q = MathTex("\\hat{q} = \\sum_{k=0}^n q_k v_k").scale(0.65).next_to(vec_fq, DOWN, buff=0.2)

        self.play(Create(vec_fp), Create(vec_fq), Write(lbl_fp_def), Write(lbl_fq_def))
        self.wait(1)
        self.play(Write(eq_p), Write(eq_q))
        self.wait(3)

        # --------------------------------------------------
        # 4. 対角化と成分ごとの積 (Convolution定理の導出)
        # --------------------------------------------------
        diag_text = Text("3. Diagonalizing the Convolution", font_size=32).move_to(shift_text.get_center())
        self.play(ReplacementTransform(shift_text, diag_text))

        # 畳み込みがなぜ各成分の積になるのかの数式ステップ
        conv_derivation_1 = MathTex(
            "(p * q) = ", "C_p", " q = \\sum_{j=0}^{n} p_j (S^j q)"
        ).scale(0.6).move_to(ORIGIN).shift(UP * 0.7)

        conv_derivation_2 = MathTex(
            "\\text{Since } v_k \\text{ is an eigenvector: } S^j v_k = \\omega^{kj} v_k"
        ).scale(0.6).next_to(conv_derivation_1, DOWN, buff=0.25)

        conv_derivation_3 = MathTex(
            "\\Rightarrow C_p(v_k) = \\left( \\sum_{j=0}^n p_j \\omega^{kj} \\right) v_k = \\hat{p}_k v_k"
        ).scale(0.6).next_to(conv_derivation_2, DOWN, buff=0.25)

        conv_derivation_4 = MathTex(
            "\\therefore ", "F(p * q)_k", " = \\hat{p}_k \\cdot \\hat{q}_k"
        ).scale(0.6).next_to(conv_derivation_3, DOWN, buff=0.35)

        derivation_group = VGroup(conv_derivation_1, conv_derivation_2, conv_derivation_3, conv_derivation_4)
        # d_box 自体も少し小さくして F の文字や括弧との重なりを回避
        d_box = SurroundingRectangle(derivation_group, color=WHITE, fill_color=BLACK, fill_opacity=0.9, buff=0.28, stroke_width=2)

        # C_p に関する補足説明
        c_p_circle = Ellipse(width=conv_derivation_1[1].width * 1.5, height=conv_derivation_1[1].height * 1.5, color=YELLOW).move_to(conv_derivation_1[1])
        c_p_circle.set_stroke(width=1)
        cp_explanation = Tex(r"$C_p = \sum p_j S^j$ : Linear Map (Polynomial of $S$)", font_size=24, color=YELLOW).next_to(d_box, UP, buff=0.2)
        cp_arrow = Arrow(cp_explanation.get_bottom(), c_p_circle.get_top(), color=YELLOW, buff=0.1)

        # F(p*q)_k の補足説明 (Underline と説明テキスト)
        # 既に上で "\therefore ", "F(p * q)_k", " = \hat{p}_k \cdot \hat{q}_k" に分割済みなので、そのまま利用します。

        # F(p*q)_k (インデックス 1) に下線を引く
        fk_underline = Underline(conv_derivation_4[1], color=YELLOW, stroke_width=2)

        # 枠線の外側（下）に補足テキストを配置
        fk_explanation = Text("k-th component of convolution(p,q)\n in the Fourier basis", font_size=16, color=YELLOW, line_spacing=0.8).next_to(d_box, DOWN, buff=0.2)
        fk_arrow = Arrow(fk_explanation.get_top(), fk_underline.get_bottom(), color=YELLOW, buff=0.1)

        self.play(Create(d_box))
        self.play(Write(conv_derivation_1))
        self.wait(1)

        # ここでC_pを囲い、補足を表示
        self.play(Create(c_p_circle))
        self.play(Write(cp_explanation), GrowArrow(cp_arrow))
        self.wait(2.5)

        self.play(Write(conv_derivation_2))
        self.wait(1.5)
        self.play(Write(conv_derivation_3))
        self.wait(2)
        self.play(Write(conv_derivation_4))

        # 下線と補足を表示
        self.play(Create(fk_underline))
        self.play(Write(fk_explanation), GrowArrow(fk_arrow))
        self.wait(4)

        self.play(FadeOut(d_box), FadeOut(derivation_group), FadeOut(c_p_circle), FadeOut(cp_explanation), FadeOut(cp_arrow),
                  FadeOut(fk_underline), FadeOut(fk_explanation), FadeOut(fk_arrow))

        # Pointwise operations (平行線) の描画
        diag_text_2 = Text("Pointwise Multiplication!", font_size=32, color=GREEN).move_to(diag_text.get_center())
        self.play(ReplacementTransform(diag_text, diag_text_2))

        parallel_lines = VGroup()
        f_entries_p = vec_fp.get_entries()
        f_entries_q = vec_fq.get_entries()

        for i in [0, 1, 3]:
            line = Line(f_entries_p[i].get_right(), f_entries_q[i].get_left(), color=GREEN, stroke_width=4)
            parallel_lines.add(line)

        self.play(Create(parallel_lines, run_time=1.5))
        complex_diag = Text("Parallel operations: O(n)", color=GREEN, font_size=24).next_to(parallel_lines, DOWN, buff=1.0)
        self.play(FadeIn(complex_diag))
        self.wait(2)

        # --------------------------------------------------
        # 5. 計算量 O(n log n) の導出と結論
        # --------------------------------------------------
        self.play(FadeOut(diag_text_2), FadeOut(complex_diag))

        # 導出ステップを中央に表示
        deriv_title = Text("Time Complexity Derivation", font_size=28, color=YELLOW).move_to(ORIGIN).shift(UP * 0.4)
        step1 = Tex("1. FFT ($p \\to \\hat{p}$, $q \\to \\hat{q}$) : ", "$O(n \\log n)$").scale(0.75).next_to(deriv_title, DOWN, aligned_edge=LEFT, buff=0.3)
        step2 = Tex("2. Pointwise multiplication : ", "$O(n)$").scale(0.75).next_to(step1, DOWN, aligned_edge=LEFT, buff=0.2)
        step3 = Tex("3. Inverse FFT ($\\Rightarrow$ result) : ", "$O(n \\log n)$").scale(0.75).next_to(step2, DOWN, aligned_edge=LEFT, buff=0.2)

        deriv_group = VGroup(deriv_title, step1, step2, step3)
        # X軸の中心に合わせる
        deriv_group.move_to(ORIGIN)
        deriv_bg = SurroundingRectangle(deriv_group, color=WHITE, fill_color=BLACK, fill_opacity=0.9, buff=0.068, stroke_width=2)

        self.play(Create(deriv_bg))
        self.play(Write(deriv_title))
        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Write(step3))
        self.wait(3.5)
        self.play(FadeOut(deriv_bg), FadeOut(deriv_group))

        # トータルの計算量（重ならないようにスケールと位置を調整）
        algo_text = Text("Total Time (with FFT): O(n log n)", color=YELLOW, font_size=28)
        # title の位置よりさらに少し下げて完全に独立させる
        algo_title_pos = title.get_center() + DOWN * 0.4
        algo_text.move_to(algo_title_pos)

        # 枠の見切れ防止のため buff を小さくする
        box = SurroundingRectangle(algo_text, color=YELLOW, buff=0.15)

        self.play(Write(algo_text))
        self.play(Create(box))

        self.wait(4)
