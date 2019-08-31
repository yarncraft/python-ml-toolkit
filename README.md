# python-ml-toolkit

<img src="https://res.cloudinary.com/yarncraft/image/upload/v1567244000/example_vhwlns.png" width="540" align="right" title="Example">

Included:

- Pandas
- Numpy
- Sklearn
- Pydataset
- Prettyprinter
- Pandas-Profiler

---

To get started locally make sure to install [poetry](https://poetry.eustace.io) and Python 3.7.

```
poetry install
poetry run python src/main/main.py
```

To get started with Docker (easy):

```
docker build -t ml .
docker run -it ml:latest bash
python run src/main/main.py
```

I recommend using Kite in VSCode as it greatly speeds up ML programming.

Pandas Profiler is one of the hidden gems which gives you a dashboard with some basis dataset stats, a html report will automatically be generated in your root folder:

<img src="https://res.cloudinary.com/yarncraft/image/upload/v1567243998/dashboard_yubone.png" width="1000" title="Example">
