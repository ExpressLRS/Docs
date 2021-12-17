import shutil, os, glob

langs = {'en'}

assetDir = 'docs/assets/images'

# for filename in glob.iglob('assetsFolder', recursive=True):


for subdir, dirs, files in os.walk(assetDir):
    for file in files:
        infilename = os.path.join(subdir, file)
        if not os.path.isfile(infilename): continue
        valid = True
        for test in langs:                                      # test if we have any localized versions
            if '.' + test + '.' in infilename:
                valid = False
            if not valid: continue                              
        if not valid: continue                                  # do not localize to other languages if already localized
        for lang in langs:
            newname = infilename.replace('.', '.'+lang+'.')
            shutil.copy(infilename, newname)