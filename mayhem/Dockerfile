FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends clang && rm -rf /var/lib/apt/lists/*
RUN pip3 install atheris

COPY . /lingpy
WORKDIR /lingpy
RUN python3 -m pip install -r requirements.txt && python3 -m pip install . && chmod +x fuzz/lingpy_fuzz.py

ENTRYPOINT [ ]
CMD ["/lingpy/fuzz/lingpy_fuzz.py"]
