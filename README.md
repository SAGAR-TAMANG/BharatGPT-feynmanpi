<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi">
    <img src="https://raw.githubusercontent.com/SAGAR-TAMANG/BharatGPT-feynmanpi/main/static/img/pi.png" alt="Logo" height="50">
  </a>

<h3 align="center">BharatGPT Feynman Pi</h3>

  <p align="center">
    India's Answer to the LLM revolution.
    <br />
    <a href="https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/blob/main/README.md"><em>Releasing Soon to Public </em></a> 
    <br />
    <a href="https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/issues">Report Bug</a>
    ·
    <a href="https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/issues">Request Feature</a>
  </p>
</div>

## Screenshots

<img src="https://raw.githubusercontent.com/SAGAR-TAMANG/BharatGPT-feynmanpi/main/static/img/ss.png">

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

(#about-the-project)

This project aims to scrape job listings from Naukri.com using Selenium.

Contributions are welcome! Please see the [Contributing](#contributing) section to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Django Python
* Vanilla HTML, CSS, JS
* Bootstrap 5.3
* HTMX and Hyperscript
* Google Cloud - Gemini API
* Django Sessions
* Django Cors
* Redis Cache
* Postgresql Database

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To run this code locally, follow these steps.

### Prerequisites

* Web Browser

### Installation

1. Clone the repo
    ```
    git clone https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi.git
    ```
2. Go to the project repo folder
    ```
    cd path\to\directory
    ```
3. Create Virtual Env (Recommended)
    ```
    virtualenv venv_name
    ```
4. Install the required Python packages using pip
    ```
    pip install -r 'requirements.txt'
    ```
5. Change main/settings.py file to include your database
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'railway',
            'USER': os.getenv("DBUSER"),
            'PASSWORD': os.getenv("DBPASSWORD"),
            'HOST': os.getenv("DBHOST"),
            'PORT': os.getenv("DBPORT"),
        }
    }
    ```
5. Migrate the databases
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
5. Run the Django development server
    ```
    pip install -r 'requirements.txt'
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Design & Develop the User Interface
- [x] Generate API through Google Cloud for Gemini model.
- [x] Integrate hyperscripts and HTMX to the templates.
- [x] Enable databases and caching
- [x] Add user interactivity and animations in HTMX
- [x] Debug necessary errors
- [ ] Features Update

See the [open issues](https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/issues) for a list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Don't forget to give the project a star! Thank you!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Sagar Tamang - [LinkedIn](https://www.linkedin.com/in/sagar-tmg/) - cs22bcagn033@kazirangauniversity.in

Official Website: [https://sagartamang.com](https://sagartamang.com)

Project Link: [https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi](https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* I would like to take this moment to thank all my dear seniors for guiding and always motativating me; Specifically from The Assam Kaziranga University.
* I would also like to thank Paraj Tamang and Upasana for their valuable inputs during the development of the project.
* Ofcourse, can't forget [ChatGPT](https://chat.openai.com/) for providing helping me debug all the errors.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/SAGAR-TAMANG/BharatGPT-feynmanpi.svg?style=for-the-badge
[contributors-url]: https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SAGAR-TAMANG/BharatGPT-feynmanpi.svg?style=for-the-badge
[forks-url]: https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/network/members
[stars-shield]: https://img.shields.io/github/stars/SAGAR-TAMANG/BharatGPT-feynmanpi.svg?style=for-the-badge
[stars-url]: https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/stargazers
[issues-shield]: https://img.shields.io/github/issues/SAGAR-TAMANG/BharatGPT-feynmanpi.svg?style=for-the-badge
[issues-url]: https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/issues
[license-url]: https://github.com/SAGAR-TAMANG/BharatGPT-feynmanpi/blob/master/license.txt
[license-shield]: https://img.shields.io/github/license/SAGAR-TAMANG/BharatGPT-feynmanpi.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/sagar-tmg/