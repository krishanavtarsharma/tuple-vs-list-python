import streamlit as st
import sys
import pandas as pd

# Page Setup
st.set_page_config(page_title="Advanced Tuple vs List Comparison", layout="wide")
st.title("🧠 Tuple vs List - Deep Technical Comparison in Python")
st.markdown("Understand the *real differences* between List and Tuple using **live code**, **memory metrics**, and **method comparison**.")

# ----------- Step 1: Basic Definitions
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

st.subheader("🔹 Syntax & Structure")
col1, col2 = st.columns(2)
col1.code(f"List  : {my_list} ➝ Mutable ✅")
col2.code(f"Tuple : {my_tuple} ➝ Immutable ❌")

st.info("👉 **Lists** use square brackets `[]` and can be modified. **Tuples** use round brackets `()` and cannot be changed.")

# ----------- Step 2: Mutability Interactive Demo
st.subheader("🔹 Mutability Demo (Try Changing List/Tuple)")
user_value = st.number_input("🔢 Try changing the first value of both:", value=10)

col1, col2 = st.columns(2)
with col1:
    mutable_list = [1, 2, 3]
    mutable_list[0] = user_value
    st.success(f"✅ List Changed: {mutable_list}")

with col2:
    immutable_tuple = (1, 2, 3)
    try:
        immutable_tuple[0] = user_value
    except TypeError:
        st.error("❌ Tuple Cannot Be Changed!")
        st.code("TypeError: 'tuple' object does not support item assignment")

# ----------- Step 3: Memory Usage
st.subheader("🔹 Memory Usage (in Bytes)")
list_size = sys.getsizeof(my_list)
tuple_size = sys.getsizeof(my_tuple)

chart_df = pd.DataFrame({
    "Data Type": ["List", "Tuple"],
    "Memory (Bytes)": [list_size, tuple_size]
})
st.bar_chart(chart_df.set_index("Data Type"))

st.markdown(f"📦 **List uses** `{list_size}` bytes | **Tuple uses** `{tuple_size}` bytes")

# ----------- Step 4: Removed (Performance)

# ----------- Step 5: Method Comparison
st.subheader("🔹 Methods Comparison")

list_methods = set(dir(my_list))
tuple_methods = set(dir(my_tuple))
extra_list = sorted(list_methods - tuple_methods)
common_methods = sorted(list_methods & tuple_methods)

col1, col2 = st.columns(2)
with col1:
    st.write("🔧 **List-only Methods**")
    st.code(extra_list)

with col2:
    st.write("🔁 **Common Methods**")
    st.code(common_methods)

# ----------- Step 6: Summary Table
st.subheader("📊 Final Summary Table")

summary_df = pd.DataFrame({
    "Feature": [
        "Mutability",
        "Syntax",
        "Memory Usage",
        "Methods Available",
        "Use Case"
    ],
    "List": [
        "✅ Mutable",
        "[1, 2, 3]",
        f"{list_size} bytes",
        "Many (`append`, `remove`, etc.)",
        "Dynamic, changing data"
    ],
    "Tuple": [
        "❌ Immutable",
        "(1, 2, 3)",
        f"{tuple_size} bytes",
        "Few (`count`, `index`)",
        "Fixed, constant data"
    ]
})
st.dataframe(summary_df)

# ----------- Step 7: Downloadable Summary
st.subheader("📥 Download Summary as TXT")

summary_txt = f"""
Tuple vs List - Technical Comparison

1. Mutability:
   - List is Mutable ✅
   - Tuple is Immutable ❌

2. Memory Usage:
   - List: {list_size} bytes
   - Tuple: {tuple_size} bytes

3. Methods:
   - List: {len(extra_list)} extra methods
   - Common: {len(common_methods)} shared methods

4. Use Case:
   - List for dynamic, modifiable data
   - Tuple for fixed, constant data

Built with ❤️ using Python and Streamlit.
"""

st.download_button("📄 Download Summary", summary_txt, file_name="tuple_vs_list_summary.txt")

st.markdown("---")
st.caption("✅ Built with Python, Streamlit, sys, and pandas — by Krishan Sharma")
