# Copyright (c) 2019 NVIDIA CORPORATION. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from WikiDownloader import WikiDownloader
from BooksDownloader import BooksDownloader


class Downloader:
    def __init__(self, dataset_name, save_path):
        self.dataset_name = dataset_name
        self.save_path = save_path


    def download(self):
        if self.dataset_name == 'bookscorpus':
            self.download_bookscorpus()

        elif self.dataset_name.startswith('wikicorpus'):
            lang = self.dataset_name.split('_')[1].strip()
            self.download_wikicorpus(lang)

        else:
            print(self.dataset_name)
            assert False, 'Unknown dataset_name provided to downloader'


    def download_bookscorpus(self):
        downloader = BooksDownloader(self.save_path)
        downloader.download()


    def download_wikicorpus(self, language):
        downloader = WikiDownloader(language, self.save_path)
        downloader.download()


