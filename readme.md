# Satellite Imagery Super-Resolution

## Datasets

`datasets.py` take only the directory that contains high resolution image and  downgrade the image automatically to generate the paired dataset.

It also support passing the custom downgrading method through `downgrading_method`

Down-scaling factor is set to 4. `(h, w) => (h/4, w/4)`

## Models

Adopts `SwinIR`. 

- Input size is (128, 128)
- Output size is (256, 256)

#### Note the output/intput ratio is not the upscaling factor. This is just for matching the models output.

## Config

| Config          |                   |
|-----------------|-------------------|
| DEVICE          | device            |
| HR_SIZE         | 256               |
| LR_SIZE         | 128               |
| WorldStrat_path | path_to_directory |
| transform_hr    | ~                 |
| transform_hr    | ~                 |

## Output result
![image](./output.png)

## Some of my thoughts

Unlike other image super-resolution tasks, for example, anime and photography and other forms of art. Satellite imagery satellite should prioritize the accuracy over the high resolution. The image itself should avoid incorrect information.

I suppose majority of the sr techniques devide the large image into small patches and process them separately. Maybe we can leverage the information from other patches to reach a better performance.

