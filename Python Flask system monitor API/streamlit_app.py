import streamlit as st
import requests

# Fetch data from Flask API
cpu_usage = requests.get("http://localhost:5000/api/system/cpu").json()
ram_usage = requests.get("http://localhost:5000/api/system/ram").json()
disk_usage = requests.get("http://localhost:5000/api/system/disk").json()
gpu_usage = requests.get("http://localhost:5000/api/system/gpu").json()

# Streamlit page title
st.title("System Resource Dashboard")
st.divider()

# Create columns for better layout
col1, col2 = st.columns(2)

# Display CPU and RAM in one column
with col1:
    st.subheader("CPU Usage")
    st.metric(label="CPU Percent", value=f"{cpu_usage['cpu_percent']}%")

    st.subheader("RAM Usage")
    st.metric(label="RAM Total", value=f"{ram_usage['total'] / (1024 ** 3):.2f} GB")
    st.metric(label="RAM Available", value=f"{ram_usage['available'] / (1024 ** 3):.2f} GB")
    st.metric(label="RAM Usage", value=f"{ram_usage['percent']}%")

# Display Disk and GPU in the second column
with col2:
    st.subheader("Disk Usage")
    st.metric(label="Disk Total", value=f"{disk_usage['total'] / (1024 ** 3):.2f} GB")
    st.metric(label="Disk Used", value=f"{disk_usage['used'] / (1024 ** 3):.2f} GB")
    st.metric(label="Disk Free", value=f"{disk_usage['free'] / (1024 ** 3):.2f} GB")
    st.metric(label="Disk Usage", value=f"{disk_usage['percent']}%")

    if "error" not in gpu_usage:
        st.subheader("GPU Usage")
        for gpu in gpu_usage:
            st.metric(label=f"GPU: {gpu['name']}", value=f"Load: {gpu['load']}%")
            st.metric(label="GPU Memory Used", value=f"{gpu['memoryUsed']} MB")
            st.metric(label="GPU Memory Free", value=f"{gpu['memoryFree']} MB")
            st.metric(label="GPU Temperature", value=f"{gpu['temperature']}°C")
