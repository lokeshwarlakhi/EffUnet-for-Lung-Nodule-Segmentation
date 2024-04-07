# About Luna16 Dataset

### Overview of the LUNA16 Dataset:

**Purpose:** It's designed for lung nodule analysis and segmentation tasks in medical imaging.

**Content:** 888 CT scans of the lungs with slice thickness less than 2.5mm , 1,186 manually annotated lung nodules.

**Division:** It's split into 10 subsets for 10-fold cross-validation.

### File Types:
- **.mhd files:** These are ***MetaImage header files*** that contain metadata about the corresponding CT scan, such as image dimensions, spacing, and orientation.

- **.zraw files:** These are ***compressed raw binary*** files that store the actual pixel data of the CT scan images.

- **annotations.csv:** This CSV file contains the annotations for the lung nodules, including their *coordinates*, *size*, and *malignancy ratings* from multiple radiologists.