from setuptools import setup, Extension, find_packages

setup(
    name="videostream",
    version="0.1.0",
    author="Javad Shafique",
    author_email="javad.asgari@simplyprint.io",
    description="A Python package for streaming video with Python bindings.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    ext_modules=[
        Extension(
            "videostream",
            sources=[
                "src/bindings.c",
                "src/VideoStream.c",
                "src/FrameEncoding.c"
            ],
            libraries=['avformat', 'avcodec', 'avutil'],
        )
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
