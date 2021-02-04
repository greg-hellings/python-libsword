import subprocess
import setuptools

def parse_pkgconfig():
    output = subprocess.getoutput('pkg-config --cflags --libs sword')
    print("Parsing {} for pkg-config flags".format(output))
    args = {'include_dirs': [], 'libraries': ['sword'], 'library_dirs': []}
    mapping = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    for flag in output.strip().split():
        args[mapping[flag[:2]]].append(flag[2:])
    print(args)
    return args

if __name__ == "__main__":
    args = parse_pkgconfig()
    setuptools.setup(
        use_scm_version={"local_scheme": "no-local-version"},
        setup_requires=["setuptools_scm[toml]>=3.5.0"],
        include_dirs=args['include_dirs'],
        ext_modules = [setuptools.Extension('_Sword',['Sword.cxx'],
            libraries=args['libraries'],
            library_dirs=args['library_dirs'],
        )]
    )
