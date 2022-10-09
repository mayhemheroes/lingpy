FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /lingpy
WORKDIR /lingpy
RUN python3 -m pip install -r requirements.txt && python3 -m pip install . && chmod +x fuzz/lingpy_fuzz.py

ENTRYPOINT [ ]
CMD ["/lingpy/fuzz/lingpy_fuzz.py"]