# jupyter-central

This repo is an attempt to centralize my little collection of [jupyter notebooks](https://github.com/jupyter/notebook) in one place. This was originally based on the idea that my notebooks would be _hosted_ in several locations by several third parties to avoid setting up my own public-facing server.

So far, I have only hosted my notebooks on Azure (see “notebooks.azure.com” below) and effectively [here](https://github.com/BryanWilhite/jupyter-central#README) in this repo on GitHub.

## my cross-platform desktop setup

My studio Jupyter environment is built on top of [Anaconda which is installed via Chocolatey on Windows](https://chocolatey.org/packages/anaconda3). (See “installing Anaconda on Ubuntu” below.) I then follow along with Microsoft’s plans for [.NET Interactive Notebooks](https://github.com/dotnet/interactive) by installing the 32-bit version of the .NET SDK 3.x and running the following:

```powershell
 dotnet tool install --global Microsoft.dotnet-interactive
 dotnet interactive jupyter install
 jupyter kernelspec list

 PS C:\Users\rasx> jupyter kernelspec list
Available kernels:
  .net-csharp        AppData\Roaming\jupyter\kernels\.net-csharp
  .net-fsharp        AppData\Roaming\jupyter\kernels\.net-fsharp
  .net-powershell    AppData\Roaming\jupyter\kernels\.net-powershell
  python3            c:\tools\Anaconda3\share\jupyter\kernels\python3
```

And, yes, Microsoft has a [Jupyter kernel for PowerShell](https://devblogs.microsoft.com/powershell/public-preview-of-powershell-support-in-jupyter-notebooks/). And do recall that Microsoft wants all of this work on Linux (and the Macintosh) as well.

## installing Anaconda on Ubuntu desktop

“[How to Install Anaconda on Ubuntu 20.04](https://linuxize.com/post/how-to-install-anaconda-on-ubuntu-20-04/)” serves as my guide for setting up Anaconda on Ubuntu desktop:

```bash
sudo apt install \
  libgl1-mesa-glx \
  libegl1-mesa \
  libxrandr2 \
  libxrandr2 \
  libxss1 \
  libxcursor1 \
  libxcomposite1 \
  libasound2 \
  libxi6 \
  libxtst6

wget -P . https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
sha256sum Anaconda3-2020.07-Linux-x86_64.sh
bash Anaconda3-2020.07-Linux-x86_64.sh

anaconda-navigator

conda update --all
```

## notebooks.azure.com

A word from Microsoft:

>The Microsoft Azure Notebooks preview website will be retired on October 9th, 2020.

Going forward, Microsoft recommends [their alternatives](https://notebooks.azure.com/Content/alternatives.html) which include [notebooks in Visual Studio Code](https://docs.microsoft.com/en-us/azure/notebooks/quickstart-export-jupyter-notebook-project#use-notebooks-in-visual-studio-code).

@[BryanWilhite](https://twitter.com/bryanwilhite)
