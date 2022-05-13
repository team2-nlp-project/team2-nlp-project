"""
A module for obtaining repo readme and language data from the github API.

Before using this module, read through it, and follow the instructions marked
TODO.

After doing so, run it like this:

    python acquire.py

To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token: https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = [
    "gocodeup/codeup-setup-script",
    "gocodeup/movies-application",
    "torvalds/linux", 'jtleek/datasharing',
    'rdpeng/ProgrammingAssignment2',
    'octocat/Spoon-Knife',
    'SmartThingsCommunity/SmartThingsPublic',
    'tensorflow/tensorflow',
    'twbs/bootstrap',
    'LSPosed/MagiskOnWSA',
    'github/gitignore',
    'Pierian-Data/Complete-Python-3-Bootcamp',
    'nightscout/cgm-remote-monitor',
    'jwasham/coding-interview-university',
    'rdpeng/ExData_Plotting1',
    'github/docs',
    'opencv/opencv',
    'EbookFoundation/free-programming-books',
    'eugenp/tutorials',
    'CyC2018/CS-Notes',
    'tensorflow/models',
    'jackfrued/Python-100-Days',
    'firstcontributions/first-contributions',
    'hitherejoe/BottomNavigationViewSample',
    'J-Rios/TLG_JoinCaptchaBot',
    'NeKosmic/NK-BOT',
    'r7kamura/ruboty',
    'MMMzq/bot_toast',
    'SpEcHiDe/PyroGramBot',
    'natario1/BottomSheetCoordinatorLayout',
    'BilalShahid13/PersistentBottomNavBar',
    'brucevanfdm/BottomNavigationView',
    'jaisonfdo/BottomNavigation',
    'germanattanasio/text-bot',
    'hikaruAi/FacebookBot',
    'xTCry/VCoin',
    'NNTin/discord-twitter-bot',
    'CharmingDays/kurusaki_voice',
    'CrazyBotsz/Adv-Auto-Filter-Bot',
    'paco0x/amm-arbitrageur',
    'nysamnang/react-native-raw-bottom-sheet',
    'fabston/TradingView-Webhook-Bot',
    '546669204/RebateBot',
    'topkecleon/telegram-bot-bash',
    'evil-mad/EggBot',
    'telegram-bot-rb/telegram-bot',
    'alfficcadenti/splinterlands-bot',
    'nodeWechat/wechat4u',
    'tucnak/telebot',
    'CarlGroth/Carl-Bot',
    'grapeot/WechatForwardBot',
    'googleworkspace/hangouts-chat-samples',
    'GreyWolfDev/Werewolf',
    'abdelhai/awesome-bots',
    'mdgspace/bot',
    'Sank6/Discord-Bot-List',
    'samc621/SneakerBot',
    'boto/boto3-sample',
    'huseinzol05/Stock-Prediction-Models',
    'SAPConversationalAI/Webchat',
    'soumyadityac/youtube-viewer',
    'CodeWithJoe2020/pancakeswapBot',
    'Merubokkusu/discord-spam-bots',
    'ZeroDiscord/EconomyBot',
    'scrapinghub/slackbot',
    'baidu/boteye',
    'kcloze/swoole-bot',
    'hyperchessbot/hyperbot',
    'yangyuan/hearthrock',
    'agermanidis/SnapchatBot',
    'brompwnie/botb',
    'thedevs-network/the-guard-bot',
    'jqs7/Jqs7Bot',
    'AdeelMufti/CryptoBot',
    'aracred/bot',
    'zeldaret/botw',
    'jh0ker/mau_mau_bot',
    'coq/bot',
    'sandimetz/1st_99bottles_ruby',
    'jsdelivr/bot',
    'mgp25/Telegram-Bot-API',
    'kereh/BOT',
    'torvalds/linux',
    'Snailclimb/JavaGuide',
    'facebook/react',
    'rdpeng/RepData_PeerAssessment1',
    'spring-projects/spring-boot',
    'jlord/patchwork',
    'TheAlgorithms/Python',
    'ant-design/ant-design',
    'barryclark/jekyll-now',
    'spring-projects/spring-framework',
    'kubernetes/kubernetes',
    'bitcoin/bitcoin',
    'vuejs/vue',
    'mrdoob/three.js',
    'DataScienceSpecialization/courses',
    'getify/You-Dont-Know-JS',
    'freeCodeCamp/freeCodeCamp',
    'angular/angular.js',
    'kamranahmedse/developer-roadmap',
    'PanJiaChen/vue-element-admin',
    'sindresorhus/awesome',
    'ohmyzsh/ohmyzsh',
    'trekhleb/javascript-algorithms',
    'flutter/flutter',
    'TheAlgorithms/Python',
    'chartjs/Chart.js',
    'coder/code-server',
    'nestjs/nest',
    'yangshun/tech-interview-handbook',
    'laravel/laravel',
    'trimstray/the-book-of-secret-knowledge',
    'ryanmcdermott/clean-code-javascript',
    'gothinkster/realworld',
    'vuejs/awesome-vue',
    'tonsky/FiraCode',
    'hakimel/reveal.js',
    'angular/angular.js',
    'reduxjs/redux',
    'tailwindlabs/tailwindcss',
    'ripienaar/free-for-dev',
    'protocolbuffers/protobuf',
    'shadowsocks/shadowsocks-windows',
    'JetBrains/kotlin',
    'yarnpkg/yarn',
    'TryGhost/Ghost',
    'square/retrofit',
    'bradtraversy/design-resources-for-developers',
    'vsouza/awesome-ios',
    'iamkun/dayjs',
    'google/googletest',
    'projectdiscovery/nuclei-templates',
    'digitalocean/nginxconfig.io',
    'flutter/flutter',
    'PaddlePaddle/PaddleOCR',
    'flutter/pinball',
    'wolfogre/go-pprof-practice',
    'supabase/supabase',
    'felipefialho/frontend-challenges',
    'flutter/samples',
    'alibaba/fastjson2',
    'florinpop17/app-ideas',
    'charmbracelet/bubbletea',
    'huggingface/transformers',
    'databricks-academy/data-engineering-with-databricks',
    'hectorqin/reader',
    'Azure/azure-rest-api-specs',
    'terra-money/core',
    'saltstack/salt',
    'PKUFlyingPig/cs-self-learning',
    'actions/virtual-environments',
    'jojoldu/junior-recruit-scheduler',
    'dotnet/aspnetcore',
    'danielgindi/Charts',
    'microsoft/unilm',
    'jtleek/datasharing',
    'rdpeng/ProgrammingAssignment2',
    'octocat/Spoon-Knife',
    'tensorflow/tensorflow',
    'twbs/bootstrap',
    'Pierian-Data/Complete-Python-3-Bootcamp',
    'nightscout/cgm-remote-monitor',
    'jwasham/coding-interview-university',
    'rdpeng/ExData_Plotting1',
    'github/docs',
    'github/docs',
    'opencv/opencv',
    'EbookFoundation/free-programming-books',
    'eugenp/tutorials',
    'CyC2018/CS-Notes',
    'jackfrued/Python-100-Days',
    'firstcontributions/first-contributions',
    'torvalds/linux',
    'Snailclimb/JavaGuide',
    'facebook/react',
    'jlord/patchwork',
    'TheAlgorithms/Python',
    'ant-design/ant-design',
    'barryclark/jekyll-now',
    'bitcoin/bitcoin',
    'angular/angular.js',
    'kamranahmedse/developer-roadmap',
    'PanJiaChen/vue-element-admin',
    'django/django',
    'mui/material-ui',
    'kamranahmedse/developer-roadmap',
    'PanJiaChen/vue-element-admin',
    'DefinitelyTyped/DefinitelyTyped',
    'django/django',
    'mui/material-ui',
    'RedHatTraining/DO180-apps',
    'qmk/qmk_firmware',
    'apache/spark',
    'apache/dubbo',
    'google/it-cert-automation-practice',
    'facebook/create-react-app',
    'airbnb/javascript',
    'git/git',
    'nodejs/node',
    'sindresorhus/awesome',
    'iluwatar/java-design-patterns',
    'python/cpython',
    'd3/d3',
    'scikit-learn/scikit-learn',
    'atralice/Curso.Prep.Henry',
    'OCA/sale-workflow',
    'forcedotcom/SalesforceMobileSDK-Android',
    'appleseedhq/appleseed',
    'jasondavies/d3-cloud',
    'phpDocumentor/phpDocumentor',
    'UZ-SLAMLab/ORB_SLAM3',
    'ExtendRealityLtd/VRTK',
    'gboeing/osmnx',
    'luvit/luvit',
    'jaredpalmer/razzle',
    'howdyai/botkit',
    'json-iterator/go',
    'docker/labs',
    'ionic-team/stencil',
    'charmbracelet/bubbletea',
    'jxnblk/mdx-deck',
    'rovo89/Xposed',
    'rauchg/slackin',
    'axi0mX/ipwndfu',
    'rshipp/awesome-malware-analysis',
    'squeaky-pl/japronto',
    'claudiodangelis/qrcp',
    'codeguy/php-the-right-way',
    'aristocratos/bpytop',
    'php-fig/fig-standards',
    'pyecharts/pyecharts',
    'arangodb/arangodb',
    'qmk/qmk_firmware',
    'MaterialDesignInXAML/MaterialDesignInXamlToolkit',
    'kubernetes-sigs/kubespray',
    'mgonto/restangular',
    'draveness/analyze',
    'danialfarid/ng-file-upload',
    'mathiasbynens/jquery-placeholder',
    'makovkastar/FloatingActionButton',
    'BVLC/caffe',
    'apache/echarts',
    'CSSEGISandData/COVID-19',
    'jenkins-docs/simple-java-maven-app',
    'vercel/next.js',
    'home-assistant/core',
    'moby/moby',
    'ColorlibHQ/AdminLTE',
    'scm-ninja/starter-web',
    'xingshaocheng/architect-awesome',
    'ArduPilot/ardupilot',
    'codebasics/py',
    'ageitgey/face_recognition',
    'bailicangdu/vue2-elm',
    'angular/angular-cli',
    'kdn251/interviews',
    'Trinea/android-open-project',
    'zero-to-mastery/start-here-guidelines',
    'FortAwesome/Font-Awesome',
    'Homebrew/legacy-homebrew',
    'jakevdp/PythonDataScienceHandbook',
    'aymericdamien/TensorFlow-Examples',
    'pallets/flask',
    'github/opensource.guide',
    'golang/go',
    'TheOdinProject/css-exercises',
    'selfteaching/the-craft-of-selfteaching',
    'pandas-dev/pandas',
    'ElemeFE/element',
    'ionic-team/ionic-framework',
    'doocs/advanced-java',
    'MarlinFirmware/Marlin',
    'shadowsocks/shadowsocks-windows',
    'CoreyMSchafer/code_snippets',
    'MicrosoftDocs/azure-docs',
    'odoo/odoo',
    'FreeRDP/FreeRDP',
    'hakimel/reveal.js',
    'gabrielecirulli/2048',
    'udacity/course-collaboration-travel-plans',
    'ossu/computer-science',
    'jakevdp/PythonDataScienceHandbook',
    'aymericdamien/TensorFlow-Examples',
    'reduxjs/redux',
    'pallets/flask',
    'TheAlgorithms/Java',
    'scutan90/DeepLearning-500-questions',
    'huggingface/transformers',
    'github/opensource.guide',
    'golang/go',
    'reduxjs/redux',
    'pallets/flask',
    'scutan90/DeepLearning-500-questions',
    'huggingface/transformers',
    'github/opensource.guide',
    'golang/go',
    'TheOdinProject/css-exercises',
    'selfteaching/the-craft-of-selfteaching',
    'netty/netty',
    'Azure/azure-quickstart-templates'
]

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        print(f'error making request {url}')
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)
