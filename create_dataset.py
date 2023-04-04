import os
import datasets
import pandas as pd
_CITATION = ""
_DESCRIPTION = "" 
_URL = ""
_HOMEPAGE = ""
_LICENSE = ""
DATA_DIR = 'train'

# https://towardsdatascience.com/how-to-turn-your-local-zip-data-into-a-huggingface-dataset-43f754c68f82

class NewDataset(datasets.GeneratorBasedBuilder):
  
  DEFAULT_WRITER_BATCH_SIZE = 256
  BUILDER_CONFIGS = [datasets.BuilderConfig(name="clean", description="Train Set.")]
  
  def _info(self):
    return datasets.DatasetInfo(
      description=_DESCRIPTION,
      features=datasets.features(
        {'image': datasets.Value('string'), 'label': datasets.Value('string')}
      ),
      homepage=_HOMEPAGE
    )
  
  def _split_generators(self, dl_manager):
    data_dir = self.config.data_dir
    if self.config.name == "clean":
      train_splits = [
        datasets.SplitGenerator(
            name='train', gen_kwargs={'files': data_dir, 'name': 'train'}
        )
      ]
      return train_splits
  
  def _generate_examples(self, files, name):
     key = 0
     examples = list()
     img_dir = os.path.join()


name_fit = []
for dirname, _, filenames_fit in os.walk(img_dir):
    for filename_fit in filenames_fit:
        name_fit.append(filename_fit.split('.')[0])
img_fit = pd.DataFrame({'id': name_fit}, index = np.arange(0, len(name_fit)))