import streamlit as st

from utils.quiz_loader import (
    load_questions
)

from utils.scoring import (
    calculate_score
)

st.set_page_config(
    page_title=
    "Agentic AI Quiz"
)

st.title(
    "🤖 Agentic AI Quiz"
)

questions = load_questions()

user_answers = []

with st.form(
    "quiz_form"
):

    for idx, q in enumerate(
        questions
    ):

        answer = st.radio(
            q["question"],
            q["options"],
            key=idx
        )

        user_answers.append(
            answer
        )

    submit = st.form_submit_button(
        "Submit Quiz"
    )

if submit:

    score, results = (
        calculate_score(
            questions,
            user_answers
        )
    )

    st.success(
        f"Score: "
        f"{score}/"
        f"{len(questions)}"
    )

    st.divider()

    for result in results:

        if result[
            "is_correct"
        ]:

            st.success(
                result["question"]
            )

        else:

            st.error(
                result["question"]
            )

        st.write(
            "Your Answer:",
            result["selected"]
        )

        st.write(
            "Correct Answer:",
            result[
                "correct_answer"
            ]
        )

        st.info(
            result[
                "explanation"
            ]
        )

        st.divider()