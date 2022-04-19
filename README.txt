# Datenvisualisierung mit Python

Dies ist ein [(Jupyter-)Notebook](https://jupyter.org/) zur Einführung in die Datenvisualisierung mit Python. Hierbei wird anhand des [Iris-Datensatzes](https://www.kaggle.com/uciml/iris) stichprobenartig auf mehrere Arten von Graphen und Visualisierungstechniken eingegangen.

## 1 Was bietet Python an?

Abhängig vom eigenen Vorhaben bietet Python für fast jede Idee eine Bibliothek an. Die bekanntesten Bibliotheken für grundlegende Darstellungen sind [Matplotlib](https://matplotlib.org/) und [Seaborn](https://seaborn.pydata.org/). Möchte man derartige Graphen in seiner eigenen Web-Applikation integrieren, können außerdem auch Bibliotheken, wie [Plotly](https://plotly.com/) und [Bokeh](https://docs.bokeh.org/en/latest/index.html), relevant sein.

Unser Ziel ist es zunächst, einfache Graphen im Python-Programm darzustellen, weswegen insbesondere Matplotlib und Seaborn in Frage kommen. Gegebenenfalls lassen sich auch Daten direkt über Extensions von [Pandas](https://pandas.pydata.org/) plotten.

## 2 Matplotlib, Seaborn, oder beides?

Seaborn baut auf Matplotlib auf und führt zusätzliche Diagrammtypen ein, welche auch um einiges ansprechender aussehen (mit weniger Codezeilen -> geringerer Aufwand). Aufgrund der Tatsache, dass Seaborn auf der Basis von Matplotlib gebaut wurde, ist es vorteilhaft, vor dem Verwenden von Seaborn die Grundlagen von Matplotlib zu beherrschen. Der Hauptgrund, warum empfohlen wird, beides zu lernen, ist aber, dass zum Teil Matplotlib verwendet wird, um Outputs von Seaborn-Plots anzupassen. 

In diesem Notebook wird sowohl Matplotlib, als auch Seaborn verwendet.

## 3 Setup und Nutzung
### 3 a) Einfache Betrachtung

Falls ihr euch einfach das Notebook ansehen wollt, klickt auf die Datei ``py_data_viz.ipynb``. Bitte nicht vergessen, die Kommentare zu lesen!

### 3 b) Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lunghungnguyen/py-data-viz/master)

Um das Notebook testweise im Browser zu nutzen (ohne Installationen), auf den Button ``launch binder`` klicken. 

[Binder](https://mybinder.org/) erstellt dann ein [Docker](https://docs.docker.com/)-Image auf der Basis von der ``environment.yml``. Nachdem alles fertig geladen hat, kann dann die ``py_data_viz.ipynb`` aufgerufen und alles beliebig innerhalb einer Session getestet werden.

### 3 c) Git clone / fork

Falls ihr kein Fan von Drittanbietern seid, könnt ihr natürlich dieses Repository einfach mit ``git clone <repo_link>`` klonen, oder direkt über das Interface forken (zu eurem eigenen Account rüberkopieren).

Um das Ganze dann zum Laufen zu bringen, braucht ihr [Anaconda](https://www.anaconda.com/), bzw. [Miniconda](https://docs.conda.io/en/latest/miniconda.html), auf eurem Rechner. Windows-Nutzer müssen conda dann außerdem zu den Systemumgebungsvariablen hinzufügen. (Für den Path einfach ``where conda`` im Anaconda Prompt eingeben)

Sobald ihr alles konfiguriert habt, müsst ihr noch [Numpy](https://anaconda.org/anaconda/numpy), [Seaborn](https://anaconda.org/anaconda/seaborn), [Matplotlib](https://anaconda.org/anaconda/matplotlib) und [Pandas](https://anaconda.org/anaconda/pandas) über das Anaconda Prompt installieren. Alternativ könnt ihr auch alle Dependencies über ein [Conda Environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) installieren. 

Startet ihr jetzt abschließend mein Notebook und führt die Imports aus, sollten keine Fehlermeldungen auftreten, falls ihr alles richtig gemacht habt. Glückwunsch und viel Spaß!

___

_Kontakt: lungnguyenhung@gmail.com_
