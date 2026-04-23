from setuptools import setup, find_packages
import os

# Read the README for the long description
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="unsloth",
    version="2024.1.0",
    description="2x faster, 60% less memory LLM finetuning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Unsloth AI",
    author_email="danielhanchen@gmail.com",
    url="https://github.com/unslothai/unsloth",
    license="Apache 2.0",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.38.0",
        "datasets>=2.16.0",
        "sentencepiece>=0.1.99",
        "tqdm",
        "psutil",
        "wheel>=0.42.0",
        "packaging>=23.1",
        "tyro>=0.5.7",
        "accelerate>=0.26.0",
        "peft>=0.8.0",
        "trl>=0.7.9",
        "xformers",
        "bitsandbytes",
        "protobuf<4.0.0",
        "huggingface_hub",
        "hf_transfer",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "isort",
            "flake8",
        ],
        "colab": [
            "triton",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "llm",
        "lora",
        "transformers",
        "triton",
    ],
    entry_points={
        "console_scripts": [
            "unsloth=unsloth.cli:main",
        ],
    },
)
