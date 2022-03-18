FROM python:3.9.1
ENV PY_CUSTOM_SCRIPTS_ROOT_PATH=/zpy_python_scripts_hub
WORKDIR /zpy_script_handler
COPY ./requirements.txt /zpy_script_handler/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /zpy_script_handler/requirements.txt
COPY ./app /zpy_script_handler/app
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8004"]
