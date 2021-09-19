```bash
pip install sklearn
pip install dvc
pip install dvc[gdrive]
git init
dvc init
dvc add data_given/sample.csv
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jayaram87/dvc_basics.git
git push -u origin main
```