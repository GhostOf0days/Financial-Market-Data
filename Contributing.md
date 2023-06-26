Use this to add your dataset source!: ```| [Folder Name](URL) | Description: N/A | Last Updated: N/A | Hedge Fund Quality (:heavy_check_mark: = yes, :x: = no) |```. Feel free to add a description. The top should contain hedge-fund quality datasets.

Symbols Markdown: Checkmark -  ```:heavy_check_mark:```, ```:x:```

Please run the trimmer.py in the scripts folder prior to creating a pull request.

Large files: Please store the file in a zip folder within the folder for that dataset. If it is still too big, please use Git LFS (Large File System) to store the zip folder that is 100 Mb or larger (see Numerai Training Dataset as an example).

Please track the individual large datasets like this: ```git lfs track "numerai_training_data_int8.csv"```


For files exceeding these [limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) (preferably 2 GB), please compress the file (see compressor.py in the scripts folder) before using Git LFS: 

| Account Type | Git LFS Maximum File Size |
| ------------ | ------------ |
| GitHub Free |	2 GB |
| GitHub Pro | 2 GB | 
| GitHub Team | 4 GB |
| GitHub Enterprise Cloud | 5 GB |

GIT LFS (Large File System) Guides:
[Advanced Reactors and Fuel Cycles Github LFS Guide](https://arfc.github.io/manual/guides/git-lfs)
[Github Docs Git LFS Guide](https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage)
[Atlassian Git LFS Guide](https://www.atlassian.com/git/tutorials/git-lfs)
[Medium Git LFS Guide](https://medium.com/junior-dev/how-to-use-git-lfs-large-file-storage-to-push-large-files-to-github-41c8db1e2d65)