import streamlit as st
from ai import generate_sql
from database import execute_query

st.set_page_config(
    page_title="Financial Data SQL Copilot",
    page_icon="📊"
)

st.title("📊 Financial Data SQL Copilot")

st.write(
    "Ask questions about financial data using natural language."
)

question = st.text_input(
    "Ask a financial question:"
)

if st.button("Analyze"):

    if not question:
        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating SQL..."):

            try:

                sql = generate_sql(question)

                st.subheader("Generated SQL")

                st.code(sql, language="sql")

                # Security check
                sql_upper = sql.upper().strip()

                if not sql_upper.startswith("SELECT"):
                    st.error(
                        "Only SELECT queries are allowed."
                    )

                else:

                    forbidden = [
                        "INSERT",
                        "UPDATE",
                        "DELETE",
                        "DROP",
                        "ALTER",
                        "CREATE"
                    ]

                    if any(
                        word in sql_upper
                        for word in forbidden
                    ):

                        st.error(
                            "Unsafe SQL query detected."
                        )

                    else:

                        result = execute_query(sql)

                        st.subheader(
                            "Query Result"
                        )

                        st.dataframe(result)

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )