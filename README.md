# 🔐 CipherForge: Boron1 Encryption Algorithm

**A custom 5-layer encryption algorithm** built as part of Year 9 Digital Technologies.

## About

This project implements a multi-layered encryption system that I designed from scratch. Each layer adds a different type of protection, similar to how real encryption algorithms like AES work.

## Algorithm Phases

> [!NOTE]
> You can find more information about algorithms in engine.py, and you can see each algorithm at work in experiment.py.

| Phase | Name            | Status       |
| ----- | --------------- | ------------ |
| 1     | Substitution    | ✅ Completed |
| 2     | Transposition   | ✅ Completed |
| 3     | Key-Dependent   | ✅ Completed |
| 4     | Noise Injection | ✅ Completed |
| 5     | Wild Card       | ✅ Completed |

## Running the Project

> [!CAUTION]
> This is not a cryptographically safe algorithm, and should not be used in any sensitive data. For encrypting data, you should use Advanced Encryption Standard (AES) or Bcrypt and etc.

Step 1. Creating the environment

```
python3 -m venv venv
```

Step 2. Launching the environment

```
source venv/bin/active
```

Step 3. Installing the dependencies

```
pip install -r requirements.txt
```

Step 4. Launching the program

```
python3 app.py
```

## Help

Any advise for common problems or issues.

```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

Mr Jones
[@benpaddlejones](https://github.com/benpaddlejones)

Callen Lin
[@callenlin](https://github.com/callen)

## Version History

- 0.2
  - Various bug fixes and optimizations
  - See [commit change]() or See [release history]() or see [branch]()
- 0.1
  - Initial Release

NOT AVAILABLE AT THE MOMENT

## License

This project is licensed under The GNU GPLv3 License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.

- [Github md syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [TempeHS Python Flask template](https://github.com/TempeHS/TempeHS_Python-Flask_DevContainer)
