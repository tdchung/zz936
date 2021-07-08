# All files

<details>
<summary>
<a name='parser/test3/dataset_dict.py' href='parser/test3/dataset_dict.py'>parser/test3/dataset_dict.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/dataset_dict.py:DatasetDict' href='parser/test3/dataset_dict.py#L25'>DatasetDict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/dataset_dict.py:IterableDatasetDict' href='parser/test3/dataset_dict.py#L871'>IterableDatasetDict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:_check_values_type' href='parser/test3/dataset_dict.py#L28'>DatasetDict:_check_values_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:__getitem__' href='parser/test3/dataset_dict.py#L35'>DatasetDict:__getitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>k,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:data' href='parser/test3/dataset_dict.py#L50'>DatasetDict:data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """The Apache Arrow tables backing each split."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:cache_files' href='parser/test3/dataset_dict.py#L56'>DatasetDict:cache_files</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """The cache files containing the Apache Arrow table backing each split."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:num_columns' href='parser/test3/dataset_dict.py#L62'>DatasetDict:num_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Number of columns in each split of the dataset."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:num_rows' href='parser/test3/dataset_dict.py#L68'>DatasetDict:num_rows</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Number of rows in each split of the dataset (same as :func:`datasets.Dataset.__len__`)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:column_names' href='parser/test3/dataset_dict.py#L74'>DatasetDict:column_names</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Names of the columns in each split of the dataset."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:shape' href='parser/test3/dataset_dict.py#L80'>DatasetDict:shape</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Shape of each split of the dataset (number of columns, number of rows)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:dictionary_encode_column_' href='parser/test3/dataset_dict.py#L86'>DatasetDict:dictionary_encode_column_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br></ul>
        <li>Docs:<br>        """Dictionary encode a column in each split.
<br>

<br>
        Dictionary encode can reduce the size of a column with many repetitions (e.g. string labels columns)
<br>
        by storing a dictionary of the strings. This only affect the internal storage.
<br>

<br>
        .. deprecated:: 1.4.0
<br>

<br>
        Args:
<br>
            column (:obj:`str`):
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:flatten_' href='parser/test3/dataset_dict.py#L103'>DatasetDict:flatten_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>max_depth = 16,<br></ul>
        <li>Docs:<br>        """In-place version of :meth:`DatasetDict.flatten`.
<br>

<br>
        .. deprecated:: 1.4.0
<br>
            Use :meth:`DatasetDict.flatten` instead.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:flatten' href='parser/test3/dataset_dict.py#L113'>DatasetDict:flatten</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>max_depth = 16,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:unique' href='parser/test3/dataset_dict.py#L121'>DatasetDict:unique</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br></ul>
        <li>Docs:<br>        """Return a list of the unique elements in a column for each split.
<br>

<br>
        This is implemented in the low-level backend and as such, very fast.
<br>

<br>
        Args:
<br>
            column (:obj:`str`):
<br>
                column name (list all the column names with :func:`datasets.Dataset.column_names`)
<br>

<br>
        Returns:
<br>
            Dict[:obj:`str`, :obj:`list`]: Dictionary of unique elements in the given column.
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:cleanup_cache_files' href='parser/test3/dataset_dict.py#L137'>DatasetDict:cleanup_cache_files</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Clean up all cache files in the dataset cache directory, excepted the currently used cache file if there is one.
<br>
        Be carefull when running this command that no other process is currently using other cache files.
<br>

<br>
        Return:
<br>
            Dict with the number of removed files for each split
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:__repr__' href='parser/test3/dataset_dict.py#L147'>DatasetDict:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:cast_' href='parser/test3/dataset_dict.py#L153'>DatasetDict:cast_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>features:  Features,<br></ul>
        <li>Docs:<br>        """In-place version of :meth:`DatasetDict.cast`.
<br>

<br>
        .. deprecated:: 1.4.0
<br>
            Use :meth:`DatasetDict.cast` instead.
<br>

<br>
        Args:
<br>
            features (:class:`datasets.Features`): New features to cast the dataset to.
<br>
                The name and order of the fields in the features must match the current column names.
<br>
                The type of the data must also be convertible from one type to the other.
<br>
                For non-trivial conversion, e.g. string <-> ClassLabel you should use :func:`map` to update the Dataset.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:cast' href='parser/test3/dataset_dict.py#L169'>DatasetDict:cast</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>features:  Features,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:remove_columns_' href='parser/test3/dataset_dict.py#L187'>DatasetDict:remove_columns_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column_names:  Union[str,<br>List[str]],<br></ul>
        <li>Docs:<br>        """In-place version of :meth:`DatasetDict.remove_columns`.
<br>

<br>
        .. deprecated:: 1.4.0
<br>
            Use :meth:`DatasetDict.remove_columns` instead.
<br>

<br>
        Args:
<br>
            column_names (:obj:`Union[str, List[str]]`): Name of the column(s) to remove.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:remove_columns' href='parser/test3/dataset_dict.py#L200'>DatasetDict:remove_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column_names:  Union[str,<br>List[str]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:rename_column_' href='parser/test3/dataset_dict.py#L217'>DatasetDict:rename_column_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>original_column_name:  str,<br>new_column_name:  str,<br></ul>
        <li>Docs:<br>        """In-place version of :meth:`DatasetDict.rename_column`.
<br>

<br>
        .. deprecated:: 1.4.0
<br>
            Use :meth:`DatasetDict.rename_column` instead.
<br>

<br>
        Args:
<br>
            original_column_name (:obj:`str`): Name of the column to rename.
<br>
            new_column_name (:obj:`str`): New name for the column.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:rename_column' href='parser/test3/dataset_dict.py#L234'>DatasetDict:rename_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>original_column_name:  str,<br>new_column_name:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:class_encode_column' href='parser/test3/dataset_dict.py#L255'>DatasetDict:class_encode_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br></ul>
        <li>Docs:<br>        """Casts the given column as :obj:``datasets.features.ClassLabel`` and updates the tables.
<br>

<br>
        Args:
<br>
            column (`str`): The name of the column to cast
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:formatted_as' href='parser/test3/dataset_dict.py#L265'>DatasetDict:formatted_as</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>type:  Optional[str]  =  None,<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>**format_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """To be used in a `with` statement. Set __getitem__ return format (type and columns)
<br>
        The transformation is applied to all the datasets of the dataset dictionary.
<br>

<br>
        Args:
<br>
            type (Optional ``str``): output type selected in [None, 'numpy', 'torch', 'tensorflow', 'pandas', 'arrow']
<br>
                None means __getitem__ returns python objects (default)
<br>
            columns (Optional ``List[str]``): columns to format in the output
<br>
                None means __getitem__ returns all columns (default)
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
            format_kwargs: keywords arguments passed to the convert function like `np.array`, `torch.tensor` or `tensorflow.ragged.constant`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:set_format' href='parser/test3/dataset_dict.py#L297'>DatasetDict:set_format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>type:  Optional[str]  =  None,<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>**format_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Set __getitem__ return format (type and columns)
<br>
        The format is set for every dataset in the dataset dictionary
<br>

<br>
        Args:
<br>
            type (Optional ``str``): output type selected in [None, 'numpy', 'torch', 'tensorflow', 'pandas', 'arrow']
<br>
                None means __getitem__ returns python objects (default)
<br>
            columns (Optional ``List[str]``): columns to format in the output.
<br>
                None means __getitem__ returns all columns (default).
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
            format_kwargs: keywords arguments passed to the convert function like `np.array`, `torch.tensor` or `tensorflow.ragged.constant`.
<br>

<br>
        It is possible to call ``map`` after calling ``set_format``. Since ``map`` may add new columns, then the list of formatted columns
<br>
        gets updated. In this case, if you apply ``map`` on a dataset to add a new column, then this column will be formatted:
<br>

<br>
            new formatted columns = (all columns - previously unformatted columns)
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:reset_format' href='parser/test3/dataset_dict.py#L324'>DatasetDict:reset_format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Reset __getitem__ return format to python objects and all columns.
<br>
        The transformation is applied to all the datasets of the dataset dictionary.
<br>

<br>
        Same as ``self.set_format()``
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:set_transform' href='parser/test3/dataset_dict.py#L334'>DatasetDict:set_transform</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>transform:  Optional[Callable],<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>,<br></ul>
        <li>Docs:<br>        """Set __getitem__ return format using this transform. The transform is applied on-the-fly on batches when __getitem__ is called.
<br>
        The transform is set for every dataset in the dataset dictionary
<br>
        As :func:`datasets.Dataset.set_format`, this can be reset using :func:`datasets.Dataset.reset_format`
<br>

<br>
        Args:
<br>
            transform (Optional ``Callable``): user-defined formatting transform, replaces the format defined by :func:`datasets.Dataset.set_format`
<br>
                A formatting function is a callable that takes a batch (as a dict) as input and returns a batch.
<br>
                This function is applied right before returning the objects in __getitem__.
<br>
            columns (Optional ``List[str]``): columns to format in the output
<br>
                If specified, then the input batch of the transform only contains those columns.
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
                If set to True, then the other un-formatted columns are kept with the output of the transform.
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:with_format' href='parser/test3/dataset_dict.py#L358'>DatasetDict:with_format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>type:  Optional[str]  =  None,<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>**format_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Set __getitem__ return format (type and columns). The data formatting is applied on-the-fly.
<br>
        The format ``type`` (for example "numpy") is used to format batches when using __getitem__.
<br>
        The format is set for every dataset in the dataset dictionary
<br>

<br>
        It's also possible to use custom transforms for formatting using :func:`datasets.Dataset.with_transform`.
<br>

<br>
        Contrary to :func:`datasets.DatasetDict.set_format`, ``with_format`` returns a new DatasetDict object with new Dataset objects.
<br>

<br>
        Args:
<br>
            type (Optional ``str``):
<br>
                Either output type selected in [None, 'numpy', 'torch', 'tensorflow', 'pandas', 'arrow'].
<br>
                None means __getitem__ returns python objects (default)
<br>
            columns (Optional ``List[str]``): columns to format in the output
<br>
                None means __getitem__ returns all columns (default)
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
            format_kwargs: keywords arguments passed to the convert function like `np.array`, `torch.tensor` or `tensorflow.ragged.constant`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:with_transform' href='parser/test3/dataset_dict.py#L386'>DatasetDict:with_transform</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>transform:  Optional[Callable],<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>,<br></ul>
        <li>Docs:<br>        """Set __getitem__ return format using this transform. The transform is applied on-the-fly on batches when __getitem__ is called.
<br>
        The transform is set for every dataset in the dataset dictionary
<br>

<br>
        As :func:`datasets.Dataset.set_format`, this can be reset using :func:`datasets.Dataset.reset_format`.
<br>

<br>
        Contrary to :func:`datasets.DatasetDict.set_transform`, ``with_transform`` returns a new DatasetDict object with new Dataset objects.
<br>

<br>
        Args:
<br>
            transform (Optional ``Callable``): user-defined formatting transform, replaces the format defined by :func:`datasets.Dataset.set_format`
<br>
                A formatting function is a callable that takes a batch (as a dict) as input and returns a batch.
<br>
                This function is applied right before returning the objects in __getitem__.
<br>
            columns (Optional ``List[str]``): columns to format in the output
<br>
                If specified, then the input batch of the transform only contains those columns.
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
                If set to True, then the other un-formatted columns are kept with the output of the transform.
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:map' href='parser/test3/dataset_dict.py#L413'>DatasetDict:map</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>function,<br>with_indices:  bool  =  False,<br>input_columns:  Optional[Union[str,<br>List[str]]]  =  None,<br>batched:  bool  =  False,<br>batch_size:  Optional[int]  =  1000,<br>remove_columns:  Optional[List[str]]  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>cache_file_names:  Optional[Dict[str,<br>Optional[str]]]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>features:  Optional[Features]  =  None,<br>disable_nullable:  bool  =  False,<br>fn_kwargs:  Optional[dict]  =  None,<br>num_proc:  Optional[int]  =  None,<br>desc:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Apply a function to all the elements in the table (individually or in batches)
<br>
        and update the table (if function does updated examples).
<br>
        The transformation is applied to all the datasets of the dataset dictionary.
<br>

<br>
        Args:
<br>
            function (`callable`): with one of the following signature:
<br>
                - `function(example: Dict) -> Union[Dict, Any]` if `batched=False` and `with_indices=False`
<br>
                - `function(example: Dict, indices: int) -> Union[Dict, Any]` if `batched=False` and `with_indices=True`
<br>
                - `function(batch: Dict[List]) -> Union[Dict, Any]` if `batched=True` and `with_indices=False`
<br>
                - `function(batch: Dict[List], indices: List[int]) -> Union[Dict, Any]` if `batched=True` and `with_indices=True`
<br>
            with_indices (`bool`, defaults to `False`): Provide example indices to `function`. Note that in this case the signature of `function` should be `def function(example, idx): ...`.
<br>
            input_columns (`Optional[Union[str, List[str]]]`, defaults to `None`): The columns to be passed into `function` as
<br>
                positional arguments. If `None`, a dict mapping to all formatted columns is passed as one argument.
<br>
            batched (`bool`, defaults to `False`): Provide batch of examples to `function`
<br>
            batch_size (`Optional[int]`, defaults to `1000`): Number of examples per batch provided to `function` if `batched=True`
<br>
                `batch_size <= 0` or `batch_size == None`: Provide the full dataset as a single batch to `function`
<br>
            remove_columns (`Optional[List[str]]`, defaults to `None`): Remove a selection of columns while doing the mapping.
<br>
                Columns will be removed before updating the examples with the output of `function`, i.e. if `function` is adding
<br>
                columns with names in `remove_columns`, these columns will be kept.
<br>
            keep_in_memory (`bool`, defaults to `False`): Keep the dataset in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (`bool`, defaults to `True`): If a cache file storing the current computation from `function`
<br>
                can be identified, use it instead of recomputing.
<br>
            cache_file_names (`Optional[Dict[str, str]]`, defaults to `None`): Provide the name of a path for the cache file. It is used to store the
<br>
                results of the computation instead of the automatically generated cache file name.
<br>
                You have to provide one :obj:`cache_file_name` per dataset in the dataset dictionary.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            features (`Optional[datasets.Features]`, defaults to `None`): Use a specific Features to store the cache file
<br>
                instead of the automatically generated one.
<br>
            disable_nullable (`bool`, defaults to `True`): Disallow null values in the table.
<br>
            fn_kwargs (`Optional[Dict]`, defaults to `None`): Keyword arguments to be passed to `function`
<br>
            num_proc (`Optional[int]`, defaults to `None`): Number of processes for multiprocessing. By default it doesn't
<br>
                use multiprocessing.
<br>
            desc (`Optional[str]`, defaults to `None`): Meaningful description to be displayed alongside with the progress bar while mapping examples.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:filter' href='parser/test3/dataset_dict.py#L493'>DatasetDict:filter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>function,<br>with_indices = False,<br>input_columns:  Optional[Union[str,<br>List[str]]]  =  None,<br>batch_size:  Optional[int]  =  1000,<br>remove_columns:  Optional[List[str]]  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>cache_file_names:  Optional[Dict[str,<br>Optional[str]]]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>fn_kwargs:  Optional[dict]  =  None,<br>num_proc:  Optional[int]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Apply a filter function to all the elements in the table in batches
<br>
        and update the table so that the dataset only includes examples according to the filter function.
<br>
        The transformation is applied to all the datasets of the dataset dictionary.
<br>

<br>
        Args:
<br>
            function (`callable`): with one of the following signature:
<br>
                - `function(example: Dict) -> bool` if `with_indices=False`
<br>
                - `function(example: Dict, indices: int) -> bool` if `with_indices=True`
<br>
            with_indices (`bool`, defaults to `False`): Provide example indices to `function`. Note that in this case the signature of `function` should be `def function(example, idx): ...`.
<br>
            input_columns (`Optional[Union[str, List[str]]]`, defaults to `None`): The columns to be passed into `function` as
<br>
                positional arguments. If `None`, a dict mapping to all formatted columns is passed as one argument.
<br>
            batch_size (`Optional[int]`, defaults to `1000`): Number of examples per batch provided to `function` if `batched=True`
<br>
                `batch_size <= 0` or `batch_size == None`: Provide the full dataset as a single batch to `function`
<br>
            remove_columns (`Optional[List[str]]`, defaults to `None`): Remove a selection of columns while doing the mapping.
<br>
                Columns will be removed before updating the examples with the output of `function`, i.e. if `function` is adding
<br>
                columns with names in `remove_columns`, these columns will be kept.
<br>
            keep_in_memory (`bool`, defaults to `False`): Keep the dataset in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (`bool`, defaults to `True`): If a cache file storing the current computation from `function`
<br>
                can be identified, use it instead of recomputing.
<br>
            cache_file_names (`Optional[Dict[str, str]]`, defaults to `None`): Provide the name of a path for the cache file. It is used to store the
<br>
                results of the computation instead of the automatically generated cache file name.
<br>
                You have to provide one :obj:`cache_file_name` per dataset in the dataset dictionary.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            fn_kwargs (`Optional[Dict]`, defaults to `None`): Keyword arguments to be passed to `function`
<br>
            num_proc (`Optional[int]`, defaults to `None`): Number of processes for multiprocessing. By default it doesn't
<br>
                use multiprocessing.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:sort' href='parser/test3/dataset_dict.py#L558'>DatasetDict:sort</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br>reverse:  bool  =  False,<br>kind:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>indices_cache_file_names:  Optional[Dict[str,<br>Optional[str]]]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>,<br></ul>
        <li>Docs:<br>        """Create a new dataset sorted according to a column.
<br>
        The transformation is applied to all the datasets of the dataset dictionary.
<br>

<br>
        Currently sorting according to a column name uses numpy sorting algorithm under the hood.
<br>
        The column should thus be a numpy compatible type (in particular not a nested type).
<br>
        This also means that the column used for sorting is fully loaded in memory (which should be fine in most cases).
<br>

<br>
        Args:
<br>
            column (`str`): column name to sort by.
<br>
            reverse: (`bool`, defaults to `False`): If True, sort by descending order rather then ascending.
<br>
            kind (Optional `str`): Numpy algorithm for sorting selected in {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’},
<br>
                The default is ‘quicksort’. Note that both ‘stable’ and ‘mergesort’ use timsort under the covers and, in general,
<br>
                the actual implementation will vary with data type. The ‘mergesort’ option is retained for backwards compatibility.
<br>
            keep_in_memory (`bool`, defaults to `False`): Keep the dataset in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (`bool`, defaults to `True`): If a cache file storing the current computation from `function`
<br>
                can be identified, use it instead of recomputing.
<br>
            indices_cache_file_names (`Optional[Dict[str, str]]`, defaults to `None`): Provide the name of a path for the cache file. It is used to store the
<br>
                indices mapping instead of the automatically generated cache file name.
<br>
                You have to provide one :obj:`cache_file_name` per dataset in the dataset dictionary.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:shuffle' href='parser/test3/dataset_dict.py#L609'>DatasetDict:shuffle</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seeds:  Optional[Union[int,<br>Dict[str,<br>Optional[int]]]]  =  None,<br>seed:  Optional[int]  =  None,<br>generators:  Optional[Dict[str,<br>np.random.Generator]]  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>indices_cache_file_names:  Optional[Dict[str,<br>Optional[str]]]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>,<br></ul>
        <li>Docs:<br>        """Create a new Dataset where the rows are shuffled.
<br>

<br>
        The transformation is applied to all the datasets of the dataset dictionary.
<br>

<br>
        Currently shuffling uses numpy random generators.
<br>
        You can either supply a NumPy BitGenerator to use, or a seed to initiate NumPy's default random generator (PCG64).
<br>

<br>
        Args:
<br>
            seeds (`Dict[str, int]` or `int`, optional): A seed to initialize the default BitGenerator if ``generator=None``.
<br>
                If None, then fresh, unpredictable entropy will be pulled from the OS.
<br>
                If an int or array_like[ints] is passed, then it will be passed to SeedSequence to derive the initial BitGenerator state.
<br>
                You can provide one :obj:`seed` per dataset in the dataset dictionary.
<br>
            seed (Optional `int`): A seed to initialize the default BitGenerator if ``generator=None``. Alias for seeds (the seed argument has priority over seeds if both arguments are provided).
<br>
            generators (Optional `Dict[str, np.random.Generator]`): Numpy random Generator to use to compute the permutation of the dataset rows.
<br>
                If ``generator=None`` (default), uses np.random.default_rng (the default BitGenerator (PCG64) of NumPy).
<br>
                You have to provide one :obj:`generator` per dataset in the dataset dictionary.
<br>
            keep_in_memory (`bool`, defaults to `False`): Keep the dataset in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (`bool`, defaults to `True`): If a cache file storing the current computation from `function`
<br>
                can be identified, use it instead of recomputing.
<br>
            indices_cache_file_names (`Dict[str, str]`, optional): Provide the name of a path for the cache file. It is used to store the
<br>
                indices mappings instead of the automatically generated cache file name.
<br>
                You have to provide one :obj:`cache_file_name` per dataset in the dataset dictionary.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:save_to_disk' href='parser/test3/dataset_dict.py#L671'>DatasetDict:save_to_disk</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_dict_path:  str,<br>fs = None,<br></ul>
        <li>Docs:<br>        """
<br>
        Saves a dataset dict to a filesystem using either :class:`~filesystems.S3FileSystem` or
<br>
        ``fsspec.spec.AbstractFileSystem``.
<br>

<br>
        Args:
<br>
            dataset_dict_path (``str``): Path (e.g. `dataset/train`) or remote URI
<br>
                (e.g. `s3://my-bucket/dataset/train`) of the dataset dict directory where the dataset dict will be
<br>
                saved to.
<br>
            fs (:class:`~filesystems.S3FileSystem`, ``fsspec.spec.AbstractFileSystem``, optional, defaults ``None``):
<br>
                Instance of the remote filesystem used to download the files from.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:load_from_disk' href='parser/test3/dataset_dict.py#L698'>DatasetDict:load_from_disk</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset_dict_path:  str,<br>fs = None,<br>keep_in_memory:  Optional[bool]  =  None,<br></ul>
        <li>Docs:<br>        """
<br>
        Load a dataset that was previously saved using :meth:`save_to_disk` from a filesystem using either
<br>
        :class:`~filesystems.S3FileSystem` or ``fsspec.spec.AbstractFileSystem``.
<br>

<br>
        Args:
<br>
            dataset_dict_path (:obj:`str`): Path (e.g. ``"dataset/train"``) or remote URI (e.g.
<br>
                ``"s3//my-bucket/dataset/train"``) of the dataset dict directory where the dataset dict will be loaded
<br>
                from.
<br>
            fs (:class:`~filesystems.S3FileSystem` or ``fsspec.spec.AbstractFileSystem``, optional, default ``None``):
<br>
                Instance of the remote filesystem used to download the files from.
<br>
            keep_in_memory (:obj:`bool`, default ``None``): Whether to copy the dataset in-memory. If `None`, the
<br>
                dataset will not be copied in-memory unless explicitly enabled by setting
<br>
                `datasets.config.IN_MEMORY_MAX_SIZE` to nonzero. See more details in the
<br>
                :ref:`load_dataset_enhancing_performance` section.
<br>

<br>
        Returns:
<br>
            :class:`DatasetDict`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:from_csv' href='parser/test3/dataset_dict.py#L739'>DatasetDict:from_csv</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path_or_paths:  Dict[str,<br>PathLike],<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Create DatasetDict from CSV file(s).
<br>

<br>
        Args:
<br>
            path_or_paths (dict of path-like): Path(s) of the CSV file(s).
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            cache_dir (str, optional, default="~/.cache/huggingface/datasets"): Directory to cache data.
<br>
            keep_in_memory (bool, default=False): Whether to copy the data in-memory.
<br>
            **kwargs: Keyword arguments to be passed to :meth:`pandas.read_csv`.
<br>

<br>
        Returns:
<br>
            :class:`DatasetDict`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:from_json' href='parser/test3/dataset_dict.py#L766'>DatasetDict:from_json</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path_or_paths:  Dict[str,<br>PathLike],<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Create DatasetDict from JSON Lines file(s).
<br>

<br>
        Args:
<br>
            path_or_paths (path-like or list of path-like): Path(s) of the JSON Lines file(s).
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            cache_dir (str, optional, default="~/.cache/huggingface/datasets"): Directory to cache data.
<br>
            keep_in_memory (bool, default=False): Whether to copy the data in-memory.
<br>
            **kwargs: Keyword arguments to be passed to :class:`JsonConfig`.
<br>

<br>
        Returns:
<br>
            :class:`DatasetDict`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:from_parquet' href='parser/test3/dataset_dict.py#L793'>DatasetDict:from_parquet</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path_or_paths:  Dict[str,<br>PathLike],<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>columns:  Optional[List[str]]  =  None,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Create DatasetDict from Parquet file(s).
<br>

<br>
        Args:
<br>
            path_or_paths (dict of path-like): Path(s) of the CSV file(s).
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            cache_dir (str, optional, default="~/.cache/huggingface/datasets"): Directory to cache data.
<br>
            keep_in_memory (bool, default=False): Whether to copy the data in-memory.
<br>
            columns (:obj:`List[str]`, optional): If not None, only these columns will be read from the file.
<br>
                A column name may be a prefix of a nested field, e.g. 'a' will select
<br>
                'a.b', 'a.c', and 'a.d.e'.
<br>
            **kwargs: Keyword arguments to be passed to :class:`ParquetConfig`.
<br>

<br>
        Returns:
<br>
            :class:`DatasetDict`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:from_text' href='parser/test3/dataset_dict.py#L829'>DatasetDict:from_text</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path_or_paths:  Dict[str,<br>PathLike],<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Create DatasetDict from text file(s).
<br>

<br>
        Args:
<br>
            path_or_paths (dict of path-like): Path(s) of the text file(s).
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            cache_dir (str, optional, default="~/.cache/huggingface/datasets"): Directory to cache data.
<br>
            keep_in_memory (bool, default=False): Whether to copy the data in-memory.
<br>
            **kwargs: Keyword arguments to be passed to :class:`TextConfig`.
<br>

<br>
        Returns:
<br>
            :class:`DatasetDict`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:prepare_for_task' href='parser/test3/dataset_dict.py#L856'>DatasetDict:prepare_for_task</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>task:  Union[str,<br>TaskTemplate],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/dataset_dict.py:DatasetDict:align_labels_with_mapping' href='parser/test3/dataset_dict.py#L861'>DatasetDict:align_labels_with_mapping</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>label2id:  Dict,<br>label_column:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/formatting/tf_formatter.py' href='parser/test3/formatting/tf_formatter.py'>parser/test3/formatting/tf_formatter.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/tf_formatter.py:TFFormatter' href='parser/test3/formatting/tf_formatter.py#L30'>TFFormatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/tf_formatter.py:TFFormatter:__init__' href='parser/test3/formatting/tf_formatter.py#L31'>TFFormatter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>**tf_tensor_kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/tf_formatter.py:TFFormatter:_tensorize' href='parser/test3/formatting/tf_formatter.py#L35'>TFFormatter:_tensorize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/tf_formatter.py:TFFormatter:_recursive_tensorize' href='parser/test3/formatting/tf_formatter.py#L46'>TFFormatter:_recursive_tensorize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data_struct:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/tf_formatter.py:TFFormatter:recursive_tensorize' href='parser/test3/formatting/tf_formatter.py#L58'>TFFormatter:recursive_tensorize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data_struct:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/tf_formatter.py:TFFormatter:format_row' href='parser/test3/formatting/tf_formatter.py#L61'>TFFormatter:format_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/tf_formatter.py:TFFormatter:format_column' href='parser/test3/formatting/tf_formatter.py#L65'>TFFormatter:format_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/tf_formatter.py:TFFormatter:format_batch' href='parser/test3/formatting/tf_formatter.py#L69'>TFFormatter:format_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/features.py' href='parser/test3/features.py'>parser/test3/features.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:_arrow_to_datasets_dtype' href='parser/test3/features.py#L43'>_arrow_to_datasets_dtype</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>arrow_type:  pa.DataType,<br></ul>
        <li>Docs:<br>    """
<br>
    _arrow_to_datasets_dtype takes a pyarrow.DataType and converts it to a datasets string dtype.
<br>
    In effect, `dt == string_to_arrow(_arrow_to_datasets_dtype(dt))`
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:string_to_arrow' href='parser/test3/features.py#L95'>string_to_arrow</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>datasets_dtype:  str,<br></ul>
        <li>Docs:<br>    """
<br>
    string_to_arrow takes a datasets string dtype and converts it to a pyarrow.DataType.
<br>

<br>
    In effect, `dt == string_to_arrow(_arrow_to_datasets_dtype(dt))`
<br>

<br>
    This is necessary because the datasets.Value() primitive type is constructed using a string dtype
<br>

<br>
    Value(dtype=str)
<br>

<br>
    But Features.type (via `get_nested_type()` expects to resolve Features into a pyarrow Schema,
<br>
        which means that each Value() must be able to resolve into a corresponding pyarrow.DataType, which is the
<br>
        purpose of this function.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:_cast_to_python_objects' href='parser/test3/features.py#L145'>_cast_to_python_objects</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>obj:  Any,<br></ul>
        <li>Docs:<br>    """
<br>
    Cast numpy/pytorch/tensorflow/pandas objects to python lists.
<br>
    It works recursively.
<br>

<br>
    To avoid iterating over possibly long lists, it first checks if the first element that is not None has to be casted.
<br>
    If the first element needs to be casted, then all the elements of the list will be casted, otherwise they'll stay the same.
<br>
    This trick allows to cast objects that contain tokenizers outputs without iterating over every single token for example.
<br>

<br>
    Args:
<br>
        obj: the object (nested struct) to cast
<br>

<br>
    Returns:
<br>
        casted_obj: the casted object
<br>
        has_changed (bool): True if the object has been changed, False if it is identical
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:cast_to_python_objects' href='parser/test3/features.py#L210'>cast_to_python_objects</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>obj:  Any,<br></ul>
        <li>Docs:<br>    """
<br>
    Cast numpy/pytorch/tensorflow/pandas objects to python lists.
<br>
    It works recursively.
<br>

<br>
    To avoid iterating over possibly long lists, it first checks if the first element that is not None has to be casted.
<br>
    If the first element needs to be casted, then all the elements of the list will be casted, otherwise they'll stay the same.
<br>
    This trick allows to cast objects that contain tokenizers outputs without iterating over every single token for example.
<br>

<br>
    Args:
<br>
        obj: the object (nested struct) to cast
<br>

<br>
    Returns:
<br>
        casted_obj: the casted object
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:_is_zero_copy_only' href='parser/test3/features.py#L381'>_is_zero_copy_only</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>pa_type:  pa.DataType,<br></ul>
        <li>Docs:<br>    """
<br>
    When converting a pyarrow array to a numpy array, we must know whether this could be done in zero-copy or not.
<br>
    This function returns the value of the ``zero_copy_only`` parameter to pass to ``.to_numpy()``, given the type of the pyarrow array.
<br>

<br>
    # zero copy is available for all primitive types except booleans
<br>
    # primitive types are types for which the physical representation in arrow and in numpy
<br>
    # https://github.com/wesm/arrow/blob/c07b9b48cf3e0bbbab493992a492ae47e5b04cad/python/pyarrow/types.pxi#L821
<br>
    # see https://arrow.apache.org/docs/python/generated/pyarrow.Array.html#pyarrow.Array.to_numpy
<br>
    # and https://issues.apache.org/jira/browse/ARROW-2871?jql=text%20~%20%22boolean%20to_numpy%22
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:pandas_types_mapper' href='parser/test3/features.py#L544'>pandas_types_mapper</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dtype,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:get_nested_type' href='parser/test3/features.py#L826'>get_nested_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>schema:  FeatureType,<br></ul>
        <li>Docs:<br>    """
<br>
    get_nested_type() converts a datasets.FeatureType into a pyarrow.DataType, and acts as the inverse of
<br>
        generate_from_arrow_type().
<br>

<br>
    It performs double-duty as the implementation of Features.type and handles the conversion of
<br>
        datasets.Feature->pa.struct
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:encode_nested_example' href='parser/test3/features.py#L858'>encode_nested_example</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>schema,<br>obj,<br></ul>
        <li>Docs:<br>    """Encode a nested example.
<br>
    This is used since some features (in particular ClassLabel) have some logic during encoding.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:generate_from_dict' href='parser/test3/features.py#L897'>generate_from_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>obj:  Any,<br></ul>
        <li>Docs:<br>    """Regenerate the nested feature object from a deserialized dict.
<br>
    We use the '_type' fields to get the dataclass name to load.
<br>

<br>
    generate_from_dict is the recursive helper for Features.from_dict, and allows for a convenient constructor syntax
<br>
    to define features from deserialized JSON dictionaries. This function is used in particular when deserializing
<br>
    a :class:`DatasetInfo` that was dumped to a JSON object. This acts as an analogue to
<br>
    :meth:`Features.from_arrow_schema` and handles the recursive field-by-field instantiation, but doesn't require any
<br>
    mapping to/from pyarrow, except for the fact that it takes advantage of the mapping of pyarrow primitive dtypes
<br>
    that :class:`Value` automatically performs.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/features.py:generate_from_arrow_type' href='parser/test3/features.py#L923'>generate_from_arrow_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>pa_type:  pa.DataType,<br></ul>
        <li>Docs:<br>    """
<br>
    generate_from_arrow_type accepts an arrow DataType and returns a datasets FeatureType to be used as the type for
<br>
        a single field.
<br>

<br>
    This is the high-level arrow->datasets type conversion and is inverted by get_nested_type().
<br>

<br>
    This operates at the individual *field* level, whereas Features.from_arrow_schema() operates at the
<br>
        full schema level and holds the methods that represent the bijection from Features<->pyarrow.Schema
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Value' href='parser/test3/features.py#L229'>Value</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:_ArrayXD' href='parser/test3/features.py#L281'>_ArrayXD</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Array2D' href='parser/test3/features.py#L296'>Array2D</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Array3D' href='parser/test3/features.py#L305'>Array3D</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Array4D' href='parser/test3/features.py#L314'>Array4D</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Array5D' href='parser/test3/features.py#L323'>Array5D</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:_ArrayXDExtensionType' href='parser/test3/features.py#L331'>_ArrayXDExtensionType</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Array2DExtensionType' href='parser/test3/features.py#L365'>Array2DExtensionType</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Array3DExtensionType' href='parser/test3/features.py#L369'>Array3DExtensionType</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Array4DExtensionType' href='parser/test3/features.py#L373'>Array4DExtensionType</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Array5DExtensionType' href='parser/test3/features.py#L377'>Array5DExtensionType</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:ArrayExtensionArray' href='parser/test3/features.py#L395'>ArrayExtensionArray</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:PandasArrayExtensionDtype' href='parser/test3/features.py#L418'>PandasArrayExtensionDtype</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:PandasArrayExtensionArray' href='parser/test3/features.py#L453'>PandasArrayExtensionArray</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:ClassLabel' href='parser/test3/features.py#L550'>ClassLabel</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Translation' href='parser/test3/features.py#L683'>Translation</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:TranslationVariableLanguages' href='parser/test3/features.py#L720'>TranslationVariableLanguages</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Sequence' href='parser/test3/features.py#L796'>Sequence</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/features.py:Features' href='parser/test3/features.py#L953'>Features</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Value:__post_init__' href='parser/test3/features.py#L260'>Value:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Value:__call__' href='parser/test3/features.py#L267'>Value:__call__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Value:encode_example' href='parser/test3/features.py#L270'>Value:encode_example</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:_ArrayXD:__post_init__' href='parser/test3/features.py#L260'>_ArrayXD:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:_ArrayXD:__call__' href='parser/test3/features.py#L267'>_ArrayXD:__call__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:_ArrayXD:encode_example' href='parser/test3/features.py#L270'>_ArrayXD:encode_example</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:_ArrayXDExtensionType:__init__' href='parser/test3/features.py#L334'>_ArrayXDExtensionType:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>shape:  tuple,<br>dtype:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:_ArrayXDExtensionType:__reduce__' href='parser/test3/features.py#L344'>_ArrayXDExtensionType:__reduce__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:_ArrayXDExtensionType:__arrow_ext_class__' href='parser/test3/features.py#L350'>_ArrayXDExtensionType:__arrow_ext_class__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:_ArrayXDExtensionType:_generate_dtype' href='parser/test3/features.py#L353'>_ArrayXDExtensionType:_generate_dtype</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dtype,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:_ArrayXDExtensionType:to_pandas_dtype' href='parser/test3/features.py#L361'>_ArrayXDExtensionType:to_pandas_dtype</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ArrayExtensionArray:__array__' href='parser/test3/features.py#L396'>ArrayExtensionArray:__array__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ArrayExtensionArray:__getitem__' href='parser/test3/features.py#L400'>ArrayExtensionArray:__getitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>i,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ArrayExtensionArray:to_numpy' href='parser/test3/features.py#L403'>ArrayExtensionArray:to_numpy</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>zero_copy_only = True,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ArrayExtensionArray:to_pylist' href='parser/test3/features.py#L413'>ArrayExtensionArray:to_pylist</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionDtype:__init__' href='parser/test3/features.py#L421'>PandasArrayExtensionDtype:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>value_type:  Union["PandasArrayExtensionDtype",<br>np.dtype],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionDtype:__from_arrow__' href='parser/test3/features.py#L424'>PandasArrayExtensionDtype:__from_arrow__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>array,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionDtype:construct_array_type' href='parser/test3/features.py#L433'>PandasArrayExtensionDtype:construct_array_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionDtype:type' href='parser/test3/features.py#L437'>PandasArrayExtensionDtype:type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionDtype:kind' href='parser/test3/features.py#L441'>PandasArrayExtensionDtype:kind</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionDtype:name' href='parser/test3/features.py#L445'>PandasArrayExtensionDtype:name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionDtype:value_type' href='parser/test3/features.py#L449'>PandasArrayExtensionDtype:value_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:__init__' href='parser/test3/features.py#L454'>PandasArrayExtensionArray:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data:  np.ndarray,<br>copy:  bool  =  False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:__array__' href='parser/test3/features.py#L458'>PandasArrayExtensionArray:__array__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dtype = None,<br></ul>
        <li>Docs:<br>        """
<br>
        Convert to NumPy Array.
<br>
        Note that Pandas expects a 1D array when dtype is set to object.
<br>
        But for other dtypes, the returned shape is the same as the one of ``data``.
<br>

<br>
        More info about pandas 1D requirement for PandasExtensionArray here:
<br>
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:copy' href='parser/test3/features.py#L478'>PandasArrayExtensionArray:copy</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>deep:  bool  =  False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:_from_sequence' href='parser/test3/features.py#L482'>PandasArrayExtensionArray:_from_sequence</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>scalars,<br>dtype:  Optional[PandasArrayExtensionDtype]  =  None,<br>copy:  bool  =  False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:_concat_same_type' href='parser/test3/features.py#L489'>PandasArrayExtensionArray:_concat_same_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>to_concat:  Sequence_["PandasArrayExtensionArray"],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:dtype' href='parser/test3/features.py#L494'>PandasArrayExtensionArray:dtype</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:nbytes' href='parser/test3/features.py#L498'>PandasArrayExtensionArray:nbytes</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:isna' href='parser/test3/features.py#L501'>PandasArrayExtensionArray:isna</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:__setitem__' href='parser/test3/features.py#L504'>PandasArrayExtensionArray:__setitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>key:  Union[int,<br>slice,<br>np.ndarray],<br>value:  Any,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:__getitem__' href='parser/test3/features.py#L507'>PandasArrayExtensionArray:__getitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>item:  Union[int,<br>slice,<br>np.ndarray],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:take' href='parser/test3/features.py#L512'>PandasArrayExtensionArray:take</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>indices:  Sequence_[int],<br>allow_fill:  bool  =  False,<br>fill_value:  bool  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:__len__' href='parser/test3/features.py#L535'>PandasArrayExtensionArray:__len__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:PandasArrayExtensionArray:__eq__' href='parser/test3/features.py#L538'>PandasArrayExtensionArray:__eq__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ClassLabel:__post_init__' href='parser/test3/features.py#L260'>ClassLabel:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """
<br>
    When converting a pyarrow array to a numpy array, we must know whether this could be done in zero-copy or not.
<br>
    This function returns the value of the ``zero_copy_only`` parameter to pass to ``.to_numpy()``, given the type of the pyarrow array.
<br>

<br>
    # zero copy is available for all primitive types except booleans
<br>
    # primitive types are types for which the physical representation in arrow and in numpy
<br>
    # https://github.com/wesm/arrow/blob/c07b9b48cf3e0bbbab493992a492ae47e5b04cad/python/pyarrow/types.pxi#L821
<br>
    # see https://arrow.apache.org/docs/python/generated/pyarrow.Array.html#pyarrow.Array.to_numpy
<br>
    # and https://issues.apache.org/jira/browse/ARROW-2871?jql=text%20~%20%22boolean%20to_numpy%22
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ClassLabel:__call__' href='parser/test3/features.py#L267'>ClassLabel:__call__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ClassLabel:str2int' href='parser/test3/features.py#L609'>ClassLabel:str2int</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>values:  Union[str,<br>Iterable],<br></ul>
        <li>Docs:<br>        """Conversion class name string => integer."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ClassLabel:int2str' href='parser/test3/features.py#L637'>ClassLabel:int2str</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>values:  Union[int,<br>Iterable],<br></ul>
        <li>Docs:<br>        """Conversion integer => class name string."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ClassLabel:encode_example' href='parser/test3/features.py#L658'>ClassLabel:encode_example</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>example_data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:ClassLabel:_load_names_from_file' href='parser/test3/features.py#L677'>ClassLabel:_load_names_from_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>names_filepath,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Translation:__call__' href='parser/test3/features.py#L267'>Translation:__call__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """
<br>
    When converting a pyarrow array to a numpy array, we must know whether this could be done in zero-copy or not.
<br>
    This function returns the value of the ``zero_copy_only`` parameter to pass to ``.to_numpy()``, given the type of the pyarrow array.
<br>

<br>
    # zero copy is available for all primitive types except booleans
<br>
    # primitive types are types for which the physical representation in arrow and in numpy
<br>
    # https://github.com/wesm/arrow/blob/c07b9b48cf3e0bbbab493992a492ae47e5b04cad/python/pyarrow/types.pxi#L821
<br>
    # see https://arrow.apache.org/docs/python/generated/pyarrow.Array.html#pyarrow.Array.to_numpy
<br>
    # and https://issues.apache.org/jira/browse/ARROW-2871?jql=text%20~%20%22boolean%20to_numpy%22
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:TranslationVariableLanguages:__post_init__' href='parser/test3/features.py#L260'>TranslationVariableLanguages:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """
<br>
    When converting a pyarrow array to a numpy array, we must know whether this could be done in zero-copy or not.
<br>
    This function returns the value of the ``zero_copy_only`` parameter to pass to ``.to_numpy()``, given the type of the pyarrow array.
<br>

<br>
    # zero copy is available for all primitive types except booleans
<br>
    # primitive types are types for which the physical representation in arrow and in numpy
<br>
    # https://github.com/wesm/arrow/blob/c07b9b48cf3e0bbbab493992a492ae47e5b04cad/python/pyarrow/types.pxi#L821
<br>
    # see https://arrow.apache.org/docs/python/generated/pyarrow.Array.html#pyarrow.Array.to_numpy
<br>
    # and https://issues.apache.org/jira/browse/ARROW-2871?jql=text%20~%20%22boolean%20to_numpy%22
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:TranslationVariableLanguages:__call__' href='parser/test3/features.py#L267'>TranslationVariableLanguages:__call__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """
<br>
    When converting a pyarrow array to a numpy array, we must know whether this could be done in zero-copy or not.
<br>
    This function returns the value of the ``zero_copy_only`` parameter to pass to ``.to_numpy()``, given the type of the pyarrow array.
<br>

<br>
    # zero copy is available for all primitive types except booleans
<br>
    # primitive types are types for which the physical representation in arrow and in numpy
<br>
    # https://github.com/wesm/arrow/blob/c07b9b48cf3e0bbbab493992a492ae47e5b04cad/python/pyarrow/types.pxi#L821
<br>
    # see https://arrow.apache.org/docs/python/generated/pyarrow.Array.html#pyarrow.Array.to_numpy
<br>
    # and https://issues.apache.org/jira/browse/ARROW-2871?jql=text%20~%20%22boolean%20to_numpy%22
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:TranslationVariableLanguages:encode_example' href='parser/test3/features.py#L771'>TranslationVariableLanguages:encode_example</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>translation_dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Features:type' href='parser/test3/features.py#L955'>Features:type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Features field types.
<br>

<br>
        Returns:
<br>
            :obj:`pyarrow.DataType`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Features:from_arrow_schema' href='parser/test3/features.py#L965'>Features:from_arrow_schema</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>pa_schema:  pa.Schema,<br></ul>
        <li>Docs:<br>        """
<br>
        Construct Features from Arrow Schema.
<br>

<br>
        Args:
<br>
            pa_schema (:obj:`pyarrow.Schema`): Arrow Schema.
<br>

<br>
        Returns:
<br>
            :class:`Features`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Features:from_dict' href='parser/test3/features.py#L979'>Features:from_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>dic,<br></ul>
        <li>Docs:<br>        """
<br>
        Construct Features from dict.
<br>

<br>
        Regenerate the nested feature object from a deserialized dict.
<br>
        We use the '_type' key to infer the dataclass name of the feature FieldType.
<br>

<br>
        It allows for a convenient constructor syntax
<br>
        to define features from deserialized JSON dictionaries. This function is used in particular when deserializing
<br>
        a :class:`DatasetInfo` that was dumped to a JSON object. This acts as an analogue to
<br>
        :meth:`Features.from_arrow_schema` and handles the recursive field-by-field instantiation, but doesn't require
<br>
        any mapping to/from pyarrow, except for the fact that it takes advantage of the mapping of pyarrow primitive
<br>
        dtypes that :class:`Value` automatically performs.
<br>

<br>
        Args:
<br>
            dic (:obj:`dict[str, Any]`): Python dictionary.
<br>

<br>
        Returns:
<br>
            :class:`Features`
<br>

<br>
        Examples:
<br>
            >>> Features.from_dict({'_type': {'dtype': 'string', 'id': None, '_type': 'Value'}})
<br>
            {'_type': Value(dtype='string', id=None)}
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Features:encode_example' href='parser/test3/features.py#L1006'>Features:encode_example</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>example,<br></ul>
        <li>Docs:<br>        """
<br>
        Encode example into a format for Arrow.
<br>

<br>
        Args:
<br>
            example (:obj:`dict[str, Any]`): Data in a Dataset row.
<br>

<br>
        Returns:
<br>
            :obj:`dict[str, Any]`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Features:encode_batch' href='parser/test3/features.py#L1019'>Features:encode_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>batch,<br></ul>
        <li>Docs:<br>        """
<br>
        Encode batch into a format for Arrow.
<br>

<br>
        Args:
<br>
            batch (:obj:`dict[str, list[Any]]`): Data in a Dataset batch.
<br>

<br>
        Returns:
<br>
            :obj:`dict[str, list[Any]]`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Features:copy' href='parser/test3/features.py#L1037'>Features:copy</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Make a deep copy of Features.
<br>

<br>
        Returns:
<br>
            :class:`Features`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/features.py:Features:reorder_fields_as' href='parser/test3/features.py#L1046'>Features:reorder_fields_as</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other:  "Features",<br></ul>
        <li>Docs:<br>        """
<br>
        Reorder Features fields to match the field order of other Features.
<br>

<br>
        The order of the fields is important since it matters for the underlying arrow data.
<br>
        Re-ordering the fields allows to make the underlying arrow data type match.
<br>

<br>
        Args:
<br>
            other (:class:`Features`): The other Features to align with.
<br>

<br>
        Returns:
<br>
            :class:`Features`
<br>

<br>
        Examples:
<br>

<br>
            >>> from datasets import Features, Sequence, Value
<br>
            >>> # let's say we have to features with a different order of nested fields (for a and b for example)
<br>
            >>> f1 = Features({"root": Sequence({"a": Value("string"), "b": Value("string")})})
<br>
            >>> f2 = Features({"root": {"b": Sequence(Value("string")), "a": Sequence(Value("string"))}})
<br>
            >>> assert f1.type != f2.type
<br>
            >>> # re-ordering keeps the base structure (here Sequence is defined at the root level), but make the fields order match
<br>
            >>> f1.reorder_fields_as(f2)
<br>
            {'root': Sequence(feature={'b': Value(dtype='string', id=None), 'a': Value(dtype='string', id=None)}, length=-1, id=None)}
<br>
            >>> assert f1.reorder_fields_as(f2).type == f2.type
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/commands/datasets_cli.py' href='parser/test3/commands/datasets_cli.py'>parser/test3/commands/datasets_cli.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/commands/datasets_cli.py:main' href='parser/test3/commands/datasets_cli.py#L12'>main</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/deprecation_utils.py' href='parser/test3/utils/deprecation_utils.py'>parser/test3/utils/deprecation_utils.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/deprecation_utils.py:deprecated' href='parser/test3/utils/deprecation_utils.py#L12'>deprecated</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>help_message:  Optional[str]  =  None,<br></ul>
        <li>Docs:<br>    """Decorator to mark a function as deprecated.
<br>

<br>
    Args:
<br>
        help_message (`Optional[str]`): An optional message to guide the user on how to
<br>
            switch to non-deprecated usage of the library.
<br>
    """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/io/abc.py' href='parser/test3/io/abc.py'>parser/test3/io/abc.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/io/abc.py:AbstractDatasetReader' href='parser/test3/io/abc.py#L9'>AbstractDatasetReader</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/abc.py:AbstractDatasetReader:__init__' href='parser/test3/io/abc.py#L10'>AbstractDatasetReader:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_paths:  NestedDataStructureLike[PathLike],<br>split:  Optional[NamedSplit]  =  None,<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/abc.py:AbstractDatasetReader:read' href='parser/test3/io/abc.py#L27'>AbstractDatasetReader:read</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/metadata.py' href='parser/test3/utils/metadata.py'>parser/test3/utils/metadata.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/metadata.py:load_json_resource' href='parser/test3/utils/metadata.py#L26'>load_json_resource</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>resource:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/metadata.py:yaml_block_from_readme' href='parser/test3/utils/metadata.py#L57'>yaml_block_from_readme</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  Path,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/metadata.py:metadata_dict_from_readme' href='parser/test3/utils/metadata.py#L68'>metadata_dict_from_readme</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  Path,<br></ul>
        <li>Docs:<br>    """Loads a dataset's metadata from the dataset card (REAMDE.md), as a Python dict"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/metadata.py:tagset_validator' href='parser/test3/utils/metadata.py#L80'>tagset_validator</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>items:  Union[List[str],<br>Dict[str,<br>List[str]]],<br>reference_values:  List[str],<br>name:  str,<br>url:  str,<br>escape_validation_predicate_fn:  Optional[Callable[[Any],<br>bool]]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/metadata.py:validate_type' href='parser/test3/utils/metadata.py#L111'>validate_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>value:  Any,<br>expected_type:  Type,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/metadata.py:validate_metadata_type' href='parser/test3/utils/metadata.py#L171'>validate_metadata_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>metadata_dict:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/metadata.py:NoDuplicateSafeLoader' href='parser/test3/utils/metadata.py#L42'>NoDuplicateSafeLoader</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/metadata.py:DatasetMetadata' href='parser/test3/utils/metadata.py#L186'>DatasetMetadata</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:NoDuplicateSafeLoader:_check_no_duplicates_on_constructed_node' href='parser/test3/utils/metadata.py#L43'>NoDuplicateSafeLoader:_check_no_duplicates_on_constructed_node</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>node,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:NoDuplicateSafeLoader:construct_mapping' href='parser/test3/utils/metadata.py#L51'>NoDuplicateSafeLoader:construct_mapping</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>node,<br>deep = False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate' href='parser/test3/utils/metadata.py#L199'>DatasetMetadata:validate</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:from_readme' href='parser/test3/utils/metadata.py#L241'>DatasetMetadata:from_readme</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>path:  Path,<br></ul>
        <li>Docs:<br>        """Loads and validates the dataset metadat from its dataset card (README.md)
<br>

<br>
        Args:
<br>
            path (:obj:`Path`): Path to the dataset card (its README.md file)
<br>

<br>
        Returns:
<br>
            :class:`DatasetMetadata`: The dataset's metadata
<br>

<br>
        Raises:
<br>
            :obj:`TypeError`: If the dataset card has no metadata (no YAML header)
<br>
            :obj:`TypeError`: If the dataset's metadata is invalid
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:from_yaml_string' href='parser/test3/utils/metadata.py#L261'>DatasetMetadata:from_yaml_string</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>string:  str,<br></ul>
        <li>Docs:<br>        """Loads and validates the dataset metadat from a YAML string
<br>

<br>
        Args:
<br>
            string (:obj:`str`): The YAML string
<br>

<br>
        Returns:
<br>
            :class:`DatasetMetadata`: The dataset's metadata
<br>

<br>
        Raises:
<br>
            :obj:`TypeError`: If the dataset's metadata is invalid
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_annotations_creators' href='parser/test3/utils/metadata.py#L277'>DatasetMetadata:validate_annotations_creators</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>annotations_creators:  Union[List[str],<br>Dict[str,<br>List[str]]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_language_creators' href='parser/test3/utils/metadata.py#L283'>DatasetMetadata:validate_language_creators</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>language_creators:  Union[List[str],<br>Dict[str,<br>List[str]]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_language_codes' href='parser/test3/utils/metadata.py#L287'>DatasetMetadata:validate_language_codes</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>languages:  Union[List[str],<br>Dict[str,<br>List[str]]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_licences' href='parser/test3/utils/metadata.py#L291'>DatasetMetadata:validate_licences</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>licenses:  Union[List[str],<br>Dict[str,<br>List[str]]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_task_categories' href='parser/test3/utils/metadata.py#L302'>DatasetMetadata:validate_task_categories</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>task_categories:  Union[List[str],<br>Dict[str,<br>List[str]]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_task_ids' href='parser/test3/utils/metadata.py#L312'>DatasetMetadata:validate_task_ids</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>task_ids:  Union[List[str],<br>Dict[str,<br>List[str]]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_mulitlinguality' href='parser/test3/utils/metadata.py#L322'>DatasetMetadata:validate_mulitlinguality</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>multilinguality:  Union[List[str],<br>Dict[str,<br>List[str]]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_size_catgeories' href='parser/test3/utils/metadata.py#L333'>DatasetMetadata:validate_size_catgeories</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>size_cats:  Union[List[str],<br>Dict[str,<br>List[str]]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_source_datasets' href='parser/test3/utils/metadata.py#L337'>DatasetMetadata:validate_source_datasets</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>sources:  Union[List[str],<br>Dict[str,<br>List[str]]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_paperswithcode_id_errors' href='parser/test3/utils/metadata.py#L352'>DatasetMetadata:validate_paperswithcode_id_errors</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>paperswithcode_id:  Optional[str],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:validate_pretty_name' href='parser/test3/utils/metadata.py#L365'>DatasetMetadata:validate_pretty_name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>pretty_name:  Union[str,<br>Dict[str,<br>str]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/metadata.py:DatasetMetadata:get_metadata_by_config_name' href='parser/test3/utils/metadata.py#L380'>DatasetMetadata:get_metadata_by_config_name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>name:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/iterable_dataset.py' href='parser/test3/iterable_dataset.py'>parser/test3/iterable_dataset.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/iterable_dataset.py:_infer_features_from_batch' href='parser/test3/iterable_dataset.py#L16'>_infer_features_from_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>batch:  Dict[str,<br>list],<br>try_features:  Optional[Features]  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/iterable_dataset.py:_examples_to_batch' href='parser/test3/iterable_dataset.py#L26'>_examples_to_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>examples:  List[Dict[str,<br>Any]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/iterable_dataset.py:_batch_to_examples' href='parser/test3/iterable_dataset.py#L34'>_batch_to_examples</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>batch:  Dict[str,<br>list],<br></ul>
        <li>Docs:<br>    """Convert a batch (dict of examples) to examples list"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/iterable_dataset.py:_shuffle_kwargs' href='parser/test3/iterable_dataset.py#L60'>_shuffle_kwargs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>rng:  np.random.Generator,<br>kwargs:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/iterable_dataset.py:_generate_examples_from_tables_wrapper' href='parser/test3/iterable_dataset.py#L281'>_generate_examples_from_tables_wrapper</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>generate_tables_fn,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/iterable_dataset.py:iterable_dataset' href='parser/test3/iterable_dataset.py#L472'>iterable_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>ex_iterable:  Iterable,<br>info:  Optional[DatasetInfo]  =  None,<br>split:  Optional[NamedSplit]  =  None,<br>format_type:  Optional[str]  =  None,<br>shuffling:  Optional[ShuffingConfig]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:_BaseExamplesIterable' href='parser/test3/iterable_dataset.py#L41'>_BaseExamplesIterable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:ExamplesIterable' href='parser/test3/iterable_dataset.py#L72'>ExamplesIterable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:ShardShuffledExamplesIterable' href='parser/test3/iterable_dataset.py#L90'>ShardShuffledExamplesIterable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:CyclingMultiSourcesExamplesIterable' href='parser/test3/iterable_dataset.py#L103'>CyclingMultiSourcesExamplesIterable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:RandomlyCyclingMultiSourcesExamplesIterable' href='parser/test3/iterable_dataset.py#L127'>RandomlyCyclingMultiSourcesExamplesIterable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:MappedExamplesIterable' href='parser/test3/iterable_dataset.py#L165'>MappedExamplesIterable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:BufferShuffledExamplesIterable' href='parser/test3/iterable_dataset.py#L205'>BufferShuffledExamplesIterable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:SkipExamplesIterable' href='parser/test3/iterable_dataset.py#L244'>SkipExamplesIterable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:TakeExamplesIterable' href='parser/test3/iterable_dataset.py#L264'>TakeExamplesIterable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:ShuffingConfig' href='parser/test3/iterable_dataset.py#L293'>ShuffingConfig</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/iterable_dataset.py:IterableDataset' href='parser/test3/iterable_dataset.py#L297'>IterableDataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:_BaseExamplesIterable:__iter__' href='parser/test3/iterable_dataset.py#L44'>_BaseExamplesIterable:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:_BaseExamplesIterable:shuffle_data_sources' href='parser/test3/iterable_dataset.py#L48'>_BaseExamplesIterable:shuffle_data_sources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br>        """
<br>
        Either shuffle the shards/sources of the dataset, or propagate the shuffling to the underlying iterable.
<br>
        If the order of the shards must stay fixed (when using .skip or .take for example), then this method returns self.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:_BaseExamplesIterable:n_shards' href='parser/test3/iterable_dataset.py#L56'>_BaseExamplesIterable:n_shards</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:ExamplesIterable:__init__' href='parser/test3/iterable_dataset.py#L73'>ExamplesIterable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>generate_examples_fn:  Callable,<br>kwargs:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:ExamplesIterable:__iter__' href='parser/test3/iterable_dataset.py#L44'>ExamplesIterable:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:ExamplesIterable:shuffle_data_sources' href='parser/test3/iterable_dataset.py#L81'>ExamplesIterable:shuffle_data_sources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:ExamplesIterable:n_shards' href='parser/test3/iterable_dataset.py#L56'>ExamplesIterable:n_shards</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:ShardShuffledExamplesIterable:__init__' href='parser/test3/iterable_dataset.py#L91'>ShardShuffledExamplesIterable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>generate_examples_fn:  Callable,<br>kwargs:  dict,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:ShardShuffledExamplesIterable:__iter__' href='parser/test3/iterable_dataset.py#L44'>ShardShuffledExamplesIterable:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:CyclingMultiSourcesExamplesIterable:__init__' href='parser/test3/iterable_dataset.py#L104'>CyclingMultiSourcesExamplesIterable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>ex_iterables:  List[_BaseExamplesIterable],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:CyclingMultiSourcesExamplesIterable:__iter__' href='parser/test3/iterable_dataset.py#L44'>CyclingMultiSourcesExamplesIterable:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:CyclingMultiSourcesExamplesIterable:shuffle_data_sources' href='parser/test3/iterable_dataset.py#L117'>CyclingMultiSourcesExamplesIterable:shuffle_data_sources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br>        """Shuffle each underlying examples iterable."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:CyclingMultiSourcesExamplesIterable:n_shards' href='parser/test3/iterable_dataset.py#L56'>CyclingMultiSourcesExamplesIterable:n_shards</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Shuffle the kwargs order to shuffle shards"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:RandomlyCyclingMultiSourcesExamplesIterable:__init__' href='parser/test3/iterable_dataset.py#L128'>RandomlyCyclingMultiSourcesExamplesIterable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>ex_iterables,<br>seed:  Optional[int]  =  None,<br>probabilities:  Optional[List[float]]  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:RandomlyCyclingMultiSourcesExamplesIterable:_iter_random_indices' href='parser/test3/iterable_dataset.py#L134'>RandomlyCyclingMultiSourcesExamplesIterable:_iter_random_indices</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>rng:  np.random.Generator,<br>num_sources:  int,<br>random_batch_size = 1000,<br>p:  Optional[List[float]]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Get an infinite iterator that randomly samples the index of the source to pick examples from."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:RandomlyCyclingMultiSourcesExamplesIterable:__iter__' href='parser/test3/iterable_dataset.py#L44'>RandomlyCyclingMultiSourcesExamplesIterable:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:RandomlyCyclingMultiSourcesExamplesIterable:shuffle_data_sources' href='parser/test3/iterable_dataset.py#L159'>RandomlyCyclingMultiSourcesExamplesIterable:shuffle_data_sources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br>        """Shuffle the data sources of each wrapped examples iterable."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:MappedExamplesIterable:__init__' href='parser/test3/iterable_dataset.py#L166'>MappedExamplesIterable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>ex_iterable:  _BaseExamplesIterable,<br>function:  Callable,<br>batched:  bool  =  False,<br>batch_size:  int  =  1000,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:MappedExamplesIterable:__iter__' href='parser/test3/iterable_dataset.py#L44'>MappedExamplesIterable:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:MappedExamplesIterable:shuffle_data_sources' href='parser/test3/iterable_dataset.py#L194'>MappedExamplesIterable:shuffle_data_sources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br>        """Shuffle the wrapped examples iterable."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:MappedExamplesIterable:n_shards' href='parser/test3/iterable_dataset.py#L56'>MappedExamplesIterable:n_shards</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Shuffle the kwargs order to shuffle shards"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:BufferShuffledExamplesIterable:__init__' href='parser/test3/iterable_dataset.py#L206'>BufferShuffledExamplesIterable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>ex_iterable:  _BaseExamplesIterable,<br>buffer_size:  int,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:BufferShuffledExamplesIterable:_iter_random_indices' href='parser/test3/iterable_dataset.py#L212'>BufferShuffledExamplesIterable:_iter_random_indices</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>rng:  np.random.Generator,<br>buffer_size:  int,<br>random_batch_size = 1000,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:BufferShuffledExamplesIterable:__iter__' href='parser/test3/iterable_dataset.py#L44'>BufferShuffledExamplesIterable:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:BufferShuffledExamplesIterable:shuffle_data_sources' href='parser/test3/iterable_dataset.py#L233'>BufferShuffledExamplesIterable:shuffle_data_sources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br>        """Shuffle the wrapped examples iterable as well as the shuffling buffer."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:BufferShuffledExamplesIterable:n_shards' href='parser/test3/iterable_dataset.py#L56'>BufferShuffledExamplesIterable:n_shards</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Shuffle the kwargs order to shuffle shards"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:SkipExamplesIterable:__init__' href='parser/test3/iterable_dataset.py#L245'>SkipExamplesIterable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>ex_iterable:  _BaseExamplesIterable,<br>n:  int,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:SkipExamplesIterable:__iter__' href='parser/test3/iterable_dataset.py#L44'>SkipExamplesIterable:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:SkipExamplesIterable:shuffle_data_sources' href='parser/test3/iterable_dataset.py#L255'>SkipExamplesIterable:shuffle_data_sources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br>        """Doesn't shuffle the wrapped examples iterable since it would skip exampels from other shards instead."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:SkipExamplesIterable:n_shards' href='parser/test3/iterable_dataset.py#L56'>SkipExamplesIterable:n_shards</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Shuffle the kwargs order to shuffle shards"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:TakeExamplesIterable:__init__' href='parser/test3/iterable_dataset.py#L245'>TakeExamplesIterable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>ex_iterable:  _BaseExamplesIterable,<br>n:  int,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:TakeExamplesIterable:__iter__' href='parser/test3/iterable_dataset.py#L44'>TakeExamplesIterable:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:TakeExamplesIterable:shuffle_data_sources' href='parser/test3/iterable_dataset.py#L272'>TakeExamplesIterable:shuffle_data_sources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seed:  Optional[int],<br></ul>
        <li>Docs:<br>        """Doesn't shuffle the wrapped examples iterable since it would take examples from other shards instead."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:TakeExamplesIterable:n_shards' href='parser/test3/iterable_dataset.py#L56'>TakeExamplesIterable:n_shards</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Shuffle the kwargs order to shuffle shards"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:__init__' href='parser/test3/iterable_dataset.py#L166'>IterableDataset:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>ex_iterable:  _BaseExamplesIterable,<br>info:  Optional[DatasetInfo]  =  None,<br>split:  Optional[NamedSplit]  =  None,<br>format_type:  Optional[str]  =  None,<br>shuffling:  Optional[ShuffingConfig]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Shuffle the wrapped examples iterable."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:_head' href='parser/test3/iterable_dataset.py#L316'>IterableDataset:_head</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>n = 5,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:_effective_seed' href='parser/test3/iterable_dataset.py#L320'>IterableDataset:_effective_seed</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:n_shards' href='parser/test3/iterable_dataset.py#L56'>IterableDataset:n_shards</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Shuffle the kwargs order to shuffle shards"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:_iter' href='parser/test3/iterable_dataset.py#L330'>IterableDataset:_iter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:__iter__' href='parser/test3/iterable_dataset.py#L44'>IterableDataset:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:with_format' href='parser/test3/iterable_dataset.py#L345'>IterableDataset:with_format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>type:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """
<br>
        Return a dataset with the specified format.
<br>
        This method only supports the "torch" format for now.
<br>

<br>
        Args:
<br>

<br>
            type (:obj:`str`, optional, default None): if set to "torch", the returned dataset
<br>
                will be a subclass of torch.utils.data.IterableDataset to be used in a DataLoader
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:map' href='parser/test3/iterable_dataset.py#L370'>IterableDataset:map</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>function:  Callable,<br>batched:  bool  =  False,<br>batch_size:  int  =  1000,<br></ul>
        <li>Docs:<br>        """
<br>
        Return a dataset with the specified map function. The function is applied on-the-fly on the examples when iterating over the dataset.
<br>

<br>
        You can specify whether the function should be batched or not with the ``batched`` parameter:
<br>

<br>
        - If batched is False, then the function takes 1 example in and should return 1 example.
<br>
          An example is a dictionary, e.g. {"text": "Hello there !"}
<br>
        - If batched is True and batch_size is 1, then the function takes a batch of 1 example as input and can return a batch with 1 or more examples.
<br>
          A batch is a dictionary, e.g. a batch of 1 example is {"text": ["Hello there !"]}
<br>
        - If batched is True and batch_size is ``n`` > 1, then the function takes a batch of ``n`` examples as input and can return a batch with ``n`` examples, or with an arbitrary number of examples.
<br>
          Note that the last batch may have less than ``n`` examples.
<br>
          A batch is a dictionary, e.g. a batch of ``n`` examples is {"text": ["Hello there !"] * n}
<br>

<br>
        Args:
<br>
            function (:obj:`Callable`, optional, default None): if not None, this function is applied
<br>
                on-the-fly on the examples when you iterate on the dataset.
<br>
            batched (:obj:`bool`, default `False`): Provide batch of examples to `function`.
<br>
            batch_size (:obj:`int`, optional, default ``1000``): Number of examples per batch provided to `function` if `batched=True`.
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:shuffle' href='parser/test3/iterable_dataset.py#L404'>IterableDataset:shuffle</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>buffer_size,<br>seed = None,<br></ul>
        <li>Docs:<br>        """
<br>
        Randomly shuffles the elements of this dataset.
<br>

<br>
        This dataset fills a buffer with buffer_size elements, then randomly samples elements from this buffer,
<br>
        replacing the selected elements with new elements. For perfect shuffling, a buffer size greater than or
<br>
        equal to the full size of the dataset is required.
<br>

<br>
        For instance, if your dataset contains 10,000 elements but ``buffer_size`` is set to 1,000, then shuffle will
<br>
        initially select a random element from only the first 1,000 elements in the buffer. Once an element is
<br>
        selected, its space in the buffer is replaced by the next (i.e. 1,001-st) element,
<br>
        maintaining the 1,000 element buffer.
<br>

<br>
        If the dataset is made of several shards, it also does shuffle the order of the shards.
<br>
        However if the order has been fixed by using :func:`datasets.IterableDataset.skip` or :func:`datasets.IterableDataset.take`
<br>
        then the order of the shards is kept unchanged.
<br>

<br>
        Args:
<br>
            buffer_size (:obj:`int`): size of the buffer.
<br>
            seed (:obj:`int`, optional, default None): random seed that will be used to create the distribution.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:set_epoch' href='parser/test3/iterable_dataset.py#L436'>IterableDataset:set_epoch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>epoch:  int,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:skip' href='parser/test3/iterable_dataset.py#L439'>IterableDataset:skip</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>n,<br></ul>
        <li>Docs:<br>        """
<br>
        Create a new IterableDataset that skips the first ``n`` elements.
<br>

<br>
        Args:
<br>
            n (:obj:`int`): number of elements to skip.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/iterable_dataset.py:IterableDataset:take' href='parser/test3/iterable_dataset.py#L455'>IterableDataset:take</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>n,<br></ul>
        <li>Docs:<br>        """
<br>
        Create a new IterableDataset with only the first ``n`` elements.
<br>

<br>
        Args:
<br>
            n (:obj:`int`): number of elements to take.
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/tqdm_utils.py' href='parser/test3/utils/tqdm_utils.py'>parser/test3/utils/tqdm_utils.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/tqdm_utils.py:tqdm' href='parser/test3/utils/tqdm_utils.py#L52'>tqdm</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/tqdm_utils.py:async_tqdm' href='parser/test3/utils/tqdm_utils.py#L59'>async_tqdm</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/tqdm_utils.py:disable_progress_bar' href='parser/test3/utils/tqdm_utils.py#L66'>disable_progress_bar</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Disabled Tqdm progress bar.
<br>

<br>
    Usage:
<br>

<br>
    datasets.disable_progress_bar()
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/tqdm_utils.py:_async_tqdm' href='parser/test3/utils/tqdm_utils.py#L79'>_async_tqdm</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """Wrapper around Tqdm which can be updated in threads.
<br>

<br>
    Usage:
<br>

<br>
    ```
<br>
    with utils.async_tqdm(...) as pbar:
<br>
        # pbar can then be modified inside a thread
<br>
        # pbar.update_total(3)
<br>
        # pbar.update()
<br>
    ```
<br>

<br>
    Args:
<br>
        *args: args of tqdm
<br>
        **kwargs: kwargs of tqdm
<br>

<br>
    Yields:
<br>
        pbar: Async pbar which can be shared between threads.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/tqdm_utils.py:EmptyTqdm' href='parser/test3/utils/tqdm_utils.py#L25'>EmptyTqdm</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/tqdm_utils.py:_TqdmPbarAsync' href='parser/test3/utils/tqdm_utils.py#L105'>_TqdmPbarAsync</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:EmptyTqdm:__init__' href='parser/test3/utils/tqdm_utils.py#L28'>EmptyTqdm:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs):   # pylint: disable = unused-argumentself._iterator = args[0] if args else Noneself):,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:EmptyTqdm:__iter__' href='parser/test3/utils/tqdm_utils.py#L31'>EmptyTqdm:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:EmptyTqdm:__getattr__' href='parser/test3/utils/tqdm_utils.py#L34'>EmptyTqdm:__getattr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>_,<br></ul>
        <li>Docs:<br>        """Return empty function."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:EmptyTqdm:__enter__' href='parser/test3/utils/tqdm_utils.py#L42'>EmptyTqdm:__enter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:EmptyTqdm:__exit__' href='parser/test3/utils/tqdm_utils.py#L45'>EmptyTqdm:__exit__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>type_,<br>value,<br>traceback,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:_TqdmPbarAsync:__init__' href='parser/test3/utils/tqdm_utils.py#L110'>_TqdmPbarAsync:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pbar,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:_TqdmPbarAsync:update_total' href='parser/test3/utils/tqdm_utils.py#L115'>_TqdmPbarAsync:update_total</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>n = 1,<br></ul>
        <li>Docs:<br>        """Increment total pbar value."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:_TqdmPbarAsync:update' href='parser/test3/utils/tqdm_utils.py#L121'>_TqdmPbarAsync:update</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>n = 1,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:_TqdmPbarAsync:refresh' href='parser/test3/utils/tqdm_utils.py#L127'>_TqdmPbarAsync:refresh</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Refresh all."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/tqdm_utils.py:_TqdmPbarAsync:clear' href='parser/test3/utils/tqdm_utils.py#L132'>_TqdmPbarAsync:clear</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Remove the tqdm pbar from the update."""
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/formatting/__init__.py' href='parser/test3/formatting/__init__.py'>parser/test3/formatting/__init__.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/__init__.py:_register_formatter' href='parser/test3/formatting/__init__.py#L42'>_register_formatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>formatter_cls:  type,<br>format_type:  Optional[str],<br>aliases:  Optional[List[str]]  =  None,<br></ul>
        <li>Docs:<br>    """
<br>
    Register a Formatter object using a name and optional aliases.
<br>
    This function must be used on a Formatter class.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/__init__.py:_register_unavailable_formatter' href='parser/test3/formatting/__init__.py#L61'>_register_unavailable_formatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>unavailable_error:  Exception,<br>format_type:  Optional[str],<br>aliases:  Optional[List[str]]  =  None,<br></ul>
        <li>Docs:<br>    """
<br>
    Register an unavailable Formatter object using a name and optional aliases.
<br>
    This function must be used on an Exception object that is raised when trying to get the unavailable formatter.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/__init__.py:get_format_type_from_alias' href='parser/test3/formatting/__init__.py#L105'>get_format_type_from_alias</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>format_type:  Optional[str],<br></ul>
        <li>Docs:<br>    """If the given format type is a known alias, then return its main type name. Otherwise return the type with no change."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/__init__.py:get_formatter' href='parser/test3/formatting/__init__.py#L113'>get_formatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>format_type:  Optional[str],<br>**format_kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    Factory function to get a Formatter given its type name and keyword arguments.
<br>
    A formatter is an object that extracts and formats data from pyarrow table.
<br>
    It defines the formatting for rows, colums and batches.
<br>
    If the formatter for a given type name doesn't exist or is not available, an error is raised.
<br>
    """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/formatting/formatting.py' href='parser/test3/formatting/formatting.py'>parser/test3/formatting/formatting.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:_is_range_contiguous' href='parser/test3/formatting/formatting.py#L34'>_is_range_contiguous</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>key:  range,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:_raise_bad_key_type' href='parser/test3/formatting/formatting.py#L38'>_raise_bad_key_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>key:  Any,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:_query_table_with_indices_mapping' href='parser/test3/formatting/formatting.py#L44'>_query_table_with_indices_mapping</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>table:  Table,<br>key:  Union[int,<br>slice,<br>range,<br>str,<br>Iterable],<br>indices:  Table,<br></ul>
        <li>Docs:<br>    """
<br>
    Query a pyarrow Table to extract the subtable that correspond to the given key.
<br>
    The :obj:`indices` parameter corresponds to the indices mapping in case we cant to take into
<br>
    account a shuffling or an indices selection for example.
<br>
    The indices table must contain one column named "indices" of type uint64.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:_query_table' href='parser/test3/formatting/formatting.py#L74'>_query_table</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>table:  Table,<br>key:  Union[int,<br>slice,<br>range,<br>str,<br>Iterable],<br>indices:  Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:_unnest' href='parser/test3/formatting/formatting.py#L116'>_unnest</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>py_dict:  Dict[str,<br>List[T]],<br></ul>
        <li>Docs:<br>    """Return the first element of a batch (dict) as a row (dict)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:_check_valid_column_key' href='parser/test3/formatting/formatting.py#L303'>_check_valid_column_key</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>key:  str,<br>columns:  List[str],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:_check_valid_index_key' href='parser/test3/formatting/formatting.py#L308'>_check_valid_index_key</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>key:  Union[int,<br>slice,<br>range,<br>Iterable],<br>size:  int,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:key_to_query_type' href='parser/test3/formatting/formatting.py#L327'>key_to_query_type</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>key:  Union[int,<br>slice,<br>range,<br>str,<br>Iterable],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:query_table' href='parser/test3/formatting/formatting.py#L337'>query_table</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>table:  Table,<br>key:  Union[int,<br>slice,<br>range,<br>str,<br>Iterable],<br>indices:  Optional[Table]  =  None,<br>,<br></ul>
        <li>Docs:<br>    """
<br>
    Query a Table to extract the subtable that correspond to the given key.
<br>

<br>
    Args:
<br>
        table (``datasets.table.Table``): The input Table to query from
<br>
        key (``Union[int, slice, range, str, Iterable]``): The key can be of different types:
<br>
            - an integer i: the subtable containing only the i-th row
<br>
            - a slice [i:j:k]: the subtable containing the rows that correspond to this slice
<br>
            - a range(i, j, k): the subtable containing the rows that correspond to this range
<br>
            - a string c: the subtable containing all the rows but only the column c
<br>
            - an iterable l: the subtable that is the concatenation of all the i-th rows for all i in the iterable
<br>
        indices (Optional ``datasets.table.Table``): If not None, it is used to re-map the given key to the table rows.
<br>
            The indices table must contain one column named "indices" of type uint64.
<br>
            This is used in case of shuffling or rows selection.
<br>

<br>

<br>
    Returns:
<br>
        ``pyarrow.Table``: the result of the query on the input table
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/formatting/formatting.py:format_table' href='parser/test3/formatting/formatting.py#L377'>format_table</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>table:  Table,<br>key:  Union[int,<br>slice,<br>range,<br>str,<br>Iterable],<br>formatter:  Formatter,<br>format_columns:  Optional[list]  =  None,<br>output_all_columns = False,<br>,<br></ul>
        <li>Docs:<br>    """
<br>
    Format a Table depending on the key that was used and a Formatter object.
<br>

<br>
    Args:
<br>
        table (``datasets.table.Table``): The input Table to format
<br>
        key (``Union[int, slice, range, str, Iterable]``): Depending on the key that was used, the formatter formats
<br>
            the table as either a row, a column or a batch.
<br>
        formatter (``datasets.formatting.formatting.Formatter``): Any subclass of a Formatter such as
<br>
            PythonFormatter, NumpyFormatter, etc.
<br>
        format_columns (Optional ``List[str]``): if not None, it defines the columns that will be formatted using the
<br>
            given formatter. Other columns are discarded (unless ``output_all_columns`` is True)
<br>
        output_all_columns (``bool``, defaults to False). If True, the formatted output is completed using the columns
<br>
            that are not in the ``format_columns`` list. For these columns, the PythonFormatter is used.
<br>

<br>

<br>
    Returns:
<br>
        A row, column or batch formatted object defined by the Formatter:
<br>
        - the PythonFormatter returns a dictionary for a row or a batch, and a list for a column.
<br>
        - the NumpyFormatter returns a dictionary for a row or a batch, and a np.array for a column.
<br>
        - the PandasFormatter returns a pd.DataFrame for a row or a batch, and a pd.Series for a column.
<br>
        - the TorchFormatter returns a dictionary for a row or a batch, and a torch.Tensor for a column.
<br>
        - the TFFormatter returns a dictionary for a row or a batch, and a tf.Tensor for a column.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:BaseArrowExtractor' href='parser/test3/formatting/formatting.py#L99'>BaseArrowExtractor</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:SimpleArrowExtractor' href='parser/test3/formatting/formatting.py#L121'>SimpleArrowExtractor</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:PythonArrowExtractor' href='parser/test3/formatting/formatting.py#L132'>PythonArrowExtractor</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:NumpyArrowExtractor' href='parser/test3/formatting/formatting.py#L143'>NumpyArrowExtractor</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:PandasArrowExtractor' href='parser/test3/formatting/formatting.py#L170'>PandasArrowExtractor</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:Formatter' href='parser/test3/formatting/formatting.py#L181'>Formatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:ArrowFormatter' href='parser/test3/formatting/formatting.py#L210'>ArrowFormatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:PythonFormatter' href='parser/test3/formatting/formatting.py#L221'>PythonFormatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:NumpyFormatter' href='parser/test3/formatting/formatting.py#L232'>NumpyFormatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:PandasFormatter' href='parser/test3/formatting/formatting.py#L246'>PandasFormatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/formatting.py:CustomFormatter' href='parser/test3/formatting/formatting.py#L257'>CustomFormatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:BaseArrowExtractor:extract_row' href='parser/test3/formatting/formatting.py#L106'>BaseArrowExtractor:extract_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:BaseArrowExtractor:extract_column' href='parser/test3/formatting/formatting.py#L109'>BaseArrowExtractor:extract_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:BaseArrowExtractor:extract_batch' href='parser/test3/formatting/formatting.py#L112'>BaseArrowExtractor:extract_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:SimpleArrowExtractor:extract_row' href='parser/test3/formatting/formatting.py#L122'>SimpleArrowExtractor:extract_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:SimpleArrowExtractor:extract_column' href='parser/test3/formatting/formatting.py#L125'>SimpleArrowExtractor:extract_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:SimpleArrowExtractor:extract_batch' href='parser/test3/formatting/formatting.py#L128'>SimpleArrowExtractor:extract_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PythonArrowExtractor:extract_row' href='parser/test3/formatting/formatting.py#L133'>PythonArrowExtractor:extract_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PythonArrowExtractor:extract_column' href='parser/test3/formatting/formatting.py#L136'>PythonArrowExtractor:extract_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PythonArrowExtractor:extract_batch' href='parser/test3/formatting/formatting.py#L139'>PythonArrowExtractor:extract_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:NumpyArrowExtractor:__init__' href='parser/test3/formatting/formatting.py#L144'>NumpyArrowExtractor:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>**np_array_kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:NumpyArrowExtractor:extract_row' href='parser/test3/formatting/formatting.py#L133'>NumpyArrowExtractor:extract_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:NumpyArrowExtractor:extract_column' href='parser/test3/formatting/formatting.py#L150'>NumpyArrowExtractor:extract_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:NumpyArrowExtractor:extract_batch' href='parser/test3/formatting/formatting.py#L139'>NumpyArrowExtractor:extract_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:NumpyArrowExtractor:_arrow_array_to_numpy' href='parser/test3/formatting/formatting.py#L156'>NumpyArrowExtractor:_arrow_array_to_numpy</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_array:  pa.Array,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PandasArrowExtractor:extract_row' href='parser/test3/formatting/formatting.py#L171'>PandasArrowExtractor:extract_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PandasArrowExtractor:extract_column' href='parser/test3/formatting/formatting.py#L174'>PandasArrowExtractor:extract_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PandasArrowExtractor:extract_batch' href='parser/test3/formatting/formatting.py#L177'>PandasArrowExtractor:extract_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:Formatter:__call__' href='parser/test3/formatting/formatting.py#L192'>Formatter:__call__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br>query_type:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:Formatter:format_row' href='parser/test3/formatting/formatting.py#L200'>Formatter:format_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:Formatter:format_column' href='parser/test3/formatting/formatting.py#L203'>Formatter:format_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:Formatter:format_batch' href='parser/test3/formatting/formatting.py#L206'>Formatter:format_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:ArrowFormatter:format_row' href='parser/test3/formatting/formatting.py#L211'>ArrowFormatter:format_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:ArrowFormatter:format_column' href='parser/test3/formatting/formatting.py#L214'>ArrowFormatter:format_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:ArrowFormatter:format_batch' href='parser/test3/formatting/formatting.py#L217'>ArrowFormatter:format_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PythonFormatter:format_row' href='parser/test3/formatting/formatting.py#L222'>PythonFormatter:format_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PythonFormatter:format_column' href='parser/test3/formatting/formatting.py#L225'>PythonFormatter:format_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PythonFormatter:format_batch' href='parser/test3/formatting/formatting.py#L228'>PythonFormatter:format_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:NumpyFormatter:__init__' href='parser/test3/formatting/formatting.py#L144'>NumpyFormatter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>**np_array_kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:NumpyFormatter:format_row' href='parser/test3/formatting/formatting.py#L222'>NumpyFormatter:format_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:NumpyFormatter:format_column' href='parser/test3/formatting/formatting.py#L239'>NumpyFormatter:format_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:NumpyFormatter:format_batch' href='parser/test3/formatting/formatting.py#L228'>NumpyFormatter:format_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PandasFormatter:format_row' href='parser/test3/formatting/formatting.py#L247'>PandasFormatter:format_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PandasFormatter:format_column' href='parser/test3/formatting/formatting.py#L250'>PandasFormatter:format_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:PandasFormatter:format_batch' href='parser/test3/formatting/formatting.py#L253'>PandasFormatter:format_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:CustomFormatter:__init__' href='parser/test3/formatting/formatting.py#L267'>CustomFormatter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>transform:  Callable[[dict],<br>dict],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:CustomFormatter:format_row' href='parser/test3/formatting/formatting.py#L222'>CustomFormatter:format_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br>    """
<br>
    A user-defined custom formatter function defined by a ``transform``.
<br>
    The transform must take as input a batch of data extracted for an arrow table using the python extractor,
<br>
    and return a batch.
<br>
    If the output batch is not a dict, then output_all_columns won't work.
<br>
    If the ouput batch has several fields, then querying a single column won't work since we don't know which field
<br>
    to return.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:CustomFormatter:format_column' href='parser/test3/formatting/formatting.py#L203'>CustomFormatter:format_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br>    """
<br>
    A user-defined custom formatter function defined by a ``transform``.
<br>
    The transform must take as input a batch of data extracted for an arrow table using the python extractor,
<br>
    and return a batch.
<br>
    If the output batch is not a dict, then output_all_columns won't work.
<br>
    If the ouput batch has several fields, then querying a single column won't work since we don't know which field
<br>
    to return.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/formatting.py:CustomFormatter:format_batch' href='parser/test3/formatting/formatting.py#L228'>CustomFormatter:format_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br>    """
<br>
    A user-defined custom formatter function defined by a ``transform``.
<br>
    The transform must take as input a batch of data extracted for an arrow table using the python extractor,
<br>
    and return a batch.
<br>
    If the output batch is not a dict, then output_all_columns won't work.
<br>
    If the ouput batch has several fields, then querying a single column won't work since we don't know which field
<br>
    to return.
<br>
    """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/search.py' href='parser/test3/search.py'>parser/test3/search.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/search.py:MissingIndex' href='parser/test3/search.py#L34'>MissingIndex</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/search.py:BaseIndex' href='parser/test3/search.py#L49'>BaseIndex</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/search.py:ElasticSearchIndex' href='parser/test3/search.py#L87'>ElasticSearchIndex</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/search.py:FaissIndex' href='parser/test3/search.py#L190'>FaissIndex</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/search.py:IndexableMixin' href='parser/test3/search.py#L345'>IndexableMixin</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:BaseIndex:search' href='parser/test3/search.py#L52'>BaseIndex:search</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>query,<br>k:  int  =  10,<br></ul>
        <li>Docs:<br>        """
<br>
        To implement.
<br>
        This method has to return the scores and the indices of the retrieved examples given a certain query.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:BaseIndex:search_batch' href='parser/test3/search.py#L59'>BaseIndex:search_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>queries,<br>k:  int  =  10,<br></ul>
        <li>Docs:<br>        """Find the nearest examples indices to the query.
<br>

<br>
        Args:
<br>
            queries (`Union[List[str], np.ndarray]`): The queries as a list of strings if `column` is a text index or as a numpy array if `column` is a vector index.
<br>
            k (`int`): The number of examples to retrieve per query.
<br>

<br>
        Ouput:
<br>
            total_scores (`List[List[float]`): The retrieval scores of the retrieved examples per query.
<br>
            total_indices (`List[List[int]]`): The indices of the retrieved examples per query.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:BaseIndex:save' href='parser/test3/search.py#L77'>BaseIndex:save</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>file:  Union[str,<br>PurePath],<br></ul>
        <li>Docs:<br>        """Serialize the index on disk"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:BaseIndex:load' href='parser/test3/search.py#L82'>BaseIndex:load</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>file:  Union[str,<br>PurePath],<br></ul>
        <li>Docs:<br>        """Deserialize the index from disk"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:ElasticSearchIndex:__init__' href='parser/test3/search.py#L97'>ElasticSearchIndex:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>host:  Optional[str]  =  None,<br>port:  Optional[int]  =  None,<br>es_client:  Optional["Elasticsearch"]  =  None,<br>es_index_name:  Optional[str]  =  None,<br>es_index_config:  Optional[dict]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:ElasticSearchIndex:add_documents' href='parser/test3/search.py#L135'>ElasticSearchIndex:add_documents</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>documents:  Union[List[str],<br>"Dataset"],<br>column:  Optional[str]  =  None,<br></ul>
        <li>Docs:<br>        """
<br>
        Add documents to the index.
<br>
        If the documents are inside a certain column, you can specify it using the `column` argument.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:ElasticSearchIndex:search' href='parser/test3/search.py#L171'>ElasticSearchIndex:search</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>query:  str,<br>k = 10,<br></ul>
        <li>Docs:<br>        """Find the nearest examples indices to the query.
<br>

<br>
        Args:
<br>
            query (`str`): The query as a string.
<br>
            k (`int`): The number of examples to retrieve.
<br>

<br>
        Ouput:
<br>
            scores (`List[List[float]`): The retrieval scores of the retrieved examples.
<br>
            indices (`List[List[int]]`): The indices of the retrieved examples.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:FaissIndex:__init__' href='parser/test3/search.py#L97'>FaissIndex:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>device:  Optional[int]  =  None,<br>string_factory:  Optional[str]  =  None,<br>metric_type:  Optional[int]  =  None,<br>custom_index:  Optional["faiss.Index"]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """
<br>
        Add documents to the index.
<br>
        If the documents are inside a certain column, you can specify it using the `column` argument.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:FaissIndex:add_vectors' href='parser/test3/search.py#L224'>FaissIndex:add_vectors</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>vectors:  Union[np.array,<br>"Dataset"],<br>column:  Optional[str]  =  None,<br>batch_size:  int  =  1000,<br>train_size:  Optional[int]  =  None,<br>faiss_verbose:  Optional[bool]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """
<br>
        Add vectors to the index.
<br>
        If the arrays are inside a certain column, you can specify it using the `column` argument.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:FaissIndex:search' href='parser/test3/search.py#L281'>FaissIndex:search</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>query:  np.array,<br>k = 10,<br></ul>
        <li>Docs:<br>        """Find the nearest examples indices to the query.
<br>

<br>
        Args:
<br>
            query (`np.array`): The query as a numpy array.
<br>
            k (`int`): The number of examples to retrieve.
<br>

<br>
        Ouput:
<br>
            scores (`List[List[float]`): The retrieval scores of the retrieved examples.
<br>
            indices (`List[List[int]]`): The indices of the retrieved examples.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:FaissIndex:search_batch' href='parser/test3/search.py#L299'>FaissIndex:search_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>queries:  np.array,<br>k = 10,<br></ul>
        <li>Docs:<br>        """Find the nearest examples indices to the queries.
<br>

<br>
        Args:
<br>
            queries (`np.array`): The queries as a numpy array.
<br>
            k (`int`): The number of examples to retrieve.
<br>

<br>
        Ouput:
<br>
            total_scores (`List[List[float]`): The retrieval scores of the retrieved examples per query.
<br>
            total_indices (`List[List[int]]`): The indices of the retrieved examples per query.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:FaissIndex:save' href='parser/test3/search.py#L77'>FaissIndex:save</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>file:  Union[str,<br>PurePath],<br></ul>
        <li>Docs:<br>        """Serialize the index on disk"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:FaissIndex:load' href='parser/test3/search.py#L328'>FaissIndex:load</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>file:  Union[str,<br>PurePath],<br>device:  Optional[int]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Deserialize the FaissIndex from disk"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:__init__' href='parser/test3/search.py#L348'>IndexableMixin:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:__len__' href='parser/test3/search.py#L351'>IndexableMixin:__len__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:__getitem__' href='parser/test3/search.py#L354'>IndexableMixin:__getitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>key,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:is_index_initialized' href='parser/test3/search.py#L357'>IndexableMixin:is_index_initialized</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:_check_index_is_initialized' href='parser/test3/search.py#L360'>IndexableMixin:_check_index_is_initialized</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:list_indexes' href='parser/test3/search.py#L366'>IndexableMixin:list_indexes</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """List the colindex_nameumns/identifiers of all the attached indexes."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:get_index' href='parser/test3/search.py#L370'>IndexableMixin:get_index</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br></ul>
        <li>Docs:<br>        """List the index_name/identifiers of all the attached indexes.
<br>

<br>
        Args:
<br>
            index_name (:obj:`str`): Index name.
<br>

<br>
        Returns:
<br>
            :class:`BaseIndex`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:add_faiss_index' href='parser/test3/search.py#L382'>IndexableMixin:add_faiss_index</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br>index_name:  Optional[str]  =  None,<br>device:  Optional[int]  =  None,<br>string_factory:  Optional[str]  =  None,<br>metric_type:  Optional[int]  =  None,<br>custom_index:  Optional["faiss.Index"]  =  None,<br>train_size:  Optional[int]  =  None,<br>faiss_verbose:  bool  =  False,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:add_faiss_index_from_external_arrays' href='parser/test3/search.py#L417'>IndexableMixin:add_faiss_index_from_external_arrays</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>external_arrays:  np.array,<br>index_name:  str,<br>device:  Optional[int]  =  None,<br>string_factory:  Optional[str]  =  None,<br>metric_type:  Optional[int]  =  None,<br>custom_index:  Optional["faiss.Index"]  =  None,<br>train_size:  Optional[int]  =  None,<br>faiss_verbose:  bool  =  False,<br>,<br></ul>
        <li>Docs:<br>        """Add a dense index using Faiss for fast retrieval.
<br>
        The index is created using the vectors of `external_arrays`.
<br>
        You can specify `device` if you want to run it on GPU (`device` must be the GPU index).
<br>
        You can find more information about Faiss here:
<br>
        - For `string factory`: https://github.com/facebookresearch/faiss/wiki/The-index-factory
<br>

<br>
        Args:
<br>
            external_arrays (:obj:`np.array`): If you want to use arrays from outside the lib for the index, you can set `external_arrays`.
<br>
                It will use `external_arrays` to create the Faiss index instead of the arrays in the given `column`.
<br>
            index_name (:obj:`str`): The index_name/identifier of the index. This is the index_name that is used to call `.get_nearest` or `.search`.
<br>
            device (Optional :obj:`int`): If not None, this is the index of the GPU to use. By default it uses the CPU.
<br>
            string_factory (Optional :obj:`str`): This is passed to the index factory of Faiss to create the index. Default index class is IndexFlatIP.
<br>
            metric_type (Optional :obj:`int`): Type of metric. Ex: faiss.faiss.METRIC_INNER_PRODUCT or faiss.METRIC_L2.
<br>
            custom_index (Optional :obj:`faiss.Index`): Custom Faiss index that you already have instantiated and configured for your needs.
<br>
            train_size (Optional :obj:`int`): If the index needs a training step, specifies how many vectors will be used to train the index.
<br>
            faiss_verbose (:obj:`bool`, defaults to False): Enable the verbosity of the Faiss index.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:save_faiss_index' href='parser/test3/search.py#L451'>IndexableMixin:save_faiss_index</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br>file:  Union[str,<br>PurePath],<br></ul>
        <li>Docs:<br>        """Save a FaissIndex on disk.
<br>

<br>
        Args:
<br>
            index_name (:obj:`str`): The index_name/identifier of the index. This is the index_name that is used to call `.get_nearest` or `.search`.
<br>
            file (:obj:`str`): The path to the serialized faiss index on disk.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:load_faiss_index' href='parser/test3/search.py#L464'>IndexableMixin:load_faiss_index</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br>file:  Union[str,<br>PurePath],<br>device:  Optional[int]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Load a FaissIndex from disk.
<br>

<br>
        If you want to do additional configurations, you can have access to the faiss index object by doing
<br>
        `.get_index(index_name).faiss_index` to make it fit your needs.
<br>

<br>
        Args:
<br>
            index_name (:obj:`str`): The index_name/identifier of the index. This is the index_name that is used to
<br>
                call `.get_nearest` or `.search`.
<br>
            file (:obj:`str`): The path to the serialized faiss index on disk.
<br>
            device (Optional :obj:`int`): If not None, this is the index of the GPU to use. By default it uses the CPU.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:add_elasticsearch_index' href='parser/test3/search.py#L490'>IndexableMixin:add_elasticsearch_index</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br>index_name:  Optional[str]  =  None,<br>host:  Optional[str]  =  None,<br>port:  Optional[int]  =  None,<br>es_client:  Optional["Elasticsearch"]  =  None,<br>es_index_name:  Optional[str]  =  None,<br>es_index_config:  Optional[dict]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Add a text index using ElasticSearch for fast retrieval.
<br>

<br>
        Args:
<br>
            column (:obj:`str`): The column of the documents to add to the index.
<br>
            index_name (Optional :obj:`str`): The index_name/identifier of the index. This is the index name that is used to call `.get_nearest` or `.search`.
<br>
                By defaul it corresponds to `column`.
<br>
            host (Optional :obj:`str`, defaults to localhost):
<br>
                host of where ElasticSearch is running
<br>
            port (Optional :obj:`str`, defaults to 9200):
<br>
                port of where ElasticSearch is running
<br>
            es_client (Optional :obj:`elasticsearch.Elasticsearch`):
<br>
                The elasticsearch client used to create the index if host and port are None.
<br>
            es_index_name (Optional :obj:`str`): The elasticsearch index name used to create the index.
<br>
            es_index_config (Optional :obj:`dict`):
<br>
                The configuration of the elasticsearch index.
<br>
                Default config is:
<br>

<br>
        Config::
<br>

<br>
            {
<br>
                "settings": {
<br>
                    "number_of_shards": 1,
<br>
                    "analysis": {"analyzer": {"stop_standard": {"type": "standard", " stopwords": "_english_"}}},
<br>
                },
<br>
                "mappings": {
<br>
                    "properties": {
<br>
                        "text": {
<br>
                            "type": "text",
<br>
                            "analyzer": "standard",
<br>
                            "similarity": "BM25"
<br>
                        },
<br>
                    }
<br>
                },
<br>
            }
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:load_elasticsearch_index' href='parser/test3/search.py#L542'>IndexableMixin:load_elasticsearch_index</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br>es_index_name:  str,<br>host:  Optional[str]  =  None,<br>port:  Optional[int]  =  None,<br>es_client:  Optional["Elasticsearch"]  =  None,<br>es_index_config:  Optional[dict]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Load an existing text index using ElasticSearch for fast retrieval.
<br>

<br>
        Args:
<br>
            index_name (:obj:`str`): The index_name/identifier of the index. This is the index name that is used to call `.get_nearest` or `.search`.
<br>
            es_index_name (:obj:`str`): The name of elasticsearch index to load.
<br>
            host (Optional :obj:`str`, defaults to localhost):
<br>
                host of where ElasticSearch is running
<br>
            port (Optional :obj:`str`, defaults to 9200):
<br>
                port of where ElasticSearch is running
<br>
            es_client (Optional :obj:`elasticsearch.Elasticsearch`):
<br>
                The elasticsearch client used to create the index if host and port are None.
<br>
            es_index_config (Optional :obj:`dict`):
<br>
                The configuration of the elasticsearch index.
<br>
                Default config is::
<br>

<br>
                    {
<br>
                        "settings": {
<br>
                            "number_of_shards": 1,
<br>
                            "analysis": {"analyzer": {"stop_standard": {"type": "standard", " stopwords": "_english_"}}},
<br>
                        },
<br>
                        "mappings": {
<br>
                            "properties": {
<br>
                                "text": {
<br>
                                    "type": "text",
<br>
                                    "analyzer": "standard",
<br>
                                    "similarity": "BM25"
<br>
                                },
<br>
                            }
<br>
                        },
<br>
                    }
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:drop_index' href='parser/test3/search.py#L586'>IndexableMixin:drop_index</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br></ul>
        <li>Docs:<br>        """Drop the index with the specified column.
<br>

<br>
        Args:
<br>
            index_name (:obj:`str`): The index_name/identifier of the index.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:search' href='parser/test3/search.py#L594'>IndexableMixin:search</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br>query:  Union[str,<br>np.array],<br>k:  int  =  10,<br></ul>
        <li>Docs:<br>        """Find the nearest examples indices in the dataset to the query.
<br>

<br>
        Args:
<br>
            index_name (:obj:`str`): The name/identifier of the index.
<br>
            query (:obj:`Union[str, np.ndarray]`): The query as a string if `index_name` is a text index or as a numpy array if `index_name` is a vector index.
<br>
            k (:obj:`int`): The number of examples to retrieve.
<br>

<br>
        Returns:
<br>
            scores (:obj:`List[List[float]`): The retrieval scores of the retrieved examples.
<br>
            indices (:obj:`List[List[int]]`): The indices of the retrieved examples.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:search_batch' href='parser/test3/search.py#L609'>IndexableMixin:search_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br>queries:  Union[List[str],<br>np.array],<br>k:  int  =  10,<br></ul>
        <li>Docs:<br>        """Find the nearest examples indices in the dataset to the query.
<br>

<br>
        Args:
<br>
            index_name (:obj:`str`): The index_name/identifier of the index.
<br>
            queries (:obj:`Union[List[str], np.ndarray]`): The queries as a list of strings if `index_name` is a text index or as a numpy array if `index_name` is a vector index.
<br>
            k (:obj:`int`): The number of examples to retrieve per query.
<br>

<br>
        Returns:
<br>
            total_scores (:obj:`List[List[float]`): The retrieval scores of the retrieved examples per query.
<br>
            total_indices (:obj:`List[List[int]]`): The indices of the retrieved examples per query.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:get_nearest_examples' href='parser/test3/search.py#L624'>IndexableMixin:get_nearest_examples</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br>query:  Union[str,<br>np.array],<br>k:  int  =  10,<br></ul>
        <li>Docs:<br>        """Find the nearest examples in the dataset to the query.
<br>

<br>
        Args:
<br>
            index_name (:obj:`str`): The index_name/identifier of the index.
<br>
            query (:obj:`Union[str, np.ndarray]`): The query as a string if `index_name` is a text index or as a numpy array if `index_name` is a vector index.
<br>
            k (:obj:`int`): The number of examples to retrieve.
<br>

<br>
        Returns:
<br>
            scores (:obj:`List[float]`): The retrieval scores of the retrieved examples.
<br>
            examples (:obj:`dict`): The retrieved examples.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/search.py:IndexableMixin:get_nearest_examples_batch' href='parser/test3/search.py#L642'>IndexableMixin:get_nearest_examples_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>index_name:  str,<br>queries:  Union[List[str],<br>np.array],<br>k:  int  =  10,<br></ul>
        <li>Docs:<br>        """Find the nearest examples in the dataset to the query.
<br>

<br>
        Args:
<br>
            index_name (:obj:`str`): The index_name/identifier of the index.
<br>
            queries (:obj:`Union[List[str], np.ndarray]`): The queries as a list of strings if `index_name` is a text index or as a numpy array if `index_name` is a vector index.
<br>
            k (:obj:`int`): The number of examples to retrieve per query.
<br>

<br>
        Returns:
<br>
            total_scores (`List[List[float]`): The retrieval scores of the retrieved examples per query.
<br>
            total_examples (`List[dict]`): The retrieved examples per query.
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/io/json.py' href='parser/test3/io/json.py'>parser/test3/io/json.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/io/json.py:JsonDatasetReader' href='parser/test3/io/json.py#L12'>JsonDatasetReader</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/io/json.py:JsonDatasetWriter' href='parser/test3/io/json.py#L60'>JsonDatasetWriter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/json.py:JsonDatasetReader:__init__' href='parser/test3/io/json.py#L13'>JsonDatasetReader:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_paths:  NestedDataStructureLike[PathLike],<br>split:  Optional[NamedSplit]  =  None,<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>field:  Optional[str]  =  None,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/json.py:JsonDatasetReader:read' href='parser/test3/io/json.py#L36'>JsonDatasetReader:read</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/json.py:JsonDatasetWriter:__init__' href='parser/test3/io/json.py#L13'>JsonDatasetWriter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset:  Dataset,<br>path_or_buf:  Union[PathLike,<br>BinaryIO],<br>batch_size:  Optional[int]  =  None,<br>**to_json_kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/json.py:JsonDatasetWriter:write' href='parser/test3/io/json.py#L73'>JsonDatasetWriter:write</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/json.py:JsonDatasetWriter:_write' href='parser/test3/io/json.py#L83'>JsonDatasetWriter:_write</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>file_obj:  BinaryIO,<br>batch_size:  int,<br>encoding:  str  =  "utf-8",<br>orient = "records",<br>lines = True,<br>**to_json_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Writes the pyarrow table as JSON lines to a binary file handle.
<br>

<br>
        Caller is responsible for opening and closing the handle.
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/commands/test.py' href='parser/test3/commands/test.py'>parser/test3/commands/test.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/commands/test.py:test_command_factory' href='parser/test3/commands/test.py#L19'>test_command_factory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>args,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/commands/test.py:TestCommand' href='parser/test3/commands/test.py#L35'>TestCommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/test.py:TestCommand:register_subcommand' href='parser/test3/commands/test.py#L37'>TestCommand:register_subcommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>parser:  ArgumentParser,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/test.py:TestCommand:__init__' href='parser/test3/commands/test.py#L78'>TestCommand:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset:  str,<br>name:  str,<br>cache_dir:  str,<br>data_dir:  str,<br>all_configs:  bool,<br>save_infos:  bool,<br>ignore_verifications:  bool,<br>force_redownload:  bool,<br>clear_cache:  bool,<br>proc_rank:  int,<br>num_proc:  int,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/test.py:TestCommand:run' href='parser/test3/commands/test.py#L111'>TestCommand:run</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/tasks/base.py' href='parser/test3/tasks/base.py'>parser/test3/tasks/base.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/tasks/base.py:TaskTemplate' href='parser/test3/tasks/base.py#L13'>TaskTemplate</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/tasks/base.py:TaskTemplate:features' href='parser/test3/tasks/base.py#L20'>TaskTemplate:features</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/tasks/base.py:TaskTemplate:column_mapping' href='parser/test3/tasks/base.py#L25'>TaskTemplate:column_mapping</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/tasks/base.py:TaskTemplate:from_dict' href='parser/test3/tasks/base.py#L29'>TaskTemplate:from_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls:  Type[T],<br>template_dict:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test2/model_gefs.py' href='parser/test2/model_gefs.py'>parser/test2/model_gefs.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:log' href='parser/test2/model_gefs.py#L12'>log</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*s,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:log2' href='parser/test2/model_gefs.py#L15'>log2</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*s,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:log3' href='parser/test2/model_gefs.py#L18'>log3</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*s,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:init' href='parser/test2/model_gefs.py#L23'>init</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*kw,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:reset' href='parser/test2/model_gefs.py#L28'>reset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:fit' href='parser/test2/model_gefs.py#L73'>fit</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data_pars = None,<br>compute_pars = None,<br>out_pars = None,<br>**kw,<br></ul>
        <li>Docs:<br>    """
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:eval' href='parser/test2/model_gefs.py#L118'>eval</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data_pars = None,<br>compute_pars = None,<br>out_pars = None,<br>**kw,<br></ul>
        <li>Docs:<br>    """
<br>
       Return metrics of the model when fitted.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:predict' href='parser/test2/model_gefs.py#L138'>predict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>Xpred = None,<br>data_pars = {},<br>compute_pars = {},<br>out_pars = {},<br>**kw,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:save' href='parser/test2/model_gefs.py#L162'>save</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path = None,<br>info = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:load_model' href='parser/test2/model_gefs.py#L174'>load_model</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path = "",<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:load_info' href='parser/test2/model_gefs.py#L187'>load_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path = "",<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:get_dataset' href='parser/test2/model_gefs.py#L198'>get_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data_pars = None,<br>task_type = "train",<br>**kw,<br></ul>
        <li>Docs:<br>    """
<br>
      "ram"  :
<br>
      "file" :
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:test' href='parser/test2/model_gefs.py#L228'>test</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>n_sample  =  100,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:test_helper' href='parser/test2/model_gefs.py#L335'>test_helper</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>model_pars,<br>data_pars,<br>compute_pars,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:pd_colcat_get_catcount' href='parser/test2/model_gefs.py#L373'>pd_colcat_get_catcount</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>df,<br>colcat,<br>coly,<br>continuous_ids = None,<br></ul>
        <li>Docs:<br>    """  Learns the number of categories in each variable and standardizes the df.
<br>
        ncat: numpy m The number of categories of each variable. One if the variable is continuous.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:is_continuous' href='parser/test2/model_gefs.py#L391'>is_continuous</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>v_array,<br></ul>
        <li>Docs:<br>    """ Returns true if df was sampled from a continuous variables, and false
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:test2' href='parser/test2/model_gefs.py#L404'>test2</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:get_dummies' href='parser/test2/model_gefs.py#L446'>get_dummies</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:learncats' href='parser/test2/model_gefs.py#L456'>learncats</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br>classcol = None,<br>continuous_ids = [],<br></ul>
        <li>Docs:<br>    """
<br>
        Learns the number of categories in each variable and standardizes the data.
<br>
        ----------
<br>
        data: numpy n x m
<br>
            Numpy array comprising n realisations (instances) of m variables.
<br>
        classcol: int  The column index of the class variables (if any).
<br>
        continuous_ids: list of ints
<br>
            List containing the indices of known continuous variables. Useful for
<br>
            discrete data like age, which is better modeled as continuous.
<br>
        Returns
<br>
        -------
<br>
        ncat: numpy m  The number of categories of each variable. One if the variable is  continuous.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:gef_is_continuous' href='parser/test2/model_gefs.py#L482'>gef_is_continuous</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br>    """
<br>
        Returns true if data was sampled from a continuous variables, and false
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:gef_get_stats' href='parser/test2/model_gefs.py#L497'>gef_get_stats</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br>ncat = None,<br></ul>
        <li>Docs:<br>    """
<br>
        Compute univariate statistics for continuous variables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:gef_normalize_data' href='parser/test2/model_gefs.py#L527'>gef_normalize_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br>maxv,<br>minv,<br></ul>
        <li>Docs:<br>    """
<br>
        Normalizes the data given the maximum and minimum values of each variable.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:gef_standardize_data' href='parser/test2/model_gefs.py#L538'>gef_standardize_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br>mean,<br>std,<br></ul>
        <li>Docs:<br>    """
<br>
        Standardizes the data given the mean and standard deviations values of
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:train_test_split2' href='parser/test2/model_gefs.py#L554'>train_test_split2</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br>ncat,<br>train_ratio = 0.7,<br>prep = 'std',<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:test_converion' href='parser/test2/model_gefs.py#L587'>test_converion</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """
<br>
    General comments on the API¶
<br>
    There are four different functions to do classification with GeFs.
<br>

<br>
    classify
<br>
    classify_avg
<br>
    classify_lspn
<br>
    classify_avg_lspn
<br>
    The first two, classify and classify_avg, exploit class factorised leaves to run inference faster
<br>
    (propagate the probabilities of all classes at once). That, of course, only works if the leaves
<br>
    are class factorised (e.g. learnsp=np.Inf). Otherwise, one should use classify_lspn and classify_avg_lspn which work
<br>
     with any PC (in particular those with a LearnSPN network at the leaves, hence the name).
<br>

<br>
    The other important distinction is that avg methods assume a model learned as an ensemble and performs inference by 'averaging' the distribution of each of the base models. These are the methods that match the original Random Forest in terms of classification (with complete data, and class factorised leaves). In contrast, the other methods run inference as if the model is a single PC. One can interpret that as giving different weights to each of the base models according to the likelihood of the instance to be classified (base models under which the instance is more likely are given higher weights).
<br>
    This inference method is referred to as GeF+ in the paper, as it defines a mixture over the base models.
<br>

<br>

<br>
    :return:
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:train_test_split' href='parser/test2/model_gefs.py#L636'>train_test_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br>ncat,<br>train_ratio = 0.7,<br>prep = 'std',<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:adult' href='parser/test2/model_gefs.py#L657'>adult</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:australia' href='parser/test2/model_gefs.py#L667'>australia</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:bank' href='parser/test2/model_gefs.py#L676'>bank</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:credit' href='parser/test2/model_gefs.py#L687'>credit</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:electricity' href='parser/test2/model_gefs.py#L698'>electricity</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:segment' href='parser/test2/model_gefs.py#L707'>segment</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:german' href='parser/test2/model_gefs.py#L718'>german</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:vowel' href='parser/test2/model_gefs.py#L726'>vowel</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:cmc' href='parser/test2/model_gefs.py#L733'>cmc</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_gefs.py:get_data' href='parser/test2/model_gefs.py#L742'>get_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data_pars = None,<br>task_type = "train",<br>**kw,<br></ul>
        <li>Docs:<br>"""
<br>
def test_dataset_classi_fake(nrows=500):
<br>
    from sklearn import datasets as sklearn_datasets
<br>
    ndim=11
<br>
    coly   = ['y']
<br>
    colnum = ["colnum_" +str(i) for i in range(0, ndim) ]
<br>
    colcat = ['colcat_1']
<br>
    X, y    = sklearn_datasets.make_classification(
<br>
        n_samples=1000,
<br>
        n_features=ndim,
<br>
        # No n_targets param for make_classification
<br>
        # n_targets=1,
<br>
        # Fake dataset, classification on 2 classes
<br>
        n_classes=2,
<br>
        # In classification, n_informative should be less than n_features
<br>
        n_informative=ndim - 2
<br>
    )
<br>
    df         = pd.DataFrame(X,  columns= colnum)
<br>
    df[coly]   = y.reshape(-1, 1)
<br>
    for ci in colcat :
<br>
      df[colcat] = np.random.randint(2, len(df))
<br>
    return df, colnum, colcat, coly
<br>
"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test2/model_gefs.py:Model' href='parser/test2/model_gefs.py#L51'>Model</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test2/model_gefs.py:Model:__init__' href='parser/test2/model_gefs.py#L52'>Model:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>model_pars = None,<br>data_pars = None,<br>compute_pars = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test2/model_sklearn.py' href='parser/test2/model_sklearn.py'>parser/test2/model_sklearn.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:log' href='parser/test2/model_sklearn.py#L12'>log</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*s,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:log2' href='parser/test2/model_sklearn.py#L15'>log2</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*s,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:log3' href='parser/test2/model_sklearn.py#L18'>log3</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*s,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:init' href='parser/test2/model_sklearn.py#L23'>init</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*kw,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:reset' href='parser/test2/model_sklearn.py#L28'>reset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:model_automl' href='parser/test2/model_sklearn.py#L43'>model_automl</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:fit' href='parser/test2/model_sklearn.py#L71'>fit</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data_pars = None,<br>compute_pars = None,<br>out_pars = None,<br>**kw,<br></ul>
        <li>Docs:<br>    """
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:predict' href='parser/test2/model_sklearn.py#L85'>predict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>Xpred = None,<br>data_pars = {},<br>compute_pars = {},<br>out_pars = {},<br>**kw,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:save' href='parser/test2/model_sklearn.py#L106'>save</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path = None,<br>info = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:load_model' href='parser/test2/model_sklearn.py#L118'>load_model</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path = "",<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:load_info' href='parser/test2/model_sklearn.py#L131'>load_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path = "",<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:get_dataset_split_for_model_pandastuple' href='parser/test2/model_sklearn.py#L143'>get_dataset_split_for_model_pandastuple</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>Xtrain,<br>ytrain = None,<br>data_pars = None,<br>,<br></ul>
        <li>Docs:<br>    """  Split data for moel input/
<br>
    Xtrain  ---> Split INTO  tuple of data  Xtuple= (df1, df2, df3) to fit model input.
<br>
    :param Xtrain:
<br>
    :param coldataloader_received:
<br>
    :param colmodel_ref:
<br>
    :return:
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:get_dataset2' href='parser/test2/model_sklearn.py#L174'>get_dataset2</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data_pars = None,<br>task_type = "train",<br>**kw,<br></ul>
        <li>Docs:<br>    """
<br>
       Raw Data (Path)   --->  Input Object (ie Pandas, ...) for Model training
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:get_dataset' href='parser/test2/model_sklearn.py#L199'>get_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>Xtrain,<br>ytrain = None,<br>data_pars = None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:get_params_sklearn' href='parser/test2/model_sklearn.py#L227'>get_params_sklearn</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>deep = False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:get_params' href='parser/test2/model_sklearn.py#L231'>get_params</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>deep = False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:test' href='parser/test2/model_sklearn.py#L251'>test</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>n_sample           =  1000,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:zz_eval' href='parser/test2/model_sklearn.py#L382'>zz_eval</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>data_pars = None,<br>compute_pars = None,<br>out_pars = None,<br>**kw,<br></ul>
        <li>Docs:<br>    """
<br>
       Return metrics of the model when fitted.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test2/model_sklearn.py:zz_preprocess' href='parser/test2/model_sklearn.py#L406'>zz_preprocess</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>prepro_pars,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test2/model_sklearn.py:Model' href='parser/test2/model_sklearn.py#L54'>Model</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test2/model_sklearn.py:Model:__init__' href='parser/test2/model_sklearn.py#L55'>Model:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>model_pars = None,<br>data_pars = None,<br>compute_pars = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/keyhash.py' href='parser/test3/keyhash.py'>parser/test3/keyhash.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/keyhash.py:_as_bytes' href='parser/test3/keyhash.py#L38'>_as_bytes</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>hash_data:  Union[str,<br>int,<br>bytes],<br></ul>
        <li>Docs:<br>    """
<br>
    Returns the input hash_data in its bytes form
<br>

<br>
    Args:
<br>
    hash_data: the hash salt/key to be converted to bytes
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/keyhash.py:InvalidKeyError' href='parser/test3/keyhash.py#L61'>InvalidKeyError</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/keyhash.py:DuplicatedKeysError' href='parser/test3/keyhash.py#L71'>DuplicatedKeysError</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/keyhash.py:KeyHasher' href='parser/test3/keyhash.py#L81'>KeyHasher</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/keyhash.py:InvalidKeyError:__init__' href='parser/test3/keyhash.py#L64'>InvalidKeyError:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>hash_data,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/keyhash.py:DuplicatedKeysError:__init__' href='parser/test3/keyhash.py#L74'>DuplicatedKeysError:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>key,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/keyhash.py:KeyHasher:__init__' href='parser/test3/keyhash.py#L84'>KeyHasher:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>hash_salt:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/keyhash.py:KeyHasher:hash' href='parser/test3/keyhash.py#L87'>KeyHasher:hash</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>key:  Union[str,<br>int,<br>bytes],<br></ul>
        <li>Docs:<br>        """Returns 128-bits unique hash of input key
<br>

<br>
        Args:
<br>
        key: the input key to be hashed (should be str, int or bytes)
<br>

<br>
        Returns: 128-bit int hash key"""
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/naming.py' href='parser/test3/naming.py'>parser/test3/naming.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/naming.py:camelcase_to_snakecase' href='parser/test3/naming.py#L33'>camelcase_to_snakecase</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>name,<br></ul>
        <li>Docs:<br>    """Convert camel-case string to snake-case."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/naming.py:snakecase_to_camelcase' href='parser/test3/naming.py#L40'>snakecase_to_camelcase</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>name,<br></ul>
        <li>Docs:<br>    """Convert snake-case string to camel-case string."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/naming.py:filename_prefix_for_name' href='parser/test3/naming.py#L47'>filename_prefix_for_name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>name,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/naming.py:filename_prefix_for_split' href='parser/test3/naming.py#L53'>filename_prefix_for_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>name,<br>split,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/naming.py:filepattern_for_dataset_split' href='parser/test3/naming.py#L61'>filepattern_for_dataset_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset_name,<br>split,<br>data_dir,<br>filetype_suffix = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/naming.py:filename_for_dataset_split' href='parser/test3/naming.py#L69'>filename_for_dataset_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset_name,<br>split,<br>filetype_suffix = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/naming.py:filepath_for_dataset_split' href='parser/test3/naming.py#L76'>filepath_for_dataset_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset_name,<br>split,<br>data_dir,<br>filetype_suffix = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/download_manager.py' href='parser/test3/utils/download_manager.py'>parser/test3/utils/download_manager.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/utils/download_manager.py:GenerateMode' href='parser/test3/utils/download_manager.py#L42'>GenerateMode</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/download_manager.py:DownloadManager' href='parser/test3/utils/download_manager.py#L66'>DownloadManager</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:__init__' href='parser/test3/utils/download_manager.py#L67'>DownloadManager:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_name:  Optional[str]  =  None,<br>data_dir:  Optional[str]  =  None,<br>download_config:  Optional[DownloadConfig]  =  None,<br>base_path:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Download manager constructor.
<br>

<br>
        Args:
<br>
            data_dir: can be used to specify a manual directory to get the files from.
<br>
            dataset_name: `str`, name of dataset this instance will be used for. If
<br>
                provided, downloads will contain which datasets they were used for.
<br>
            download_config: `DownloadConfig` to specify the cache directory and other
<br>
                download options
<br>
            base_path: `str`, base path that is used when relative paths are used to
<br>
                download files. This can be a remote url.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:manual_dir' href='parser/test3/utils/download_manager.py#L95'>DownloadManager:manual_dir</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:downloaded_size' href='parser/test3/utils/download_manager.py#L99'>DownloadManager:downloaded_size</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Returns the total size of downloaded files."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:ship_files_with_pipeline' href='parser/test3/utils/download_manager.py#L103'>DownloadManager:ship_files_with_pipeline</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>downloaded_path_or_paths,<br>pipeline,<br></ul>
        <li>Docs:<br>        """
<br>
        Ship the files using Beam FileSystems to the pipeline temp dir.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:_record_sizes_checksums' href='parser/test3/utils/download_manager.py#L131'>DownloadManager:_record_sizes_checksums</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>url_or_urls:  NestedDataStructure,<br>downloaded_path_or_paths:  NestedDataStructure,<br></ul>
        <li>Docs:<br>        """Record size/checksum of downloaded files."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:download_custom' href='parser/test3/utils/download_manager.py#L137'>DownloadManager:download_custom</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>url_or_urls,<br>custom_download,<br></ul>
        <li>Docs:<br>        """
<br>
        Download given urls(s) by calling `custom_download`.
<br>

<br>
        Args:
<br>
            url_or_urls: url or `list`/`dict` of urls to download and extract. Each
<br>
                url is a `str`.
<br>
            custom_download: Callable with signature (src_url: str, dst_path: str) -> Any
<br>
                as for example `tf.io.gfile.copy`, that lets you download from google storage
<br>

<br>
        Returns:
<br>
            downloaded_path(s): `str`, The downloaded paths matching the given input
<br>
                url_or_urls.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:download' href='parser/test3/utils/download_manager.py#L176'>DownloadManager:download</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Download given url(s).
<br>

<br>
        Args:
<br>
            url_or_urls: url or `list`/`dict` of urls to download and extract. Each
<br>
                url is a `str`.
<br>

<br>
        Returns:
<br>
            downloaded_path(s): `str`, The downloaded paths matching the given input
<br>
                url_or_urls.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:_download' href='parser/test3/utils/download_manager.py#L216'>DownloadManager:_download</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>url_or_filename:  str,<br>download_config:  DownloadConfig,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:iter_archive' href='parser/test3/utils/download_manager.py#L222'>DownloadManager:iter_archive</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path,<br></ul>
        <li>Docs:<br>        """Returns iterator over files within archive.
<br>

<br>
        Args:
<br>
            path: path to archive.
<br>

<br>
        Returns:
<br>
            Generator yielding tuple (path_within_archive, file_obj).
<br>
            File-Obj are opened in byte mode (io.BufferedReader)
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:extract' href='parser/test3/utils/download_manager.py#L247'>DownloadManager:extract</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_paths,<br>num_proc = None,<br></ul>
        <li>Docs:<br>        """Extract given path(s).
<br>

<br>
        Args:
<br>
            path_or_paths: path or `list`/`dict` of path of file to extract. Each
<br>
                path is a `str`.
<br>
            num_proc: Use multi-processing if `num_proc` > 1 and the length of
<br>
                `path_or_paths` is larger than `num_proc`
<br>

<br>
        Returns:
<br>
            extracted_path(s): `str`, The extracted paths matching the given input
<br>
                path_or_paths.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:download_and_extract' href='parser/test3/utils/download_manager.py#L273'>DownloadManager:download_and_extract</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>url_or_urls,<br></ul>
        <li>Docs:<br>        """Download and extract given url_or_urls.
<br>

<br>
        Is roughly equivalent to:
<br>

<br>
        ```
<br>
        extracted_paths = dl_manager.extract(dl_manager.download(url_or_urls))
<br>
        ```
<br>

<br>
        Args:
<br>
            url_or_urls: url or `list`/`dict` of urls to download and extract. Each
<br>
                url is a `str`.
<br>

<br>
        Returns:
<br>
            extracted_path(s): `str`, extracted paths of given URL(s).
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/download_manager.py:DownloadManager:get_recorded_sizes_checksums' href='parser/test3/utils/download_manager.py#L291'>DownloadManager:get_recorded_sizes_checksums</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/packaged_modules/parquet/parquet.py' href='parser/test3/packaged_modules/parquet/parquet.py'>parser/test3/packaged_modules/parquet/parquet.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/packaged_modules/parquet/parquet.py:ParquetConfig' href='parser/test3/packaged_modules/parquet/parquet.py#L17'>ParquetConfig</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/packaged_modules/parquet/parquet.py:Parquet' href='parser/test3/packaged_modules/parquet/parquet.py#L25'>Parquet</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/parquet/parquet.py:Parquet:_info' href='parser/test3/packaged_modules/parquet/parquet.py#L28'>Parquet:_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/parquet/parquet.py:Parquet:_split_generators' href='parser/test3/packaged_modules/parquet/parquet.py#L35'>Parquet:_split_generators</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager,<br></ul>
        <li>Docs:<br>        """We handle string, list and dicts in datafiles"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/parquet/parquet.py:Parquet:_generate_tables' href='parser/test3/packaged_modules/parquet/parquet.py#L52'>Parquet:_generate_tables</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>files,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/combine.py' href='parser/test3/combine.py'>parser/test3/combine.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/combine.py:interleave_datasets' href='parser/test3/combine.py#L20'>interleave_datasets</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>datasets:  List[DatasetType],<br>probabilities:  Optional[List[float]]  =  None,<br>seed:  Optional[int]  =  None,<br></ul>
        <li>Docs:<br>    """
<br>
    Interleave several datasets (sources) into a single dataset.
<br>
    The new dataset is constructed by alternating between the sources to get the examples.
<br>

<br>
    You can use this function on a list of :class:`Dataset` objects, or on a list of :class:`IterableDataset` objects.
<br>

<br>
    If ``probabilities`` is ``None`` (default) the new dataset is constructed by cycling between each source to get the examples.
<br>
    If ``probabilities`` is not ``None``, the new dataset is constructed by getting examples from a random source at a time according to the provided probabilities.
<br>

<br>
    The resulting dataset ends when one of the source datasets runs out of examples.
<br>

<br>
    Examples:
<br>

<br>
        For regular datasets (map-style):
<br>

<br>
        >>> from datasets import Dataset, interleave_datasets
<br>
        >>> d1 = Dataset.from_dict({"a": [0, 1, 2]})
<br>
        >>> d2 = Dataset.from_dict({"a": [10, 11, 12]})
<br>
        >>> d3 = Dataset.from_dict({"a": [20, 21, 22]})
<br>
        >>> dataset = interleave_datasets([d1, d2, d3])
<br>
        >>> dataset["a"]
<br>
        [0, 10, 20, 1, 11, 21, 2, 12, 22]
<br>
        >>> dataset = interleave_datasets([d1, d2, d3], probabilities=[0.7, 0.2, 0.1], seed=42)
<br>
        >>> dataset["a"]
<br>
        [10, 0, 11, 1, 2, 20, 12]
<br>

<br>
        For datasets in streaming mode (iterable):
<br>

<br>
        >>> from datasets import load_dataset, interleave_datasets
<br>
        >>> d1 = load_dataset("oscar", "unshuffled_deduplicated_en", split="train", streaming=True)
<br>
        >>> d2 = load_dataset("oscar", "unshuffled_deduplicated_fr", split="train", streaming=True)
<br>
        >>> dataset = interleave_datasets([d1, d2])
<br>
        >>> iterator = iter(dataset)
<br>
        >>> next(iterator)
<br>
        {'text': 'Mtendere Village was inspired by the vision...
<br>
        >>> next(iterator)
<br>
        {'text': "Média de débat d'idées, de culture...
<br>

<br>
    Args:
<br>
        datasets (:obj:`List[Dataset]` or :obj:`List[IterableDataset]`): list of datasets to interleave
<br>
        probabilities (:obj:`List[float]`, optional, default None): If specified, the new dataset is constructued by sampling
<br>
            examples from one source at a time according to these probabilities.
<br>
        seed (:obj:`int`, optional, default None): The random seed used to choose a source for each example.
<br>
        **kwargs: For map-style datasets:
<br>
            Keyword arguments to be passed to :meth:`datasets.Datasets.select` when selecting the indices used to interleave the datasets.
<br>

<br>
    Output:
<br>
        :class:`datasets.Dataset` if the input is a list of :class:`datasets.Dataset`
<br>
        or :class:`datasets.IterableDataset` if the input is a list of :class:`datasets.IterableDataset`
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/combine.py:_interleave_map_style_datasets' href='parser/test3/combine.py#L95'>_interleave_map_style_datasets</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>datasets:  List["Dataset"],<br>probabilities:  Optional[List[float]]  =  None,<br>seed:  Optional[int]  =  None,<br>info:  Optional[Any]  =  None,<br>split:  Optional[Any]  =  None,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>    """
<br>
    Interleave several map-style datasets (sources) into a single map-style dataset.
<br>
    The new dataset is constructed by alternating between the sources to get the examples.
<br>
    If `probabilities = None` (default) the new dataset is constructed by cycling between each source to get the examples.
<br>
    If `probabilities` is not `None, the new dataset is constructed by getting examples from a random source at a time according to the provided probabilities.
<br>

<br>
    Args:
<br>
        datasets (:obj:`List[Dataset]`): list of datasets to interleave
<br>
        probabilities (:obj:`List[float]`, optional, default None): If specified, the new dataset is constructued by sampling
<br>
            examples from one source at a time according to these probabilities.
<br>
        seed (:obj:`int`, optional, default None): The random seed used to choose a source for each example.
<br>
        **kwargs: Keyword arguments to be passed to :meth:`datasets.Datasets.select` when selecting the indices used to interleave the datasets.
<br>

<br>
    Output:
<br>
        :class:`datasets.Dataset`
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/combine.py:_interleave_iterable_datasets' href='parser/test3/combine.py#L161'>_interleave_iterable_datasets</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>datasets:  List["IterableDataset"],<br>probabilities:  Optional[List[float]]  =  None,<br>seed:  Optional[int]  =  None,<br>info:  Optional[Any]  =  None,<br>split:  Optional[Any]  =  None,<br>,<br></ul>
        <li>Docs:<br>    """
<br>
    Interleave several iterable datasets (sources) into a single iterable dataset.
<br>
    The new iterable dataset alternates between the sources to yield examples.
<br>
    If `probabilities = None` (default) the iterable dataset will cycles through the sources in order for each next example in the iteration.
<br>
    If `probabilities` is not `None, the iterable dataset will sample a random source according to the provided probabilities for each next examples in the iteration.
<br>

<br>
    Args:
<br>
        datasets (:obj:`List[IterableDataset]`): list of datasets to interleave
<br>
        probabilities (:obj:`List[float]`, optional, default None): If specified, the new iterable dataset samples
<br>
            examples from one source at a time according to these probabilities.
<br>
        seed (:obj:`int`, optional, default None): The random seed used to choose a source for each example.
<br>

<br>
    Output:
<br>
        :class:`datasets.IterableDataset`
<br>
    """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/filelock.py' href='parser/test3/utils/filelock.py'>parser/test3/utils/filelock.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/filelock.py:logger' href='parser/test3/utils/filelock.py#L80'>logger</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Returns the logger instance used in this module."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/filelock.py:Timeout' href='parser/test3/utils/filelock.py#L89'>Timeout</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/filelock.py:_Acquire_ReturnProxy' href='parser/test3/utils/filelock.py#L117'>_Acquire_ReturnProxy</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/filelock.py:BaseFileLock' href='parser/test3/utils/filelock.py#L130'>BaseFileLock</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/filelock.py:WindowsFileLock' href='parser/test3/utils/filelock.py#L349'>WindowsFileLock</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/filelock.py:UnixFileLock' href='parser/test3/utils/filelock.py#L392'>UnixFileLock</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/filelock.py:SoftFileLock' href='parser/test3/utils/filelock.py#L425'>SoftFileLock</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:Timeout:__init__' href='parser/test3/utils/filelock.py#L95'>Timeout:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>lock_file,<br></ul>
        <li>Docs:<br>        """ """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:Timeout:__str__' href='parser/test3/utils/filelock.py#L101'>Timeout:__str__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:_Acquire_ReturnProxy:__init__' href='parser/test3/utils/filelock.py#L118'>_Acquire_ReturnProxy:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>lock,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:_Acquire_ReturnProxy:__enter__' href='parser/test3/utils/filelock.py#L122'>_Acquire_ReturnProxy:__enter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:_Acquire_ReturnProxy:__exit__' href='parser/test3/utils/filelock.py#L125'>_Acquire_ReturnProxy:__exit__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>exc_type,<br>exc_value,<br>traceback,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:__init__' href='parser/test3/utils/filelock.py#L135'>BaseFileLock:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>lock_file,<br>timeout = -1,<br>max_filename_length = 255,<br></ul>
        <li>Docs:<br>        """ """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:lock_file' href='parser/test3/utils/filelock.py#L161'>BaseFileLock:lock_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        The path to the lock file.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:timeout' href='parser/test3/utils/filelock.py#L168'>BaseFileLock:timeout</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        You can set a default timeout for the filelock. It will be used as
<br>
        fallback value in the acquire method, if no timeout value (*None*) is
<br>
        given.
<br>

<br>
        If you want to disable the timeout, set it to a negative value.
<br>

<br>
        A timeout of 0 means, that there is exactly one attempt to acquire the
<br>
        file lock.
<br>

<br>
        .. versionadded:: 2.0.0
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:timeout' href='parser/test3/utils/filelock.py#L184'>BaseFileLock:timeout</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """ """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:_acquire' href='parser/test3/utils/filelock.py#L192'>BaseFileLock:_acquire</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Platform dependent. If the file lock could be
<br>
        acquired, self._lock_file_fd holds the file descriptor
<br>
        of the lock file.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:_release' href='parser/test3/utils/filelock.py#L200'>BaseFileLock:_release</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Releases the lock and sets self._lock_file_fd to None.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:is_locked' href='parser/test3/utils/filelock.py#L210'>BaseFileLock:is_locked</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        True, if the object holds the file lock.
<br>

<br>
        .. versionchanged:: 2.0.0
<br>

<br>
            This was previously a method and is now a property.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:acquire' href='parser/test3/utils/filelock.py#L220'>BaseFileLock:acquire</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>timeout = None,<br>poll_intervall = 0.05,<br></ul>
        <li>Docs:<br>        """
<br>
        Acquires the file lock or fails with a :exc:`Timeout` error.
<br>

<br>
        .. code-block:: python
<br>

<br>
            # You can use this method in the context manager (recommended)
<br>
            with lock.acquire():
<br>
                pass
<br>

<br>
            # Or use an equivalent try-finally construct:
<br>
            lock.acquire()
<br>
            try:
<br>
                pass
<br>
            finally:
<br>
                lock.release()
<br>

<br>
        :arg float timeout:
<br>
            The maximum time waited for the file lock.
<br>
            If ``timeout < 0``, there is no timeout and this method will
<br>
            block until the lock could be acquired.
<br>
            If ``timeout`` is None, the default :attr:`~timeout` is used.
<br>

<br>
        :arg float poll_intervall:
<br>
            We check once in *poll_intervall* seconds if we can acquire the
<br>
            file lock.
<br>

<br>
        :raises Timeout:
<br>
            if the lock could not be acquired in *timeout* seconds.
<br>

<br>
        .. versionchanged:: 2.0.0
<br>

<br>
            This method returns now a *proxy* object instead of *self*,
<br>
            so that it can be used in a with statement without side effects.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:release' href='parser/test3/utils/filelock.py#L293'>BaseFileLock:release</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>force = False,<br></ul>
        <li>Docs:<br>        """
<br>
        Releases the file lock.
<br>

<br>
        Please note, that the lock is only completly released, if the lock
<br>
        counter is 0.
<br>

<br>
        Also note, that the lock file itself is not automatically deleted.
<br>

<br>
        :arg bool force:
<br>
            If true, the lock counter is ignored and the lock is released in
<br>
            every case.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:__enter__' href='parser/test3/utils/filelock.py#L122'>BaseFileLock:__enter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """
<br>
    Implements the base class of a file lock.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:__exit__' href='parser/test3/utils/filelock.py#L125'>BaseFileLock:__exit__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>exc_type,<br>exc_value,<br>traceback,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:__del__' href='parser/test3/utils/filelock.py#L330'>BaseFileLock:__del__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:BaseFileLock:hash_filename_if_too_long' href='parser/test3/utils/filelock.py#L334'>BaseFileLock:hash_filename_if_too_long</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path:  str,<br>max_length:  int,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:WindowsFileLock:_acquire' href='parser/test3/utils/filelock.py#L192'>WindowsFileLock:_acquire</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Platform dependent. If the file lock could be
<br>
        acquired, self._lock_file_fd holds the file descriptor
<br>
        of the lock file.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:WindowsFileLock:_release' href='parser/test3/utils/filelock.py#L200'>WindowsFileLock:_release</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Releases the lock and sets self._lock_file_fd to None.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:UnixFileLock:_acquire' href='parser/test3/utils/filelock.py#L192'>UnixFileLock:_acquire</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Platform dependent. If the file lock could be
<br>
        acquired, self._lock_file_fd holds the file descriptor
<br>
        of the lock file.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:UnixFileLock:_release' href='parser/test3/utils/filelock.py#L200'>UnixFileLock:_release</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Releases the lock and sets self._lock_file_fd to None.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:SoftFileLock:_acquire' href='parser/test3/utils/filelock.py#L192'>SoftFileLock:_acquire</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Platform dependent. If the file lock could be
<br>
        acquired, self._lock_file_fd holds the file descriptor
<br>
        of the lock file.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/filelock.py:SoftFileLock:_release' href='parser/test3/utils/filelock.py#L200'>SoftFileLock:_release</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """
<br>
        Releases the lock and sets self._lock_file_fd to None.
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/mock_download_manager.py' href='parser/test3/utils/mock_download_manager.py'>parser/test3/utils/mock_download_manager.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager' href='parser/test3/utils/mock_download_manager.py#L33'>MockDownloadManager</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:__init__' href='parser/test3/utils/mock_download_manager.py#L37'>MockDownloadManager:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_name:  str,<br>config:  str,<br>version:  Union[Version,<br>str],<br>cache_dir:  Optional[str]  =  None,<br>use_local_dummy_data:  bool  =  False,<br>load_existing_dummy_data:  bool  =  True,<br>download_callbacks:  Optional[List[Callable]]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:dummy_file' href='parser/test3/utils/mock_download_manager.py#L65'>MockDownloadManager:dummy_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:dummy_data_folder' href='parser/test3/utils/mock_download_manager.py#L71'>MockDownloadManager:dummy_data_folder</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:dummy_zip_file' href='parser/test3/utils/mock_download_manager.py#L79'>MockDownloadManager:dummy_zip_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:download_dummy_data' href='parser/test3/utils/mock_download_manager.py#L82'>MockDownloadManager:download_dummy_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:local_path_to_dummy_data' href='parser/test3/utils/mock_download_manager.py#L94'>MockDownloadManager:local_path_to_dummy_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:github_path_to_dummy_data' href='parser/test3/utils/mock_download_manager.py#L98'>MockDownloadManager:github_path_to_dummy_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:manual_dir' href='parser/test3/utils/mock_download_manager.py#L104'>MockDownloadManager:manual_dir</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:download_and_extract' href='parser/test3/utils/mock_download_manager.py#L112'>MockDownloadManager:download_and_extract</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data_url,<br>*args,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:download' href='parser/test3/utils/mock_download_manager.py#L129'>MockDownloadManager:download</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:download_custom' href='parser/test3/utils/mock_download_manager.py#L133'>MockDownloadManager:download_custom</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data_url,<br>custom_download,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:extract' href='parser/test3/utils/mock_download_manager.py#L137'>MockDownloadManager:extract</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:get_recorded_sizes_checksums' href='parser/test3/utils/mock_download_manager.py#L141'>MockDownloadManager:get_recorded_sizes_checksums</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:create_dummy_data_dict' href='parser/test3/utils/mock_download_manager.py#L144'>MockDownloadManager:create_dummy_data_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_to_dummy_data,<br>data_url,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:create_dummy_data_list' href='parser/test3/utils/mock_download_manager.py#L171'>MockDownloadManager:create_dummy_data_list</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_to_dummy_data,<br>data_url,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/mock_download_manager.py:MockDownloadManager:create_dummy_data_single' href='parser/test3/utils/mock_download_manager.py#L189'>MockDownloadManager:create_dummy_data_single</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_to_dummy_data,<br>data_url,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/commands/env.py' href='parser/test3/commands/env.py'>parser/test3/commands/env.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/commands/env.py:info_command_factory' href='parser/test3/commands/env.py#L10'>info_command_factory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>_,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/commands/env.py:EnvironmentCommand' href='parser/test3/commands/env.py#L14'>EnvironmentCommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/env.py:EnvironmentCommand:register_subcommand' href='parser/test3/commands/env.py#L16'>EnvironmentCommand:register_subcommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>parser:  ArgumentParser,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/env.py:EnvironmentCommand:run' href='parser/test3/commands/env.py#L20'>EnvironmentCommand:run</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/env.py:EnvironmentCommand:format_dict' href='parser/test3/commands/env.py#L34'>EnvironmentCommand:format_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>d,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/streaming.py' href='parser/test3/streaming.py'>parser/test3/streaming.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/streaming.py:extend_module_for_streaming' href='parser/test3/streaming.py#L75'>extend_module_for_streaming</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>module_path,<br>use_auth_token:  Optional[Union[str,<br>bool]]  =  None,<br></ul>
        <li>Docs:<br>    """
<br>
    Extend the `open` and `os.path.join` functions of the module to support data streaming.
<br>
    They rare replaced by `xopen` and `xjoin` defined to work with the StreamingDownloadManager.
<br>

<br>
    We use fsspec to extend `open` to be able to read remote files.
<br>
    To join paths and naviguate in remote compressed archives, we use the "::" separator.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/streaming.py:_PatchedModuleObj' href='parser/test3/streaming.py#L12'>_PatchedModuleObj</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/streaming.py:patch_submodule' href='parser/test3/streaming.py#L22'>patch_submodule</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/streaming.py:_PatchedModuleObj:__init__' href='parser/test3/streaming.py#L15'>_PatchedModuleObj:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>module,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/streaming.py:patch_submodule:__init__' href='parser/test3/streaming.py#L41'>patch_submodule:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>obj,<br>target:  str,<br>new,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/streaming.py:patch_submodule:__enter__' href='parser/test3/streaming.py#L48'>patch_submodule:__enter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/streaming.py:patch_submodule:__exit__' href='parser/test3/streaming.py#L56'>patch_submodule:__exit__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*exc_info,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/streaming.py:patch_submodule:start' href='parser/test3/streaming.py#L59'>patch_submodule:start</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Activate a patch."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/streaming.py:patch_submodule:stop' href='parser/test3/streaming.py#L64'>patch_submodule:stop</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Stop an active patch."""
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/beam_utils.py' href='parser/test3/utils/beam_utils.py'>parser/test3/utils/beam_utils.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/beam_utils.py:upload_local_to_remote' href='parser/test3/utils/beam_utils.py#L27'>upload_local_to_remote</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>local_file_path,<br>remote_file_path,<br>force_upload = False,<br></ul>
        <li>Docs:<br>    """Use the Beam Filesystems to upload to a remote directory on gcs/s3/hdfs..."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/beam_utils.py:download_remote_to_local' href='parser/test3/utils/beam_utils.py#L44'>download_remote_to_local</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>remote_file_path,<br>local_file_path,<br>force_download = False,<br></ul>
        <li>Docs:<br>    """Use the Beam Filesystems to download from a remote directory on gcs/s3/hdfs..."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/beam_utils.py:_create_parquet_sink' href='parser/test3/utils/beam_utils.py#L181'>_create_parquet_sink</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path_prefix,<br>schema,<br>codec,<br>row_group_buffer_size,<br>record_batch_size,<br>use_deprecated_int96_timestamps,<br>file_name_suffix,<br>num_shards,<br>shard_name_template,<br>mime_type,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/beam_utils.py:BeamPipeline' href='parser/test3/utils/beam_utils.py#L19'>BeamPipeline</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/beam_utils.py:WriteToParquet' href='parser/test3/utils/beam_utils.py#L61'>WriteToParquet</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/beam_utils.py:_ParquetSink' href='parser/test3/utils/beam_utils.py#L207'>_ParquetSink</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:BeamPipeline:is_local' href='parser/test3/utils/beam_utils.py#L22'>BeamPipeline:is_local</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:WriteToParquet:__init__' href='parser/test3/utils/beam_utils.py#L72'>WriteToParquet:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>file_path_prefix,<br>schema,<br>row_group_buffer_size = 64 * 1024 * 1024,<br>record_batch_size = 1000,<br>codec = "none",<br>use_deprecated_int96_timestamps = False,<br>file_name_suffix = "",<br>num_shards = 0,<br>shard_name_template = None,<br>mime_type = "application/x-parquet",<br>,<br></ul>
        <li>Docs:<br>        """Initialize a WriteToParquet transform.
<br>
        (from apache_beam.io.parquetio, only ._flush_buffer() is different)
<br>

<br>
        Writes parquet files from a :class:`~apache_beam.pvalue.PCollection` of
<br>
        records. Each record is a dictionary with keys of a string type that
<br>
        represent column names. Schema must be specified like the example below.
<br>

<br>
        .. testsetup::
<br>

<br>
            from tempfile import NamedTemporaryFile
<br>
            import glob
<br>
            import os
<br>
            import pyarrow
<br>

<br>
            filename = NamedTemporaryFile(delete=False).name
<br>

<br>
        .. testcode::
<br>

<br>
            with beam.Pipeline() as p:
<br>
                records = p | 'Read' >> beam.Create(
<br>
                        [{'name': 'foo', 'age': 10}, {'name': 'bar', 'age': 20}]
<br>
                )
<br>
                _ = records | 'Write' >> beam.io.WriteToParquet(filename,
<br>
                        pyarrow.schema(
<br>
                                [('name', pyarrow.binary()), ('age', pyarrow.int64())]
<br>
                        )
<br>
                )
<br>

<br>
        .. testcleanup::
<br>

<br>
            for output in glob.glob('{}*'.format(filename)):
<br>
                os.remove(output)
<br>

<br>
        For more information on supported types and schema, please see the pyarrow
<br>
        document.
<br>

<br>
        Args:
<br>
            file_path_prefix: The file path to write to. The files written will begin
<br>
                with this prefix, followed by a shard identifier (see num_shards), and
<br>
                end in a common extension, if given by file_name_suffix. In most cases,
<br>
                only this argument is specified and num_shards, shard_name_template, and
<br>
                file_name_suffix use default values.
<br>
            schema: The schema to use, as type of ``pyarrow.Schema``.
<br>
            row_group_buffer_size: The byte size of the row group buffer. Note that
<br>
                this size is for uncompressed data on the memory and normally much
<br>
                bigger than the actual row group size written to a file.
<br>
            record_batch_size: The number of records in each record batch. Record
<br>
                batch is a basic unit used for storing data in the row group buffer.
<br>
                A higher record batch size implies low granularity on a row group buffer
<br>
                size. For configuring a row group size based on the number of records,
<br>
                set ``row_group_buffer_size`` to 1 and use ``record_batch_size`` to
<br>
                adjust the value.
<br>
            codec: The codec to use for block-level compression. Any string supported
<br>
                by the pyarrow specification is accepted.
<br>
            use_deprecated_int96_timestamps: Write nanosecond resolution timestamps to
<br>
                INT96 Parquet format. Defaults to False.
<br>
            file_name_suffix: Suffix for the files written.
<br>
            num_shards: The number of files (shards) used for output. If not set, the
<br>
                service will decide on the optimal number of shards.
<br>
                Constraining the number of shards is likely to reduce
<br>
                the performance of a pipeline.  Setting this value is not recommended
<br>
                unless you require a specific number of output files.
<br>
            shard_name_template: A template string containing placeholders for
<br>
                the shard number and shard count. When constructing a filename for a
<br>
                particular shard number, the upper-case letters 'S' and 'N' are
<br>
                replaced with the 0-padded shard number and shard count respectively.
<br>
                This argument can be '' in which case it behaves as if num_shards was
<br>
                set to 1 and only one file will be generated. The default pattern used
<br>
                is '-SSSSS-of-NNNNN' if None is passed as the shard_name_template.
<br>
            mime_type: The MIME type to use for the produced files, if the filesystem
<br>
                supports specifying MIME types.
<br>

<br>
        Returns:
<br>
            A WriteToParquet transform usable for writing.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:WriteToParquet:expand' href='parser/test3/utils/beam_utils.py#L174'>WriteToParquet:expand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pcoll,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:WriteToParquet:display_data' href='parser/test3/utils/beam_utils.py#L177'>WriteToParquet:display_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:_ParquetSink:__init__' href='parser/test3/utils/beam_utils.py#L72'>_ParquetSink:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>file_path_prefix,<br>schema,<br>codec,<br>row_group_buffer_size,<br>record_batch_size,<br>use_deprecated_int96_timestamps,<br>file_name_suffix,<br>num_shards,<br>shard_name_template,<br>mime_type,<br>,<br></ul>
        <li>Docs:<br>        """Initialize a WriteToParquet transform.
<br>
        (from apache_beam.io.parquetio, only ._flush_buffer() is different)
<br>

<br>
        Writes parquet files from a :class:`~apache_beam.pvalue.PCollection` of
<br>
        records. Each record is a dictionary with keys of a string type that
<br>
        represent column names. Schema must be specified like the example below.
<br>

<br>
        .. testsetup::
<br>

<br>
            from tempfile import NamedTemporaryFile
<br>
            import glob
<br>
            import os
<br>
            import pyarrow
<br>

<br>
            filename = NamedTemporaryFile(delete=False).name
<br>

<br>
        .. testcode::
<br>

<br>
            with beam.Pipeline() as p:
<br>
                records = p | 'Read' >> beam.Create(
<br>
                        [{'name': 'foo', 'age': 10}, {'name': 'bar', 'age': 20}]
<br>
                )
<br>
                _ = records | 'Write' >> beam.io.WriteToParquet(filename,
<br>
                        pyarrow.schema(
<br>
                                [('name', pyarrow.binary()), ('age', pyarrow.int64())]
<br>
                        )
<br>
                )
<br>

<br>
        .. testcleanup::
<br>

<br>
            for output in glob.glob('{}*'.format(filename)):
<br>
                os.remove(output)
<br>

<br>
        For more information on supported types and schema, please see the pyarrow
<br>
        document.
<br>

<br>
        Args:
<br>
            file_path_prefix: The file path to write to. The files written will begin
<br>
                with this prefix, followed by a shard identifier (see num_shards), and
<br>
                end in a common extension, if given by file_name_suffix. In most cases,
<br>
                only this argument is specified and num_shards, shard_name_template, and
<br>
                file_name_suffix use default values.
<br>
            schema: The schema to use, as type of ``pyarrow.Schema``.
<br>
            row_group_buffer_size: The byte size of the row group buffer. Note that
<br>
                this size is for uncompressed data on the memory and normally much
<br>
                bigger than the actual row group size written to a file.
<br>
            record_batch_size: The number of records in each record batch. Record
<br>
                batch is a basic unit used for storing data in the row group buffer.
<br>
                A higher record batch size implies low granularity on a row group buffer
<br>
                size. For configuring a row group size based on the number of records,
<br>
                set ``row_group_buffer_size`` to 1 and use ``record_batch_size`` to
<br>
                adjust the value.
<br>
            codec: The codec to use for block-level compression. Any string supported
<br>
                by the pyarrow specification is accepted.
<br>
            use_deprecated_int96_timestamps: Write nanosecond resolution timestamps to
<br>
                INT96 Parquet format. Defaults to False.
<br>
            file_name_suffix: Suffix for the files written.
<br>
            num_shards: The number of files (shards) used for output. If not set, the
<br>
                service will decide on the optimal number of shards.
<br>
                Constraining the number of shards is likely to reduce
<br>
                the performance of a pipeline.  Setting this value is not recommended
<br>
                unless you require a specific number of output files.
<br>
            shard_name_template: A template string containing placeholders for
<br>
                the shard number and shard count. When constructing a filename for a
<br>
                particular shard number, the upper-case letters 'S' and 'N' are
<br>
                replaced with the 0-padded shard number and shard count respectively.
<br>
                This argument can be '' in which case it behaves as if num_shards was
<br>
                set to 1 and only one file will be generated. The default pattern used
<br>
                is '-SSSSS-of-NNNNN' if None is passed as the shard_name_template.
<br>
            mime_type: The MIME type to use for the produced files, if the filesystem
<br>
                supports specifying MIME types.
<br>

<br>
        Returns:
<br>
            A WriteToParquet transform usable for writing.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:_ParquetSink:open' href='parser/test3/utils/beam_utils.py#L244'>_ParquetSink:open</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>temp_path,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:_ParquetSink:write_record' href='parser/test3/utils/beam_utils.py#L253'>_ParquetSink:write_record</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>writer,<br>value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:_ParquetSink:close' href='parser/test3/utils/beam_utils.py#L264'>_ParquetSink:close</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>writer,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:_ParquetSink:display_data' href='parser/test3/utils/beam_utils.py#L177'>_ParquetSink:display_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """A sink for parquet files."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:_ParquetSink:_write_batches' href='parser/test3/utils/beam_utils.py#L282'>_ParquetSink:_write_batches</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>writer,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/beam_utils.py:_ParquetSink:_flush_buffer' href='parser/test3/utils/beam_utils.py#L288'>_ParquetSink:_flush_buffer</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/io/text.py' href='parser/test3/io/text.py'>parser/test3/io/text.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/io/text.py:TextDatasetReader' href='parser/test3/io/text.py#L9'>TextDatasetReader</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/text.py:TextDatasetReader:__init__' href='parser/test3/io/text.py#L10'>TextDatasetReader:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_paths:  NestedDataStructureLike[PathLike],<br>split:  Optional[NamedSplit]  =  None,<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/text.py:TextDatasetReader:read' href='parser/test3/io/text.py#L30'>TextDatasetReader:read</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/filesystems/s3filesystem.py' href='parser/test3/filesystems/s3filesystem.py'>parser/test3/filesystems/s3filesystem.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/filesystems/s3filesystem.py:S3FileSystem' href='parser/test3/filesystems/s3filesystem.py#L4'>S3FileSystem</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/doc_utils.py' href='parser/test3/utils/doc_utils.py'>parser/test3/utils/doc_utils.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/doc_utils.py:is_documented_by' href='parser/test3/utils/doc_utils.py#L4'>is_documented_by</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>function_with_docstring:  Callable,<br></ul>
        <li>Docs:<br>    """Decorator to share docstrings across common functions.
<br>

<br>
    Args:
<br>
        function_with_docstring (`Callable`): Name of the function with the docstring.
<br>
    """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/py_utils.py' href='parser/test3/utils/py_utils.py'>parser/test3/utils/py_utils.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:size_str' href='parser/test3/utils/py_utils.py#L59'>size_str</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>size_in_bytes,<br></ul>
        <li>Docs:<br>    """Returns a human readable size string.
<br>

<br>
    If size_in_bytes is None, then returns "Unknown size".
<br>

<br>
    For example `size_str(1.5 * datasets.units.GiB) == "1.50 GiB"`.
<br>

<br>
    Args:
<br>
        size_in_bytes: `int` or `None`, the size, in bytes, that we want to
<br>
            format as a human-readable size string.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:temporary_assignment' href='parser/test3/utils/py_utils.py#L84'>temporary_assignment</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>obj,<br>attr,<br>value,<br></ul>
        <li>Docs:<br>    """Temporarily assign obj.attr to value."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:zip_dict' href='parser/test3/utils/py_utils.py#L94'>zip_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*dicts,<br></ul>
        <li>Docs:<br>    """Iterate over items of dictionaries grouped by their keys."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:_single_map_nested' href='parser/test3/utils/py_utils.py#L136'>_single_map_nested</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>args,<br></ul>
        <li>Docs:<br>    """Apply a function recursively to each element of a nested data struct."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:map_nested' href='parser/test3/utils/py_utils.py#L169'>map_nested</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>function,<br>data_struct,<br>dict_only:  bool  =  False,<br>map_list:  bool  =  True,<br>map_tuple:  bool  =  False,<br>map_numpy:  bool  =  False,<br>num_proc:  Optional[int]  =  None,<br>types = None,<br>,<br></ul>
        <li>Docs:<br>    """Apply a function recursively to each element of a nested data struct.
<br>
    If num_proc > 1 and the length of data_struct is longer than num_proc: use multi-processing
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:zip_nested' href='parser/test3/utils/py_utils.py#L241'>zip_nested</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>arg0,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """Zip data struct together and return a data struct with the same shape."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:flatten_nest_dict' href='parser/test3/utils/py_utils.py#L257'>flatten_nest_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>d,<br></ul>
        <li>Docs:<br>    """Return the dict with all nested keys flattened joined with '/'."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:has_sufficient_disk_space' href='parser/test3/utils/py_utils.py#L283'>has_sufficient_disk_space</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>needed_bytes,<br>directory = ".",<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:dump' href='parser/test3/utils/py_utils.py#L310'>dump</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>obj,<br>file,<br></ul>
        <li>Docs:<br>    """pickle an object to a file"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:_no_cache_fields' href='parser/test3/utils/py_utils.py#L317'>_no_cache_fields</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>obj,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:dumps' href='parser/test3/utils/py_utils.py#L336'>dumps</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>obj,<br></ul>
        <li>Docs:<br>    """pickle an object to a string"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:pklregister' href='parser/test3/utils/py_utils.py#L344'>pklregister</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>t,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:_save_code' href='parser/test3/utils/py_utils.py#L394'>_save_code</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>pickler,<br>obj,<br></ul>
        <li>Docs:<br>    """
<br>
    From dill._dill.save_code
<br>
    This is a modified version that removes the origin (filename + line no.)
<br>
    of functions created in notebooks or shells for example.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:save_function' href='parser/test3/utils/py_utils.py#L475'>save_function</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>pickler,<br>obj,<br></ul>
        <li>Docs:<br>    """
<br>
    From dill._dill.save_function
<br>
    This is a modified version that make globs deterministic since the order of
<br>
    the keys in the output dictionary of globalvars can change.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/py_utils.py:copyfunc' href='parser/test3/utils/py_utils.py#L548'>copyfunc</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>func,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/py_utils.py:NonMutableDict' href='parser/test3/utils/py_utils.py#L101'>NonMutableDict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/py_utils.py:classproperty' href='parser/test3/utils/py_utils.py#L129'>classproperty</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/py_utils.py:NestedDataStructure' href='parser/test3/utils/py_utils.py#L269'>NestedDataStructure</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/py_utils.py:Pickler' href='parser/test3/utils/py_utils.py#L291'>Pickler</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/py_utils.py:_CloudPickleTypeHintFix' href='parser/test3/utils/py_utils.py#L352'>_CloudPickleTypeHintFix</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:NonMutableDict:__init__' href='parser/test3/utils/py_utils.py#L109'>NonMutableDict:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:NonMutableDict:__setitem__' href='parser/test3/utils/py_utils.py#L118'>NonMutableDict:__setitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>key,<br>value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:NonMutableDict:update' href='parser/test3/utils/py_utils.py#L123'>NonMutableDict:update</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:classproperty:__get__' href='parser/test3/utils/py_utils.py#L132'>classproperty:__get__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>obj,<br>objtype = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:NestedDataStructure:__init__' href='parser/test3/utils/py_utils.py#L270'>NestedDataStructure:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:NestedDataStructure:flatten' href='parser/test3/utils/py_utils.py#L273'>NestedDataStructure:flatten</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:Pickler:save_global' href='parser/test3/utils/py_utils.py#L296'>Pickler:save_global</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>obj,<br>name = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:_CloudPickleTypeHintFix:_is_parametrized_type_hint' href='parser/test3/utils/py_utils.py#L360'>_CloudPickleTypeHintFix:_is_parametrized_type_hint</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>obj,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:_CloudPickleTypeHintFix:_create_parametrized_type_hint' href='parser/test3/utils/py_utils.py#L367'>_CloudPickleTypeHintFix:_create_parametrized_type_hint</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>origin,<br>args,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/py_utils.py:_CloudPickleTypeHintFix:_save_parametrized_type_hint' href='parser/test3/utils/py_utils.py#L370'>_CloudPickleTypeHintFix:_save_parametrized_type_hint</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>pickler,<br>obj,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/readme.py' href='parser/test3/utils/readme.py'>parser/test3/utils/readme.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/readme.py:load_yaml_resource' href='parser/test3/utils/readme.py#L23'>load_yaml_resource</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>resource:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/readme.py:Section' href='parser/test3/utils/readme.py#L40'>Section</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/readme.py:ReadMe' href='parser/test3/utils/readme.py#L173'>ReadMe</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:Section:__init__' href='parser/test3/utils/readme.py#L41'>Section:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>name:  str,<br>level:  str,<br>lines:  List[str]  =  None,<br>suppress_parsing_errors:  bool  =  False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:Section:parse' href='parser/test3/utils/readme.py#L53'>Section:parse</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>suppress_parsing_errors:  bool  =  False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:Section:validate' href='parser/test3/utils/readme.py#L95'>Section:validate</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>structure:  dict,<br></ul>
        <li>Docs:<br>        """Validates a Section class object recursively using the structure provided as a dictionary.
<br>

<br>
        Args:
<br>
            structute (:obj: `dict`): The dictionary representing expected structure.
<br>

<br>
        Returns:
<br>
            :obj: `ReadmeValidatorOutput`: The dictionary representation of the section, and the errors.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:Section:to_dict' href='parser/test3/utils/readme.py#L163'>Section:to_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Returns the dictionary representation of a section."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:ReadMe:__init__' href='parser/test3/utils/readme.py#L174'>ReadMe:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>name:  str,<br>lines:  List[str],<br>structure:  dict  =  None,<br>suppress_parsing_errors:  bool  =  False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:ReadMe:validate' href='parser/test3/utils/readme.py#L183'>ReadMe:validate</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:ReadMe:from_readme' href='parser/test3/utils/readme.py#L194'>ReadMe:from_readme</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>path:  Path,<br>structure:  dict  =  None,<br>suppress_parsing_errors:  bool  =  False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:ReadMe:from_string' href='parser/test3/utils/readme.py#L200'>ReadMe:from_string</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>string:  str,<br>structure:  dict  =  None,<br>root_name:  str  =  "root",<br>suppress_parsing_errors:  bool  =  False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:ReadMe:parse' href='parser/test3/utils/readme.py#L53'>ReadMe:parse</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>suppress_parsing_errors:  bool  =  False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:ReadMe:__str__' href='parser/test3/utils/readme.py#L223'>ReadMe:__str__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Returns the string of dictionary representation of the ReadMe."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/readme.py:ReadMe:_validate' href='parser/test3/utils/readme.py#L227'>ReadMe:_validate</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>readme_structure,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/streaming_download_manager.py' href='parser/test3/utils/streaming_download_manager.py'>parser/test3/utils/streaming_download_manager.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/streaming_download_manager.py:xjoin' href='parser/test3/utils/streaming_download_manager.py#L20'>xjoin</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>a,<br>*p,<br></ul>
        <li>Docs:<br>    """
<br>
    This function extends os.path.join to support the "::" hop separator. It supports both paths and urls.
<br>

<br>
    A shorthand, particularly useful where you have multiple hops, is to “chain” the URLs with the special separator "::".
<br>
    This is used to access files inside a zip file over http for example.
<br>

<br>
    Let's say you have a zip file at https://host.com/archive.zip, and you want to access the file inside the zip file at /folder1/file.txt.
<br>
    Then you can just chain the url this way:
<br>

<br>
        zip://folder1/file.txt::https://host.com/archive.zip
<br>

<br>
    The xjoin function allows you to apply the join on the first path of the chain.
<br>

<br>
    Example::
<br>

<br>
        >>> xjoin("zip://folder1::https://host.com/archive.zip", "file.txt")
<br>
        zip://folder1/file.txt::https://host.com/archive.zip
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/streaming_download_manager.py:_add_retries_to_file_obj_read_method' href='parser/test3/utils/streaming_download_manager.py#L47'>_add_retries_to_file_obj_read_method</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_obj,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/streaming_download_manager.py:xopen' href='parser/test3/utils/streaming_download_manager.py#L68'>xopen</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file,<br>mode = "r",<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    This function extends the builin `open` function to support remote files using fsspec.
<br>

<br>
    It also has a retry mechanism in case connection fails.
<br>
    The args and kwargs are passed to fsspec.open, except `use_auth_token` which is used for queries to private repos on huggingface.co
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/streaming_download_manager.py:StreamingDownloadManager' href='parser/test3/utils/streaming_download_manager.py#L82'>StreamingDownloadManager</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/streaming_download_manager.py:StreamingDownloadManager:__init__' href='parser/test3/utils/streaming_download_manager.py#L90'>StreamingDownloadManager:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_name:  Optional[str]  =  None,<br>data_dir:  Optional[str]  =  None,<br>download_config:  Optional[DownloadConfig]  =  None,<br>base_path:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/streaming_download_manager.py:StreamingDownloadManager:manual_dir' href='parser/test3/utils/streaming_download_manager.py#L103'>StreamingDownloadManager:manual_dir</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/streaming_download_manager.py:StreamingDownloadManager:download' href='parser/test3/utils/streaming_download_manager.py#L106'>StreamingDownloadManager:download</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>url_or_urls,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/streaming_download_manager.py:StreamingDownloadManager:_download' href='parser/test3/utils/streaming_download_manager.py#L110'>StreamingDownloadManager:_download</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>url_or_filename,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/streaming_download_manager.py:StreamingDownloadManager:extract' href='parser/test3/utils/streaming_download_manager.py#L116'>StreamingDownloadManager:extract</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_paths,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/streaming_download_manager.py:StreamingDownloadManager:_extract' href='parser/test3/utils/streaming_download_manager.py#L120'>StreamingDownloadManager:_extract</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>urlpath,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/streaming_download_manager.py:StreamingDownloadManager:_get_extraction_protocol' href='parser/test3/utils/streaming_download_manager.py#L131'>StreamingDownloadManager:_get_extraction_protocol</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>urlpath,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/streaming_download_manager.py:StreamingDownloadManager:download_and_extract' href='parser/test3/utils/streaming_download_manager.py#L141'>StreamingDownloadManager:download_and_extract</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>url_or_urls,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/info.py' href='parser/test3/info.py'>parser/test3/info.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/info.py:SupervisedKeysData' href='parser/test3/info.py#L53'>SupervisedKeysData</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/info.py:DownloadChecksumsEntryData' href='parser/test3/info.py#L59'>DownloadChecksumsEntryData</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/info.py:MissingCachedSizesConfigError' href='parser/test3/info.py#L64'>MissingCachedSizesConfigError</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/info.py:NonMatchingCachedSizesError' href='parser/test3/info.py#L68'>NonMatchingCachedSizesError</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/info.py:PostProcessedInfo' href='parser/test3/info.py#L73'>PostProcessedInfo</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/info.py:DatasetInfo' href='parser/test3/info.py#L89'>DatasetInfo</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/info.py:DatasetInfosDict' href='parser/test3/info.py#L283'>DatasetInfosDict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/info.py:MetricInfo' href='parser/test3/info.py#L308'>MetricInfo</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:PostProcessedInfo:__post_init__' href='parser/test3/info.py#L77'>PostProcessedInfo:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:PostProcessedInfo:from_dict' href='parser/test3/info.py#L83'>PostProcessedInfo:from_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>post_processed_info_dict:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:__post_init__' href='parser/test3/info.py#L77'>DatasetInfo:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:_license_path' href='parser/test3/info.py#L184'>DatasetInfo:_license_path</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_info_dir,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:write_to_directory' href='parser/test3/info.py#L187'>DatasetInfo:write_to_directory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_info_dir,<br></ul>
        <li>Docs:<br>        """Write `DatasetInfo` as JSON to `dataset_info_dir`.
<br>

<br>
        Also save the license separately in LICENCE.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:_dump_info' href='parser/test3/info.py#L198'>DatasetInfo:_dump_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>file,<br></ul>
        <li>Docs:<br>        """Dump info in `file` file-like object open in bytes mode (to support remote files)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:_dump_license' href='parser/test3/info.py#L202'>DatasetInfo:_dump_license</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>file,<br></ul>
        <li>Docs:<br>        """Dump license in `file` file-like object open in bytes mode (to support remote files)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:from_merge' href='parser/test3/info.py#L207'>DatasetInfo:from_merge</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>dataset_infos:  List["DatasetInfo"],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:from_directory' href='parser/test3/info.py#L244'>DatasetInfo:from_directory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>dataset_info_dir:  str,<br></ul>
        <li>Docs:<br>        """Create DatasetInfo from the JSON file in `dataset_info_dir`.
<br>

<br>
        This function updates all the dynamically generated fields (num_examples,
<br>
        hash, time of creation,...) of the DatasetInfo.
<br>

<br>
        This will overwrite all previous metadata.
<br>

<br>
        Args:
<br>
            dataset_info_dir (`str`): The directory containing the metadata file. This
<br>
                should be the root directory of a specific dataset version.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:from_dict' href='parser/test3/info.py#L265'>DatasetInfo:from_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>dataset_info_dict:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:update' href='parser/test3/info.py#L269'>DatasetInfo:update</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other_dataset_info:  "DatasetInfo",<br>ignore_none = True,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfo:copy' href='parser/test3/info.py#L279'>DatasetInfo:copy</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfosDict:write_to_directory' href='parser/test3/info.py#L284'>DatasetInfosDict:write_to_directory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_infos_dir,<br>overwrite = False,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:DatasetInfosDict:from_directory' href='parser/test3/info.py#L297'>DatasetInfosDict:from_directory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>dataset_infos_dir,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:MetricInfo:__post_init__' href='parser/test3/info.py#L77'>MetricInfo:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """Information about a dataset.
<br>

<br>
    `DatasetInfo` documents datasets, including its name, version, and features.
<br>
    See the constructor arguments and properties for a full list.
<br>

<br>
    Note: Not all fields are known on construction and may be updated later.
<br>

<br>
    Attributes:
<br>
        description (str): A description of the dataset.
<br>
        citation (str): A BibTeX citation of the dataset.
<br>
        homepage (str): A URL to the official homepage for the dataset.
<br>
        license (str): The dataset's license. It can be the name of the license or a paragraph containing the terms of the license.
<br>
        features (Features, optional): The features used to specify the dataset's column types.
<br>
        post_processed (PostProcessedInfo, optional): Information regarding the resources of a possible post-processing of a dataset. For example, it can contain the information of an index.
<br>
        supervised_keys (SupervisedKeysData, optional): Specifies the input feature and the label for supervised learning if applicable for the dataset (legacy from TFDS).
<br>
        builder_name (str, optional): The name of the :class:`GeneratorBasedBuilder` subclass used to create the dataset. Usually matched to the corresponding script name. It is also the snake_case version of the dataset builder class name.
<br>
        config_name (str, optional): The name of the configuration derived from :class:`BuilderConfig`
<br>
        version (str or Version, optional): The version of the dataset.
<br>
        splits (dict, optional): The mapping between split name and metadata.
<br>
        download_checksums (dict, optional): The mapping between the URL to download the dataset's checksums and corresponding metadata.
<br>
        download_size (int, optional): The size of the files to download to generate the dataset, in bytes.
<br>
        post_processing_size (int, optional): Size of the dataset in bytes after post-processing, if any.
<br>
        dataset_size (int, optional): The combined size in bytes of the Arrow tables for all splits.
<br>
        size_in_bytes (int, optional): The combined size in bytes of all files associated with the dataset (downloaded files + Arrow files).
<br>
        task_templates (List[TaskTemplate], optional): The task templates to prepare the dataset for during training and evaluation. Each template casts the dataset's :class:`Features` to standardized column names and types as detailed in :py:mod:`datasets.tasks`.
<br>
        **config_kwargs: Keyword arguments to be passed to the :class:`BuilderConfig` and used in the :class:`DatasetBuilder`.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:MetricInfo:write_to_directory' href='parser/test3/info.py#L344'>MetricInfo:write_to_directory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>metric_info_dir,<br></ul>
        <li>Docs:<br>        """Write `MetricInfo` as JSON to `metric_info_dir`.
<br>
        Also save the license separately in LICENCE.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:MetricInfo:from_directory' href='parser/test3/info.py#L355'>MetricInfo:from_directory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>metric_info_dir,<br></ul>
        <li>Docs:<br>        """Create MetricInfo from the JSON file in `metric_info_dir`.
<br>

<br>
        Args:
<br>
            metric_info_dir: `str` The directory containing the metadata file. This
<br>
                should be the root directory of a specific dataset version.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/info.py:MetricInfo:from_dict' href='parser/test3/info.py#L371'>MetricInfo:from_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>metric_info_dict:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/tasks/automatic_speech_recognition.py' href='parser/test3/tasks/automatic_speech_recognition.py'>parser/test3/tasks/automatic_speech_recognition.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/tasks/automatic_speech_recognition.py:AutomaticSpeechRecognition' href='parser/test3/tasks/automatic_speech_recognition.py#L9'>AutomaticSpeechRecognition</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/tasks/automatic_speech_recognition.py:AutomaticSpeechRecognition:column_mapping' href='parser/test3/tasks/automatic_speech_recognition.py#L19'>AutomaticSpeechRecognition:column_mapping</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/table.py' href='parser/test3/table.py'>parser/test3/table.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:inject_arrow_table_documentation' href='parser/test3/table.py#L19'>inject_arrow_table_documentation</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>arrow_table_method,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:_in_memory_arrow_table_from_file' href='parser/test3/table.py#L28'>_in_memory_arrow_table_from_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>filename:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:_in_memory_arrow_table_from_buffer' href='parser/test3/table.py#L35'>_in_memory_arrow_table_from_buffer</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>buffer:  pa.Buffer,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:_memory_mapped_arrow_table_from_file' href='parser/test3/table.py#L42'>_memory_mapped_arrow_table_from_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>filename:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:_write_table_to_file' href='parser/test3/table.py#L49'>_write_table_to_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>table:  pa.Table,<br>filename:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:_deepcopy' href='parser/test3/table.py#L59'>_deepcopy</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>x,<br>memo:  dict,<br></ul>
        <li>Docs:<br>    """deepcopy a regular class instance"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:_interpolation_search' href='parser/test3/table.py#L69'>_interpolation_search</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>arr:  List[int],<br>x:  int,<br></ul>
        <li>Docs:<br>    """
<br>
    Return the position i of a sorted array so that arr[i] <= x < arr[i+1]
<br>

<br>
    Args:
<br>
        arr (:obj:`List[int]`): non-empty sorted list of integers
<br>
        x (:obj:`int`): query
<br>

<br>
    Returns:
<br>
        `int`: the position i so that arr[i] <= x < arr[i+1]
<br>

<br>
    Raises:
<br>
        `IndexError`: if the array is empty or if the query is outside the array values
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:concat_tables' href='parser/test3/table.py#L833'>concat_tables</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>tables:  List[Table],<br>axis:  int  =  0,<br></ul>
        <li>Docs:<br>    """
<br>
    Concatenate tables.
<br>

<br>
    Args:
<br>
        tables (list of :class:`Table`): List of tables to be concatenated.
<br>
        axis (``{0, 1}``, default ``0``, meaning over rows):
<br>
            Axis to concatenate over, where ``0`` means over rows (vertically) and ``1`` means over columns
<br>
            (horizontally).
<br>

<br>
            .. versionadded:: 1.6.0
<br>

<br>
    Returns:
<br>
        :obj:`datasets.table.Table` that is the concatenated table:
<br>
            If the number of input tables is > 1, then the returned table is a :obj:`datasets.table.ConcatenationTable`.
<br>
            Otherwise if there's only one table, it is returned as is.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:list_table_cache_files' href='parser/test3/table.py#L856'>list_table_cache_files</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>table:  Table,<br></ul>
        <li>Docs:<br>    """
<br>
    Get the cache files that are loaded by the table.
<br>
    Cache file are used when parts of the table come from the disk via memory mapping.
<br>

<br>
    Returns:
<br>
        :obj:`List[str]`: a list of paths to the cache files loaded by the table
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/table.py:cast_with_sliced_list_support' href='parser/test3/table.py#L876'>cast_with_sliced_list_support</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>pa_table:  pa.Table,<br>schema:  pa.Schema,<br></ul>
        <li>Docs:<br>    """Same as pyarrow.Table.cast, except it works for sliced list arrays"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/table.py:IndexedTableMixin' href='parser/test3/table.py#L95'>IndexedTableMixin</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/table.py:Table' href='parser/test3/table.py#L141'>Table</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/table.py:TableBlock' href='parser/test3/table.py#L317'>TableBlock</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/table.py:InMemoryTable' href='parser/test3/table.py#L327'>InMemoryTable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/table.py:MemoryMappedTable' href='parser/test3/table.py#L422'>MemoryMappedTable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/table.py:ConcatenationTable' href='parser/test3/table.py#L551'>ConcatenationTable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:IndexedTableMixin:__init__' href='parser/test3/table.py#L96'>IndexedTableMixin:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:IndexedTableMixin:fast_gather' href='parser/test3/table.py#L101'>IndexedTableMixin:fast_gather</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>indices:  Union[List[int],<br>np.ndarray],<br></ul>
        <li>Docs:<br>        """
<br>
        Create a pa.Table by gathering the records at the records at the specified indices. Should be faster
<br>
        than pa.concat_tables(table.fast_slice(int(i) % table.num_rows, 1) for i in indices) since NumPy can compute
<br>
        the binary searches in parallel, highly optimized C
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:IndexedTableMixin:fast_slice' href='parser/test3/table.py#L117'>IndexedTableMixin:fast_slice</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>offset = 0,<br>length = None,<br></ul>
        <li>Docs:<br>        """
<br>
        Slice the Table using interpolation search.
<br>
        The behavior is the same as :obj:`pyarrow.Table.slice` but it's significantly faster.
<br>

<br>
        Interpolation search is used to find the start and end indexes of the batches we want to keep.
<br>
        The batches to keep are then concatenated to form the sliced Table.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:__init__' href='parser/test3/table.py#L96'>Table:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>table:  pa.Table,<br></ul>
        <li>Docs:<br>        """
<br>
        Create a pa.Table by gathering the records at the records at the specified indices. Should be faster
<br>
        than pa.concat_tables(table.fast_slice(int(i) % table.num_rows, 1) for i in indices) since NumPy can compute
<br>
        the binary searches in parallel, highly optimized C
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:__deepcopy__' href='parser/test3/table.py#L157'>Table:__deepcopy__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>memo:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:__getstate__' href='parser/test3/table.py#L166'>Table:__getstate__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:__setstate__' href='parser/test3/table.py#L181'>Table:__setstate__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>state,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:validate' href='parser/test3/table.py#L193'>Table:validate</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:equals' href='parser/test3/table.py#L197'>Table:equals</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:to_batches' href='parser/test3/table.py#L203'>Table:to_batches</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:to_pydict' href='parser/test3/table.py#L207'>Table:to_pydict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:to_pandas' href='parser/test3/table.py#L211'>Table:to_pandas</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:to_string' href='parser/test3/table.py#L214'>Table:to_string</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:field' href='parser/test3/table.py#L218'>Table:field</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:column' href='parser/test3/table.py#L222'>Table:column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:itercolumns' href='parser/test3/table.py#L226'>Table:itercolumns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:schema' href='parser/test3/table.py#L230'>Table:schema</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:columns' href='parser/test3/table.py#L234'>Table:columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:num_columns' href='parser/test3/table.py#L238'>Table:num_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:num_rows' href='parser/test3/table.py#L242'>Table:num_rows</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:shape' href='parser/test3/table.py#L246'>Table:shape</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:nbytes' href='parser/test3/table.py#L250'>Table:nbytes</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:column_names' href='parser/test3/table.py#L254'>Table:column_names</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:__eq__' href='parser/test3/table.py#L257'>Table:__eq__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:__getitem__' href='parser/test3/table.py#L260'>Table:__getitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>i,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:__len__' href='parser/test3/table.py#L263'>Table:__len__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:__repr__' href='parser/test3/table.py#L266'>Table:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:__str__' href='parser/test3/table.py#L269'>Table:__str__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:slice' href='parser/test3/table.py#L273'>Table:slice</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:filter' href='parser/test3/table.py#L277'>Table:filter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:flatten' href='parser/test3/table.py#L281'>Table:flatten</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:combine_chunks' href='parser/test3/table.py#L285'>Table:combine_chunks</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:cast' href='parser/test3/table.py#L289'>Table:cast</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:add_column' href='parser/test3/table.py#L293'>Table:add_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:append_column' href='parser/test3/table.py#L297'>Table:append_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:remove_column' href='parser/test3/table.py#L301'>Table:remove_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:set_column' href='parser/test3/table.py#L305'>Table:set_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:rename_columns' href='parser/test3/table.py#L309'>Table:rename_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:Table:drop' href='parser/test3/table.py#L313'>Table:drop</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:from_file' href='parser/test3/table.py#L343'>InMemoryTable:from_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>filename:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:from_buffer' href='parser/test3/table.py#L348'>InMemoryTable:from_buffer</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>buffer:  pa.Buffer,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:from_pandas' href='parser/test3/table.py#L354'>InMemoryTable:from_pandas</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:from_arrays' href='parser/test3/table.py#L359'>InMemoryTable:from_arrays</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:from_pydict' href='parser/test3/table.py#L364'>InMemoryTable:from_pydict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:from_batches' href='parser/test3/table.py#L369'>InMemoryTable:from_batches</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:slice' href='parser/test3/table.py#L373'>InMemoryTable:slice</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>offset = 0,<br>length = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:filter' href='parser/test3/table.py#L277'>InMemoryTable:filter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:flatten' href='parser/test3/table.py#L281'>InMemoryTable:flatten</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:combine_chunks' href='parser/test3/table.py#L285'>InMemoryTable:combine_chunks</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:cast' href='parser/test3/table.py#L289'>InMemoryTable:cast</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:add_column' href='parser/test3/table.py#L293'>InMemoryTable:add_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:append_column' href='parser/test3/table.py#L297'>InMemoryTable:append_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:remove_column' href='parser/test3/table.py#L301'>InMemoryTable:remove_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:set_column' href='parser/test3/table.py#L305'>InMemoryTable:set_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:rename_columns' href='parser/test3/table.py#L309'>InMemoryTable:rename_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:InMemoryTable:drop' href='parser/test3/table.py#L313'>InMemoryTable:drop</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:__init__' href='parser/test3/table.py#L443'>MemoryMappedTable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>table:  pa.Table,<br>path:  str,<br>replays:  Optional[List[Replay]]  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:from_file' href='parser/test3/table.py#L449'>MemoryMappedTable:from_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>filename:  str,<br>replays = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:__getstate__' href='parser/test3/table.py#L166'>MemoryMappedTable:__getstate__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:__setstate__' href='parser/test3/table.py#L181'>MemoryMappedTable:__setstate__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>state,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:_apply_replays' href='parser/test3/table.py#L465'>MemoryMappedTable:_apply_replays</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>table:  pa.Table,<br>replays:  Optional[List[Replay]]  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:_append_replay' href='parser/test3/table.py#L471'>MemoryMappedTable:_append_replay</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>replay:  Replay,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:slice' href='parser/test3/table.py#L373'>MemoryMappedTable:slice</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>offset = 0,<br>length = None,<br></ul>
        <li>Docs:<br>    """
<br>
    The table is said memory mapped when it doesn't use the user's RAM but loads the data
<br>
    from the disk instead.
<br>

<br>
    Pickling it doesn't copy the data into memory.
<br>
    Instead, only the path to the memory mapped arrow file is pickled, as well as the list
<br>
    of transforms to "replay" when reloading the table from the disk.
<br>

<br>
    Its implementation requires to store an history of all the transforms that were applied
<br>
    to the underlying pyarrow Table, so that they can be "replayed" when reloading the Table
<br>
    from the disk.
<br>

<br>
    This is different from the InMemoryTable table, for which pickling does copy all the
<br>
    data in memory.
<br>

<br>
    InMemoryTable must be used when data fit in memory, while MemoryMapped are reserved for
<br>
    data bigger than memory or when you want the memory footprint of your application to
<br>
    stay low.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:filter' href='parser/test3/table.py#L277'>MemoryMappedTable:filter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:flatten' href='parser/test3/table.py#L281'>MemoryMappedTable:flatten</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:combine_chunks' href='parser/test3/table.py#L285'>MemoryMappedTable:combine_chunks</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:cast' href='parser/test3/table.py#L289'>MemoryMappedTable:cast</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:add_column' href='parser/test3/table.py#L293'>MemoryMappedTable:add_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:append_column' href='parser/test3/table.py#L297'>MemoryMappedTable:append_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:remove_column' href='parser/test3/table.py#L301'>MemoryMappedTable:remove_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:set_column' href='parser/test3/table.py#L305'>MemoryMappedTable:set_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:rename_columns' href='parser/test3/table.py#L309'>MemoryMappedTable:rename_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:MemoryMappedTable:drop' href='parser/test3/table.py#L313'>MemoryMappedTable:drop</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:__init__' href='parser/test3/table.py#L574'>ConcatenationTable:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>table:  pa.Table,<br>blocks:  List[List[TableBlock]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:__getstate__' href='parser/test3/table.py#L166'>ConcatenationTable:__getstate__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:__setstate__' href='parser/test3/table.py#L181'>ConcatenationTable:__setstate__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>state,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:_concat_blocks' href='parser/test3/table.py#L596'>ConcatenationTable:_concat_blocks</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>blocks:  List[Union[TableBlock,<br>pa.Table]],<br>axis:  int  =  0,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:_concat_blocks_horizontally_and_vertically' href='parser/test3/table.py#L620'>ConcatenationTable:_concat_blocks_horizontally_and_vertically</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>blocks:  List[List[TableBlock]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:_merge_blocks' href='parser/test3/table.py#L630'>ConcatenationTable:_merge_blocks</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>blocks:  TableBlockContainer,<br>axis:  Optional[int]  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:_consolidate_blocks' href='parser/test3/table.py#L646'>ConcatenationTable:_consolidate_blocks</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>blocks:  TableBlockContainer,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:from_blocks' href='parser/test3/table.py#L655'>ConcatenationTable:from_blocks</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>blocks:  TableBlockContainer,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:from_tables' href='parser/test3/table.py#L669'>ConcatenationTable:from_tables</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>tables:  List[Union[pa.Table,<br>Table]],<br>axis:  int  =  0,<br></ul>
        <li>Docs:<br>        """Create ConcatenationTable from list of tables.
<br>

<br>
        Args:
<br>
            tables (list of :class:`Table` or list of :obj:`pyarrow.Table`): List of tables.
<br>
            axis: (``{0, 1}``, default ``0``, meaning over rows):
<br>
            Axis to concatenate over, where ``0`` means over rows (vertically) and ``1`` means over columns
<br>
            (horizontally).
<br>

<br>
            .. versionadded:: 1.6.0
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:_slices' href='parser/test3/table.py#L720'>ConcatenationTable:_slices</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:slice' href='parser/test3/table.py#L373'>ConcatenationTable:slice</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>offset = 0,<br>length = None,<br></ul>
        <li>Docs:<br>    """
<br>
    The table is said memory mapped when it doesn't use the user's RAM but loads the data
<br>
    from the disk instead.
<br>

<br>
    Pickling it doesn't copy the data into memory.
<br>
    Instead, only the path to the memory mapped arrow file is pickled, as well as the list
<br>
    of transforms to "replay" when reloading the table from the disk.
<br>

<br>
    Its implementation requires to store an history of all the transforms that were applied
<br>
    to the underlying pyarrow Table, so that they can be "replayed" when reloading the Table
<br>
    from the disk.
<br>

<br>
    This is different from the InMemoryTable table, for which pickling does copy all the
<br>
    data in memory.
<br>

<br>
    InMemoryTable must be used when data fit in memory, while MemoryMapped are reserved for
<br>
    data bigger than memory or when you want the memory footprint of your application to
<br>
    stay low.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:filter' href='parser/test3/table.py#L747'>ConcatenationTable:filter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>mask,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:flatten' href='parser/test3/table.py#L281'>ConcatenationTable:flatten</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:combine_chunks' href='parser/test3/table.py#L285'>ConcatenationTable:combine_chunks</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br>    """
<br>
    TableBlock is the allowed class inside a ConcanetationTable.
<br>
    Only MemoryMappedTable and InMemoryTable are TableBlock.
<br>
    This is because we don't want a ConcanetationTable made out of other ConcanetationTables.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:cast' href='parser/test3/table.py#L772'>ConcatenationTable:cast</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>target_schema,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:add_column' href='parser/test3/table.py#L293'>ConcatenationTable:add_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:append_column' href='parser/test3/table.py#L297'>ConcatenationTable:append_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:remove_column' href='parser/test3/table.py#L796'>ConcatenationTable:remove_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>i,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:set_column' href='parser/test3/table.py#L305'>ConcatenationTable:set_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:rename_columns' href='parser/test3/table.py#L814'>ConcatenationTable:rename_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>names,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/table.py:ConcatenationTable:drop' href='parser/test3/table.py#L825'>ConcatenationTable:drop</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>columns,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/arrow_writer.py' href='parser/test3/arrow_writer.py'>parser/test3/arrow_writer.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_writer.py:parquet_to_arrow' href='parser/test3/arrow_writer.py#L536'>parquet_to_arrow</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>sources,<br>destination,<br></ul>
        <li>Docs:<br>    """Convert parquet files to arrow file. Inputs can be str paths or file-like objects"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_writer.py:TypedSequence' href='parser/test3/arrow_writer.py#L39'>TypedSequence</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_writer.py:OptimizedTypedSequence' href='parser/test3/arrow_writer.py#L136'>OptimizedTypedSequence</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_writer.py:ArrowWriter' href='parser/test3/arrow_writer.py#L149'>ArrowWriter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_writer.py:BeamWriter' href='parser/test3/arrow_writer.py#L436'>BeamWriter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:TypedSequence:__init__' href='parser/test3/arrow_writer.py#L79'>TypedSequence:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data,<br>type = None,<br>try_type = None,<br>optimized_int_type = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:TypedSequence:__arrow_array__' href='parser/test3/arrow_writer.py#L86'>TypedSequence:__arrow_array__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>type = None,<br></ul>
        <li>Docs:<br>        """This function is called when calling pa.array(typed_sequence)"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:OptimizedTypedSequence:__init__' href='parser/test3/arrow_writer.py#L137'>OptimizedTypedSequence:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data,<br>type = None,<br>try_type = None,<br>col = None,<br>optimized_int_type = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:__init__' href='parser/test3/arrow_writer.py#L152'>ArrowWriter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>schema:  Optional[pa.Schema]  =  None,<br>features:  Optional[Features]  =  None,<br>path:  Optional[str]  =  None,<br>stream:  Optional[pa.NativeFile]  =  None,<br>fingerprint:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  None,<br>hash_salt:  Optional[str]  =  None,<br>check_duplicates:  Optional[bool]  =  False,<br>disable_nullable:  bool  =  False,<br>update_features:  bool  =  False,<br>with_metadata:  bool  =  True,<br>unit:  str  =  "examples",<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:__len__' href='parser/test3/arrow_writer.py#L212'>ArrowWriter:__len__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Return the number of writed and staged examples"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:__enter__' href='parser/test3/arrow_writer.py#L216'>ArrowWriter:__enter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:__exit__' href='parser/test3/arrow_writer.py#L219'>ArrowWriter:__exit__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>exc_type,<br>exc_val,<br>exc_tb,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:close' href='parser/test3/arrow_writer.py#L222'>ArrowWriter:close</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:_build_writer' href='parser/test3/arrow_writer.py#L232'>ArrowWriter:_build_writer</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>inferred_schema:  pa.Schema,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:schema' href='parser/test3/arrow_writer.py#L256'>ArrowWriter:schema</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:_build_metadata' href='parser/test3/arrow_writer.py#L260'>ArrowWriter:_build_metadata</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>info:  DatasetInfo,<br>fingerprint:  Optional[str]  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:write_examples_on_file' href='parser/test3/arrow_writer.py#L269'>ArrowWriter:write_examples_on_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Write stored examples from the write-pool of examples. It makes a table out of the examples and write it."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:write_rows_on_file' href='parser/test3/arrow_writer.py#L308'>ArrowWriter:write_rows_on_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Write stored rows from the write-pool of rows. It concatenates the single-row tables and it writes the resulting table."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:write' href='parser/test3/arrow_writer.py#L316'>ArrowWriter:write</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:check_duplicate_keys' href='parser/test3/arrow_writer.py#L349'>ArrowWriter:check_duplicate_keys</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Raises error if duplicates found in a batch"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:write_row' href='parser/test3/arrow_writer.py#L358'>ArrowWriter:write_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Add a given single-row Table to the write-pool of rows which is written to file.
<br>

<br>
        Args:
<br>
            row: the row to add.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:write_batch' href='parser/test3/arrow_writer.py#L370'>ArrowWriter:write_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>batch_examples:  Dict[str,<br>List[Any]],<br>writer_batch_size:  Optional[int]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Write a batch of Example to file.
<br>

<br>
        Args:
<br>
            example: the Example to add.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:write_table' href='parser/test3/arrow_writer.py#L391'>ArrowWriter:write_table</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br>writer_batch_size:  Optional[int]  =  None,<br></ul>
        <li>Docs:<br>        """Write a Table to file.
<br>

<br>
        Args:
<br>
            example: the Table to add.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:ArrowWriter:finalize' href='parser/test3/arrow_writer.py#L410'>ArrowWriter:finalize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>close_stream = True,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:BeamWriter:__init__' href='parser/test3/arrow_writer.py#L152'>BeamWriter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>features:  Optional[Features]  =  None,<br>schema:  Optional[pa.Schema]  =  None,<br>path:  Optional[str]  =  None,<br>namespace:  Optional[str]  =  None,<br>cache_dir:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:BeamWriter:write_from_pcollection' href='parser/test3/arrow_writer.py#L468'>BeamWriter:write_from_pcollection</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pcoll_examples,<br></ul>
        <li>Docs:<br>        """Add the final steps of the beam pipeline: write to parquet files."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_writer.py:BeamWriter:finalize' href='parser/test3/arrow_writer.py#L490'>BeamWriter:finalize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>metrics_query_result:  dict,<br></ul>
        <li>Docs:<br>        """
<br>
        Run after the pipeline has finished.
<br>
        It converts the resulting parquet files to arrow and it completes the info from the pipeline metrics.
<br>

<br>
        Args:
<br>
            metrics_query_result: `dict` obtained from pipeline_results.metrics().query(m_filter). Make sure
<br>
                that the filter keeps only the metrics for the considered split, under the namespace `split_name`.
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/commands/__init__.py' href='parser/test3/commands/__init__.py'>parser/test3/commands/__init__.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/commands/__init__.py:BaseDatasetsCLICommand' href='parser/test3/commands/__init__.py#L5'>BaseDatasetsCLICommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/__init__.py:BaseDatasetsCLICommand:register_subcommand' href='parser/test3/commands/__init__.py#L8'>BaseDatasetsCLICommand:register_subcommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>parser:  ArgumentParser,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/__init__.py:BaseDatasetsCLICommand:run' href='parser/test3/commands/__init__.py#L12'>BaseDatasetsCLICommand:run</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/code_parser.py' href='parser/code_parser.py'>parser/code_parser.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_function_name' href='parser/code_parser.py#L23'>get_list_function_name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The function use to get all functions of the python file
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: list_functions   - List all python functions in the input file
<br>
    Example Output:
<br>
        ['func1', 'func2']
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_class_name' href='parser/code_parser.py#L45'>get_list_class_name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The function use to get all classes of the python file
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: list_classes     - List all python classes in the input file
<br>
    Example Output:
<br>
        ['Class1', 'Class1']
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_class_methods' href='parser/code_parser.py#L70'>get_list_class_methods</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The function use to get all classes and all methods in this class of the python file
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: An array of class info [{dict}, {dict}, ...]
<br>
    Example Output:
<br>
    [
<br>
        {"class_name": "Class1", "listMethods": ["method1", "method2", "method3"]},
<br>
        {"class_name": "Class2", "listMethods": ["method4", "method5", "method6"]},
<br>
    ]
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_variable_global' href='parser/code_parser.py#L102'>get_list_variable_global</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The function use to get all global variable of the python file
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: list_var         - Array of all global variable
<br>
    Example Output:
<br>
        ['Var1', 'Var2']
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_docs' href='parser/code_parser.py#L124'>_get_docs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>all_lines,<br>index_1,<br>func_lines,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_function_info' href='parser/code_parser.py#L164'>get_list_function_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The function use to get functions stars
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: Array of functions, lines of the function, and variable in function
<br>
    Example Output:
<br>
        [
<br>
            {"name": "function_name1", "lines": 20, "variables": ["a", "b", "c"]},
<br>
            {"name": "function_name2", "lines": 30, "variables": []},
<br>
        ]
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_class_info' href='parser/code_parser.py#L202'>get_list_class_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The class use to get functions stars
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: Array of functions, lines of the function, and variable in function
<br>
    Example Output:
<br>
        [
<br>
            {"function": "function_name1", "lines": 20, "variables": ["a", "b", "c"]},
<br>
            {"function": "function_name2", "lines": 30, "variables": []},
<br>
        ]
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_method_info' href='parser/code_parser.py#L238'>get_list_method_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """get_list_method_info
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: Array of methods in class
<br>
    Example Output:
<br>
        [
<br>
            {"function": "function_name1", "lines": 20, "variables": ["a", "b", "c"]},
<br>
            {"function": "function_name2", "lines": 30, "variables": []},
<br>
        ]
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_method_stats' href='parser/code_parser.py#L280'>get_list_method_stats</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The function use to get methods stars
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: Dataframe with bellow fields
<br>
            uri:   path1/path2/filename.py:function1
<br>
            name: function1
<br>
            n_lines
<br>
            n_words
<br>
            n_words_unqiue
<br>
            n_characters
<br>
            avg_char_per_word = n_charaecter / n_words
<br>
            n_loop  : nb of for, while loop
<br>
            n_ifthen  : nb of if_then
<br>
        
<br>
        **** return None if no function in file
<br>
    Example Output:
<br>
                                                    uri                                               name    type  n_variable  n_words  n_words_unique  n_characters  avg_char_per_word  n_loop  n_ifthen
<br>
    0   d:/Project/job/test2/zz936/parser/test/keys.py...                              VerifyingKey:__init__  method           2       11              11           100           9.090909       0         1      
<br>
    1   d:/Project/job/test2/zz936/parser/test/keys.py...                     VerifyingKey:from_public_point  method          10       13              12           185          14.230769       0         0      
<br>
    2   d:/Project/job/test2/zz936/parser/test/keys.py...                           VerifyingKey:from_string  method          17       45              39           504          11.200000       0         1      
<br>
    3   d:/Project/job/test2/zz936/parser/test/keys.py...                              VerifyingKey:from_pem  method           2        2               2            39          19.500000       0         0      
<br>
    4   d:/Project/job/test2/zz936/parser/test/keys.py...                              VerifyingKey:from_der  method          19       64              38           683          10.671875       0         3      
<br>
    5   d:/Project/job/test2/zz936/parser/test/keys.py...              VerifyingKey:from_public_key_recovery  method           4        8               8           137          17.125000       0         0      
<br>
    6   d:/Project/job/test2/zz936/parser/test/keys.py...  VerifyingKey:from_public_key_recovery_with_digest  method          13       24              23           288          12.000000       0         0      
<br>
    7   d:/Project/job/test2/zz936/parser/test/keys.py...                             VerifyingKey:to_string  method           6       11               8           145          13.181818       0         0      
<br>
    8   d:/Project/job/test2/zz936/parser/test/keys.py...                                VerifyingKey:to_pem  method           2        4               4            42          10.500000       0         0  
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_class_stats' href='parser/code_parser.py#L316'>get_list_class_stats</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The class use to get functions stars
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: Dataframe with bellow fields
<br>
            uri:   path1/path2/filename.py:function1
<br>
            name: function1
<br>
            n_lines
<br>
            n_words
<br>
            n_words_unqiue
<br>
            n_characters
<br>
            avg_char_per_word = n_charaecter / n_words
<br>
            n_loop  : nb of for, while loop
<br>
            n_ifthen  : nb of if_then
<br>
        
<br>
        **** return None if no function in file
<br>
    Example Output:
<br>
                                                    uri               name   type  n_variable  n_words  n_words_unique  n_characters  avg_char_per_word  n_loop  n_ifthen
<br>
    0  d:/Project/job/test2/zz936/parser/test/keys.py...  BadSignatureError  class           0        1               1             4           4.000000       0         0
<br>
    1  d:/Project/job/test2/zz936/parser/test/keys.py...     BadDigestError  class           0        1               1             4           4.000000       0         0
<br>
    2  d:/Project/job/test2/zz936/parser/test/keys.py...       VerifyingKey  class          84      301             189          3584          11.906977       0         7
<br>
    3  d:/Project/job/test2/zz936/parser/test/keys.py...         SigningKey  class         138      482             310          4615           9.574689       3         9
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_list_function_stats' href='parser/code_parser.py#L347'>get_list_function_stats</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The function use to get functions stars
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: Dataframe with bellow fields
<br>
            uri:   path1/path2/filename.py:function1
<br>
            name: function1
<br>
            n_lines
<br>
            n_words
<br>
            n_words_unqiue
<br>
            n_characters
<br>
            avg_char_per_word = n_charaecter / n_words
<br>
            n_loop  : nb of for, while loop
<br>
            n_ifthen  : nb of if_then
<br>
        
<br>
        **** return None if no function in file
<br>
    Example Output:
<br>
            uri                                 name  n_variable  n_words  n_words_unique  n_characters  avg_char_per_word  n_loop  n_ifthen
<br>
        0   d:\Project\job\test2\zz936\parser/test/test2.p...     prepare_target_and_clean_up_test           8       92              32           535           5.815217       0         0
<br>
        1   d:\Project\job\test2\zz936\parser/test/test2.p...                 clean_up_config_test           6       55              19           241           4.381818       0         1
<br>
        2   d:\Project\job\test2\zz936\parser/test/test2.p...         check_default_network_config          22      388              74           955           2.461340       1         5
<br>
        3   d:\Project\job\test2\zz936\parser/test/test2.p...                     check_module_env           9      250              54           553           2.212000       1         1
<br>
        4   d:\Project\job\test2\zz936\parser/test/test2.p...     provision_certificates_to_target           7      101              29           384           3.801980       0         3
<br>
        5   d:\Project\job\test2\zz936\parser/test/test2.p...            config_session_connection           2       14               8            97           6.928571       0         0
<br>
        6   d:\Project\job\test2\zz936\parser/test/test2.p...  config_cipher_suite_and_tcps_action           8      101              30           335           3.316832       0         3
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_stats' href='parser/code_parser.py#L383'>get_stats</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>df: pd.DataFrame,<br>file_path: str,<br></ul>
        <li>Docs:<br>    """ Calculate stats from datafaframe
<br>
    Args:
<br>
        df: pandas DataFrame
<br>

<br>
    Returns:
<br>
        pandas DataFrame
<br>

<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:get_file_stats' href='parser/code_parser.py#L412'>get_file_stats</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """The function use to get file stars
<br>
    Args:
<br>
        IN: file_path         - the file path input
<br>
        OUT: Dict of file stars
<br>
    Example Output:
<br>
        {
<br>
            "total_functions": 22,
<br>
            "avg_lines" : 110.2,
<br>
            "total_class": 3
<br>
        }
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_words' href='parser/code_parser.py#L440'>_get_words</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>row,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_avg_char_per_word' href='parser/code_parser.py#L450'>_get_avg_char_per_word</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>row,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_validate_file' href='parser/code_parser.py#L454'>_validate_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """Check if the file is existed and it's a python file
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_clean_data' href='parser/code_parser.py#L469'>_clean_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>array,<br></ul>
        <li>Docs:<br>    """Remove empty lines and comment lines start with #
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_remove_empty_line' href='parser/code_parser.py#L512'>_remove_empty_line</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>line,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_remmove_commemt_line' href='parser/code_parser.py#L516'>_remmove_commemt_line</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>line,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_and_clean_all_lines' href='parser/code_parser.py#L522'>_get_and_clean_all_lines</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br>    """Prepare all lines of the file
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_all_line' href='parser/code_parser.py#L532'>_get_all_line</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_all_lines_in_function' href='parser/code_parser.py#L538'>_get_all_lines_in_function</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>function_name,<br>array,<br>indentMethod = '',<br></ul>
        <li>Docs:<br>    """The function use to get all lines of the function
<br>
    Args:
<br>
        IN: function_name - name of the function will be used to get all line
<br>
        IN: array         - list all lines of the file have this input function
<br>
        OUT: list_lines   - Array of all line of this function
<br>
        OUT: indent       - The indent of this function (this will be used for another calculation)
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_all_lines_in_class' href='parser/code_parser.py#L583'>_get_all_lines_in_class</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>class_name,<br>array,<br></ul>
        <li>Docs:<br>    """The function use to get all lines of the class
<br>
    Args:
<br>
        IN: class_name    - name of the class will be used to get all line
<br>
        IN: array         - list all lines of the file have this input class
<br>
        OUT: list_lines   - Array of all line of this class
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_all_lines_define_function' href='parser/code_parser.py#L622'>_get_all_lines_define_function</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>function_name,<br>array,<br>indentMethod = '',<br></ul>
        <li>Docs:<br>    """The function use to get all lines define_function
<br>
    Args:
<br>
        IN: function_name - name of the function will be used to get all line
<br>
        IN: array         - list all lines of the file have this input function
<br>
        OUT: list_lines   - Array of all line used to define the function
<br>
        OUT: indent       - The indent of this function (this will be used for another calculation)
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_define_function_stats' href='parser/code_parser.py#L659'>_get_define_function_stats</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>array,<br></ul>
        <li>Docs:<br>    """The function use to get define function stats: arg_name, arg_type, arg_value
<br>
    Args:
<br>
        IN: array         - list all lines of function to get variables
<br>
        OUT: function stats: arg_name, arg_type, arg_value
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:_get_function_stats' href='parser/code_parser.py#L720'>_get_function_stats</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>array,<br>indent,<br></ul>
        <li>Docs:<br>    """The function use to get all lines of the function
<br>
    Args:
<br>
        IN: indent        - indent string
<br>
        IN: array         - list all lines of function to get variables
<br>
        OUT: list_var     - Array of all variables
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:export_stats_pertype' href='parser/code_parser.py#L809'>export_stats_pertype</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>in_path: str = None,<br>type: str = None,<br>out_path: str = None,<br></ul>
        <li>Docs:<br>    """
<br>
        python code_parser.py type <in_path> <type> <out_path>
<br>
    Returns:
<br>

<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:export_stats_perfile' href='parser/code_parser.py#L835'>export_stats_perfile</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>in_path: str = None,<br>out_path: str = None,<br></ul>
        <li>Docs:<br>    """
<br>
        python code_parser.py  export_stats_perfile <in_path> <out_path>
<br>

<br>
    Returns:
<br>

<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:export_stats_perrepo' href='parser/code_parser.py#L859'>export_stats_perrepo</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>in_path: str = None,<br>out_path: str = None,<br></ul>
        <li>Docs:<br>    """ 
<br>
        python code_parser.py  export_stats_perfile <in_path> <out_path>
<br>

<br>
    Returns:
<br>
        1  repo   --->  a single file stats for all sub-diractory
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/code_parser.py:test_example' href='parser/code_parser.py#L895'>test_example</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/formatting/torch_formatter.py' href='parser/test3/formatting/torch_formatter.py'>parser/test3/formatting/torch_formatter.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/torch_formatter.py:TorchFormatter' href='parser/test3/formatting/torch_formatter.py#L30'>TorchFormatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/torch_formatter.py:TorchFormatter:__init__' href='parser/test3/formatting/torch_formatter.py#L31'>TorchFormatter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>**torch_tensor_kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/torch_formatter.py:TorchFormatter:_tensorize' href='parser/test3/formatting/torch_formatter.py#L35'>TorchFormatter:_tensorize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/torch_formatter.py:TorchFormatter:_recursive_tensorize' href='parser/test3/formatting/torch_formatter.py#L46'>TorchFormatter:_recursive_tensorize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data_struct:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/torch_formatter.py:TorchFormatter:recursive_tensorize' href='parser/test3/formatting/torch_formatter.py#L54'>TorchFormatter:recursive_tensorize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data_struct:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/torch_formatter.py:TorchFormatter:format_row' href='parser/test3/formatting/torch_formatter.py#L57'>TorchFormatter:format_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/torch_formatter.py:TorchFormatter:format_column' href='parser/test3/formatting/torch_formatter.py#L61'>TorchFormatter:format_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/torch_formatter.py:TorchFormatter:format_batch' href='parser/test3/formatting/torch_formatter.py#L65'>TorchFormatter:format_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/io/parquet.py' href='parser/test3/io/parquet.py'>parser/test3/io/parquet.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/io/parquet.py:ParquetDatasetReader' href='parser/test3/io/parquet.py#L16'>ParquetDatasetReader</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/io/parquet.py:ParquetDatasetWriter' href='parser/test3/io/parquet.py#L66'>ParquetDatasetWriter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/parquet.py:ParquetDatasetReader:__init__' href='parser/test3/io/parquet.py#L17'>ParquetDatasetReader:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_paths:  NestedDataStructureLike[PathLike],<br>split:  Optional[NamedSplit]  =  None,<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/parquet.py:ParquetDatasetReader:read' href='parser/test3/io/parquet.py#L43'>ParquetDatasetReader:read</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/parquet.py:ParquetDatasetWriter:__init__' href='parser/test3/io/parquet.py#L17'>ParquetDatasetWriter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset:  Dataset,<br>path_or_buf:  Union[PathLike,<br>BinaryIO],<br>batch_size:  Optional[int]  =  None,<br>**parquet_writer_kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/parquet.py:ParquetDatasetWriter:write' href='parser/test3/io/parquet.py#L83'>ParquetDatasetWriter:write</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/parquet.py:ParquetDatasetWriter:_write' href='parser/test3/io/parquet.py#L93'>ParquetDatasetWriter:_write</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>file_obj:  BinaryIO,<br>batch_size:  int,<br>**parquet_writer_kwargs,<br></ul>
        <li>Docs:<br>        """Writes the pyarrow table as Parquet to a binary file handle.
<br>

<br>
        Caller is responsible for opening and closing the handle.
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/arrow_dataset.py' href='parser/test3/arrow_dataset.py'>parser/test3/arrow_dataset.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_dataset.py:transmit_format' href='parser/test3/arrow_dataset.py#L166'>transmit_format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>func,<br></ul>
        <li>Docs:<br>    """Wrapper for dataset transforms that recreate a new Dataset to transmit the format of the original dataset to the new dataset"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_dataset.py:update_metadata_with_features' href='parser/test3/arrow_dataset.py#L207'>update_metadata_with_features</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>table:  Table,<br>features:  Features,<br></ul>
        <li>Docs:<br>    """To be used in dataset transforms that modify the features of the dataset, in order to update the features stored in the metadata of its schema."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_dataset.py:_check_table' href='parser/test3/arrow_dataset.py#L223'>_check_table</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>table,<br></ul>
        <li>Docs:<br>    """We check the table type to make sure it's an instance of :class:`datasets.table.Table`"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_dataset.py:concatenate_datasets' href='parser/test3/arrow_dataset.py#L3228'>concatenate_datasets</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dsets:  List[Dataset],<br>info:  Optional[Any]  =  None,<br>split:  Optional[Any]  =  None,<br>axis:  int  =  0,<br>,<br></ul>
        <li>Docs:<br>    """
<br>
    Converts a list of :class:`Dataset` with the same schema into a single :class:`Dataset`.
<br>

<br>
    Args:
<br>
        dsets (:obj:`List[datasets.Dataset]`): List of Datasets to concatenate.
<br>
        info (:class:`DatasetInfo`, optional): Dataset information, like description, citation, etc.
<br>
        split (:class:`NamedSplit`, optional): Name of the dataset split.
<br>
        axis (``{0, 1}``, default ``0``, meaning over rows):
<br>
            Axis to concatenate over, where ``0`` means over rows (vertically) and ``1`` means over columns
<br>
            (horizontally).
<br>

<br>
            .. versionadded:: 1.6.0
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_dataset.py:map_function' href='parser/test3/arrow_dataset.py#L3319'>map_function</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>batch,<br>*args,<br>function = None,<br>with_indices = None,<br>**fn_kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin' href='parser/test3/arrow_dataset.py#L90'>DatasetInfoMixin</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_dataset.py:DatasetTransformationNotAllowedError' href='parser/test3/arrow_dataset.py#L162'>DatasetTransformationNotAllowedError</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_dataset.py:Dataset' href='parser/test3/arrow_dataset.py#L235'>Dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:__init__' href='parser/test3/arrow_dataset.py#L95'>DatasetInfoMixin:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>info:  DatasetInfo,<br>split:  Optional[NamedSplit],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:info' href='parser/test3/arrow_dataset.py#L100'>DatasetInfoMixin:info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """:class:`datasets.DatasetInfo` object containing all the metadata in the dataset."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:split' href='parser/test3/arrow_dataset.py#L105'>DatasetInfoMixin:split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """:class:`datasets.NamedSplit` object corresponding to a named dataset split."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:builder_name' href='parser/test3/arrow_dataset.py#L110'>DatasetInfoMixin:builder_name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:citation' href='parser/test3/arrow_dataset.py#L114'>DatasetInfoMixin:citation</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:config_name' href='parser/test3/arrow_dataset.py#L118'>DatasetInfoMixin:config_name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:dataset_size' href='parser/test3/arrow_dataset.py#L122'>DatasetInfoMixin:dataset_size</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:description' href='parser/test3/arrow_dataset.py#L126'>DatasetInfoMixin:description</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:download_checksums' href='parser/test3/arrow_dataset.py#L130'>DatasetInfoMixin:download_checksums</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:download_size' href='parser/test3/arrow_dataset.py#L134'>DatasetInfoMixin:download_size</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:features' href='parser/test3/arrow_dataset.py#L138'>DatasetInfoMixin:features</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:homepage' href='parser/test3/arrow_dataset.py#L142'>DatasetInfoMixin:homepage</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:license' href='parser/test3/arrow_dataset.py#L146'>DatasetInfoMixin:license</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:size_in_bytes' href='parser/test3/arrow_dataset.py#L150'>DatasetInfoMixin:size_in_bytes</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:supervised_keys' href='parser/test3/arrow_dataset.py#L154'>DatasetInfoMixin:supervised_keys</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:DatasetInfoMixin:version' href='parser/test3/arrow_dataset.py#L158'>DatasetInfoMixin:version</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:__init__' href='parser/test3/arrow_dataset.py#L238'>Dataset:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>arrow_table:  Table,<br>info:  Optional[DatasetInfo]  =  None,<br>split:  Optional[NamedSplit]  =  None,<br>indices_table:  Optional[Table]  =  None,<br>fingerprint:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:from_file' href='parser/test3/arrow_dataset.py#L310'>Dataset:from_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>filename:  str,<br>info:  Optional[DatasetInfo]  =  None,<br>split:  Optional[NamedSplit]  =  None,<br>indices_filename:  Optional[str]  =  None,<br>in_memory:  bool  =  False,<br>,<br></ul>
        <li>Docs:<br>        """Instantiate a Dataset backed by an Arrow table at filename.
<br>

<br>
        Args:
<br>
            filename (:obj:`str`): File name of the dataset.
<br>
            info (:class:`DatasetInfo`, optional): Dataset information, like description, citation, etc.
<br>
            split (:class:`NamedSplit`, optional): Name of the dataset split.
<br>
            indices_filename (:obj:`str`, optional): File names of the indices.
<br>
            in_memory (:obj:`bool`, default ``False``): Whether to copy the data in-memory.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:from_buffer' href='parser/test3/arrow_dataset.py#L345'>Dataset:from_buffer</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>buffer:  pa.Buffer,<br>info:  Optional[DatasetInfo]  =  None,<br>split:  Optional[NamedSplit]  =  None,<br>indices_buffer:  Optional[pa.Buffer]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Instantiate a Dataset backed by an Arrow buffer.
<br>

<br>
        Args:
<br>
            buffer (:obj:`pyarrow.Buffer`): Arrow buffer.
<br>
            info (:class:`DatasetInfo`, optional): Dataset information, like description, citation, etc.
<br>
            split (:class:`NamedSplit`, optional): Name of the dataset split.
<br>
            indices_buffer (:obj:`pyarrow.Buffer`, optional): Indices Arrow buffer.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:from_pandas' href='parser/test3/arrow_dataset.py#L373'>Dataset:from_pandas</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>df:  pd.DataFrame,<br>features:  Optional[Features]  =  None,<br>info:  Optional[DatasetInfo]  =  None,<br>split:  Optional[NamedSplit]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """
<br>
        Convert :obj:`pandas.DataFrame` to a :obj:`pyarrow.Table` to create a :class:`Dataset`.
<br>

<br>
        The column types in the resulting Arrow Table are inferred from the dtypes of the pandas.Series in the
<br>
        DataFrame. In the case of non-object Series, the NumPy dtype is translated to its Arrow equivalent. In the
<br>
        case of `object`, we need to guess the datatype by looking at the Python objects in this Series.
<br>

<br>
        Be aware that Series of the `object` dtype don't carry enough information to always lead to a meaningful Arrow
<br>
        type. In the case that we cannot infer a type, e.g. because the DataFrame is of length 0 or the Series only
<br>
        contains None/nan objects, the type is set to null. This behavior can be avoided by constructing explicit
<br>
        features and passing it to this function.
<br>

<br>
        Args:
<br>
            df (:obj:`pandas.DataFrame`): Dataframe that contains the dataset.
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            info (:class:`DatasetInfo`, optional): Dataset information, like description, citation, etc.
<br>
            split (:class:`NamedSplit`, optional): Name of the dataset split.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:from_dict' href='parser/test3/arrow_dataset.py#L415'>Dataset:from_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>mapping:  dict,<br>features:  Optional[Features]  =  None,<br>info:  Optional[Any]  =  None,<br>split:  Optional[Any]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """
<br>
        Convert :obj:`dict` to a :obj:`pyarrow.Table` to create a :class:`Dataset`.
<br>

<br>
        Args:
<br>
            mapping (:obj:`Mapping`): Mapping of strings to Arrays or Python lists.
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            info (:class:`DatasetInfo`, optional): Dataset information, like description, citation, etc.
<br>
            split (:class:`NamedSplit`, optional): Name of the dataset split.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:from_csv' href='parser/test3/arrow_dataset.py#L456'>Dataset:from_csv</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path_or_paths:  Union[PathLike,<br>List[PathLike]],<br>split:  Optional[NamedSplit]  =  None,<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Create Dataset from CSV file(s).
<br>

<br>
        Args:
<br>
            path_or_paths (path-like or list of path-like): Path(s) of the CSV file(s).
<br>
            split (:class:`NamedSplit`, optional): Split name to be assigned to the dataset.
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            cache_dir (:obj:`str`, optional, default ``"~/.cache/huggingface/datasets"``): Directory to cache data.
<br>
            keep_in_memory (:obj:`bool`, default ``False``): Whether to copy the data in-memory.
<br>
            **kwargs: Keyword arguments to be passed to :meth:`pandas.read_csv`.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:from_json' href='parser/test3/arrow_dataset.py#L485'>Dataset:from_json</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path_or_paths:  Union[PathLike,<br>List[PathLike]],<br>split:  Optional[NamedSplit]  =  None,<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>field:  Optional[str]  =  None,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Create Dataset from JSON or JSON Lines file(s).
<br>

<br>
        Args:
<br>
            path_or_paths (path-like or list of path-like): Path(s) of the JSON or JSON Lines file(s).
<br>
            split (:class:`NamedSplit`, optional): Split name to be assigned to the dataset.
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            cache_dir (:obj:`str`, optional, default ``"~/.cache/huggingface/datasets"``): Directory to cache data.
<br>
            keep_in_memory (:obj:`bool`, default ``False``): Whether to copy the data in-memory.
<br>
            field (:obj:`str`, optional): Field name of the JSON file where the dataset is contained in.
<br>
            **kwargs: Keyword arguments to be passed to :class:`JsonConfig`.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:from_parquet' href='parser/test3/arrow_dataset.py#L522'>Dataset:from_parquet</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path_or_paths:  Union[PathLike,<br>List[PathLike]],<br>split:  Optional[NamedSplit]  =  None,<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>columns:  Optional[List[str]]  =  None,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Create Dataset from Parquet file(s).
<br>

<br>
        Args:
<br>
            path_or_paths (path-like or list of path-like): Path(s) of the Parquet file(s).
<br>
            split (:class:`NamedSplit`, optional): Split name to be assigned to the dataset.
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            cache_dir (:obj:`str`, optional, default ``"~/.cache/huggingface/datasets"``): Directory to cache data.
<br>
            keep_in_memory (:obj:`bool`, default ``False``): Whether to copy the data in-memory.
<br>
            columns (:obj:`List[str]`, optional): If not None, only these columns will be read from the file.
<br>
                A column name may be a prefix of a nested field, e.g. 'a' will select
<br>
                'a.b', 'a.c', and 'a.d.e'.
<br>
            **kwargs: Keyword arguments to be passed to :class:`ParquetConfig`.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:from_text' href='parser/test3/arrow_dataset.py#L561'>Dataset:from_text</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path_or_paths:  Union[PathLike,<br>List[PathLike]],<br>split:  Optional[NamedSplit]  =  None,<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Create Dataset from text file(s).
<br>

<br>
        Args:
<br>
            path_or_paths (path-like or list of path-like): Path(s) of the text file(s).
<br>
            split (:class:`NamedSplit`, optional): Split name to be assigned to the dataset.
<br>
            features (:class:`Features`, optional): Dataset features.
<br>
            cache_dir (:obj:`str`, optional, default ``"~/.cache/huggingface/datasets"``): Directory to cache data.
<br>
            keep_in_memory (:obj:`bool`, default ``False``): Whether to copy the data in-memory.
<br>
            **kwargs: Keyword arguments to be passed to :class:`TextConfig`.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:__del__' href='parser/test3/arrow_dataset.py#L589'>Dataset:__del__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:__enter__' href='parser/test3/arrow_dataset.py#L595'>Dataset:__enter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:__exit__' href='parser/test3/arrow_dataset.py#L598'>Dataset:__exit__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>exc_type,<br>exc_val,<br>exc_tb,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:save_to_disk' href='parser/test3/arrow_dataset.py#L602'>Dataset:save_to_disk</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_path:  str,<br>fs = None,<br></ul>
        <li>Docs:<br>        """
<br>
        Saves a dataset to a dataset directory, or in a filesystem using either :class:`~filesystems.S3FileSystem` or
<br>
        any implementation of ``fsspec.spec.AbstractFileSystem``.
<br>

<br>

<br>
        Note regarding sliced datasets:
<br>

<br>
        If you sliced the dataset in some way (using shard, train_test_split or select for example), then an indices mapping
<br>
        is added to avoid having to rewrite a new arrow Table (save time + disk/memory usage).
<br>
        It maps the indices used by __getitem__ to the right rows if the arrow Table.
<br>
        By default save_to_disk does save the full dataset table + the mapping.
<br>

<br>
        If you want to only save the shard of the dataset instead of the original arrow file and the indices,
<br>
        then you have to call :func:`datasets.Dataset.flatten_indices` before saving.
<br>
        This will create a new arrow table by using the right rows of the original table.
<br>

<br>
        Args:
<br>
            dataset_path (:obj:`str`): Path (e.g. `dataset/train`) or remote URI (e.g. `s3://my-bucket/dataset/train`)
<br>
                of the dataset directory where the dataset will be saved to.
<br>
            fs (:class:`~filesystems.S3FileSystem`, ``fsspec.spec.AbstractFileSystem``, optional, defaults ``None``):
<br>
                Instance of the remote filesystem used to download the files from.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:load_from_disk' href='parser/test3/arrow_dataset.py#L697'>Dataset:load_from_disk</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset_path:  str,<br>fs = None,<br>keep_in_memory:  Optional[bool]  =  None,<br></ul>
        <li>Docs:<br>        """
<br>
        Loads a dataset that was previously saved using :meth:`save_to_disk` from a dataset directory, or from a
<br>
        filesystem using either :class:`~filesystems.S3FileSystem` or any implementation of
<br>
        ``fsspec.spec.AbstractFileSystem``.
<br>

<br>
        Args:
<br>
            dataset_path (:obj:`str`): Path (e.g. `dataset/train`) or remote URI (e.g. `s3//my-bucket/dataset/train`) of
<br>
                the dataset directory where the dataset will be loaded from.
<br>
            fs (:class:`~filesystems.S3FileSystem`, ``fsspec.spec.AbstractFileSystem``, optional, default ``None``):
<br>
                Instance of the remote filesystem used to download the files from.
<br>
            keep_in_memory (:obj:`bool`, default ``None``): Whether to copy the dataset in-memory. If `None`, the
<br>
                dataset will not be copied in-memory unless explicitly enabled by setting
<br>
                `datasets.config.IN_MEMORY_MAX_SIZE` to nonzero. See more details in the
<br>
                :ref:`load_dataset_enhancing_performance` section.
<br>

<br>
        Returns:
<br>
            :class:`Dataset` or :class:`DatasetDict`.
<br>
                - if `dataset_path` is a path of a dataset directory: the :class:`Dataset` requested,
<br>
                - if `dataset_path` is a path of a dataset dict directory: a :class:`DatasetDict` with each split.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:data' href='parser/test3/arrow_dataset.py#L771'>Dataset:data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """The Apache Arrow table backing the dataset."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:cache_files' href='parser/test3/arrow_dataset.py#L776'>Dataset:cache_files</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """The cache files containing the Apache Arrow table backing the dataset."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:num_columns' href='parser/test3/arrow_dataset.py#L784'>Dataset:num_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Number of columns in the dataset."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:num_rows' href='parser/test3/arrow_dataset.py#L789'>Dataset:num_rows</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Number of rows in the dataset (same as :meth:`Dataset.__len__`)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:column_names' href='parser/test3/arrow_dataset.py#L796'>Dataset:column_names</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Names of the columns in the dataset."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:shape' href='parser/test3/arrow_dataset.py#L801'>Dataset:shape</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Shape of the dataset (number of columns, number of rows)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:unique' href='parser/test3/arrow_dataset.py#L807'>Dataset:unique</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br></ul>
        <li>Docs:<br>        """Return a list of the unique elements in a column.
<br>

<br>
        This is implemented in the low-level backend and as such, very fast.
<br>

<br>
        Args:
<br>
            column (:obj:`str`): Column name (list all the column names with :func:`datasets.Dataset.column_names`).
<br>

<br>
        Returns:
<br>
            :obj:`list`: List of unique elements in the given column.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:class_encode_column' href='parser/test3/arrow_dataset.py#L830'>Dataset:class_encode_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br></ul>
        <li>Docs:<br>        """Casts the given column as :obj:``datasets.features.ClassLabel`` and updates the table.
<br>

<br>
        Args:
<br>
            column (`str`): The name of the column to cast (list all the column names with :func:`datasets.Dataset.column_names`)
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:dictionary_encode_column_' href='parser/test3/arrow_dataset.py#L867'>Dataset:dictionary_encode_column_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br></ul>
        <li>Docs:<br>        """Dictionary encode a column.
<br>

<br>
        Dictionary encode can reduce the size of a column with many repetitions (e.g. string labels columns)
<br>
        by storing a dictionary of the strings. This only affect the internal storage.
<br>

<br>
        .. deprecated:: 1.4.0
<br>

<br>
        Args:
<br>
            column (:obj:`str`):
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:flatten_' href='parser/test3/arrow_dataset.py#L892'>Dataset:flatten_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>max_depth = 16,<br></ul>
        <li>Docs:<br>        """In-place version of :meth:`Dataset.flatten`.
<br>

<br>
        .. deprecated:: 1.4.0
<br>
            Use :meth:`Dataset.flatten` instead.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:flatten' href='parser/test3/arrow_dataset.py#L910'>Dataset:flatten</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>max_depth = 16,<br></ul>
        <li>Docs:<br>        """Flatten the table.
<br>
        Each column with a struct type is flattened into one column per struct field.
<br>
        Other columns are left unchanged.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`: A copy of the dataset with flattened columns.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:cast_' href='parser/test3/arrow_dataset.py#L933'>Dataset:cast_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>features:  Features,<br>batch_size:  Optional[int]  =  10_000,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  10_000,<br>num_proc:  Optional[int]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """In-place version of :meth:`Dataset.cast`.
<br>

<br>
        .. deprecated:: 1.4.0
<br>
            Use :meth:`Dataset.cast` instead.
<br>

<br>
        Args:
<br>
            features (:class:`datasets.Features`): New features to cast the dataset to.
<br>
                The name of the fields in the features must match the current column names.
<br>
                The type of the data must also be convertible from one type to the other.
<br>
                For non-trivial conversion, e.g. string <-> ClassLabel you should use :func:`map` to update the Dataset.
<br>
            batch_size (`Optional[int]`, defaults to `1000`): Number of examples per batch provided to cast.
<br>
                `batch_size <= 0` or `batch_size == None`: Provide the full dataset as a single batch to cast.
<br>
            keep_in_memory (:obj:`bool`, default ``False``): Whether to copy the data in-memory.
<br>
            load_from_cache_file (:obj:`bool`, default `True` if caching is enabled): If a cache file storing the current computation from `function`
<br>
                can be identified, use it instead of recomputing.
<br>
            cache_file_name (`Optional[str]`, default `None`): Provide the name of a path for the cache file. It is used to store the
<br>
                results of the computation instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            num_proc (`Optional[int]`, default `None`): Number of processes for multiprocessing. By default it doesn't
<br>
                use multiprocessing.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:cast' href='parser/test3/arrow_dataset.py#L990'>Dataset:cast</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>features:  Features,<br>batch_size:  Optional[int]  =  10_000,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  10_000,<br>num_proc:  Optional[int]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:remove_columns_' href='parser/test3/arrow_dataset.py#L1050'>Dataset:remove_columns_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column_names:  Union[str,<br>List[str]],<br></ul>
        <li>Docs:<br>        """In-place version of :meth:`Dataset.remove_columns`.
<br>

<br>
        .. deprecated:: 1.4.0
<br>
            Use :meth:`Dataset.remove_columns` instead.
<br>

<br>
        Args:
<br>
            column_names (:obj:`Union[str, List[str]]`): Name of the column(s) to remove.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:remove_columns' href='parser/test3/arrow_dataset.py#L1076'>Dataset:remove_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column_names:  Union[str,<br>List[str]],<br></ul>
        <li>Docs:<br>        """
<br>
        Remove one or several column(s) in the dataset and the features associated to them.
<br>

<br>
        You can also remove a column using :func:`Dataset.map` with `remove_columns` but the present method
<br>
        is in-place (doesn't copy the data to a new dataset) and is thus faster.
<br>

<br>
        Args:
<br>
            column_names (:obj:`Union[str, List[str]]`): Name of the column(s) to remove.
<br>
            new_fingerprint
<br>

<br>
        Returns:
<br>
            :class:`Dataset`: A copy of the dataset object without the columns to remove.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:rename_column_' href='parser/test3/arrow_dataset.py#L1111'>Dataset:rename_column_</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>original_column_name:  str,<br>new_column_name:  str,<br></ul>
        <li>Docs:<br>        """In-place version of :meth:`Dataset.rename_column`.
<br>

<br>
        .. deprecated:: 1.4.0
<br>
            Use :meth:`Dataset.rename_column` instead.
<br>

<br>
        Args:
<br>
            original_column_name (:obj:`str`): Name of the column to rename.
<br>
            new_column_name (:obj:`str`): New name for the column.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:rename_column' href='parser/test3/arrow_dataset.py#L1153'>Dataset:rename_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>original_column_name:  str,<br>new_column_name:  str,<br></ul>
        <li>Docs:<br>        """
<br>
        Rename a column in the dataset, and move the features associated to the original column under the new column
<br>
        name.
<br>

<br>
        Args:
<br>
            original_column_name (:obj:`str`): Name of the column to rename.
<br>
            new_column_name (:obj:`str`): New name for the column.
<br>
            new_fingerprint
<br>

<br>
        Returns:
<br>
            :class:`Dataset`: A copy of the dataset with a renamed column.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:rename_columns' href='parser/test3/arrow_dataset.py#L1201'>Dataset:rename_columns</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column_mapping:  Dict[str,<br>str],<br>new_fingerprint,<br></ul>
        <li>Docs:<br>        """
<br>
        Rename several columns in the dataset, and move the features associated to the original columns under
<br>
        the new column names.
<br>

<br>
        Args:
<br>
            column_mapping (:obj:`Dict[str, str]`): A mapping of columns to rename to their new names
<br>

<br>
        Returns:
<br>
            :class:`Dataset`: A copy of the dataset with renamed columns
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:__len__' href='parser/test3/arrow_dataset.py#L1251'>Dataset:__len__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Number of rows in the dataset."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:__iter__' href='parser/test3/arrow_dataset.py#L1255'>Dataset:__iter__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Iterate through the examples.
<br>

<br>
        If a formatting is set with :meth:`Dataset.set_format` rows will be returned with the
<br>
        selected format.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:__repr__' href='parser/test3/arrow_dataset.py#L1274'>Dataset:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:format' href='parser/test3/arrow_dataset.py#L1278'>Dataset:format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:formatted_as' href='parser/test3/arrow_dataset.py#L1287'>Dataset:formatted_as</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>type:  Optional[str]  =  None,<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>**format_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """To be used in a `with` statement. Set __getitem__ return format (type and columns).
<br>

<br>
        Args:
<br>
            type (Optional ``str``): output type selected in [None, 'numpy', 'torch', 'tensorflow', 'pandas', 'arrow']
<br>
                None means __getitem__ returns python objects (default)
<br>
            columns (Optional ``List[str]``): columns to format in the output
<br>
                None means __getitem__ returns all columns (default)
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
            format_kwargs: keywords arguments passed to the convert function like `np.array`, `torch.tensor` or `tensorflow.ragged.constant`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:set_format' href='parser/test3/arrow_dataset.py#L1315'>Dataset:set_format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>type:  Optional[str]  =  None,<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>**format_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Set __getitem__ return format (type and columns). The data formatting is applied on-the-fly.
<br>
        The format ``type`` (for example "numpy") is used to format batches when using __getitem__.
<br>
        It's also possible to use custom transforms for formatting using :func:`datasets.Dataset.set_transform`.
<br>

<br>
        Args:
<br>
            type (Optional ``str``):
<br>
                Either output type selected in [None, 'numpy', 'torch', 'tensorflow', 'pandas', 'arrow'].
<br>
                None means __getitem__ returns python objects (default)
<br>
            columns (Optional ``List[str]``): columns to format in the output.
<br>
                None means __getitem__ returns all columns (default).
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
            format_kwargs: keywords arguments passed to the convert function like `np.array`, `torch.tensor` or `tensorflow.ragged.constant`.
<br>

<br>
        It is possible to call ``map`` after calling ``set_format``. Since ``map`` may add new columns, then the list of formatted columns
<br>
        gets updated. In this case, if you apply ``map`` on a dataset to add a new column, then this column will be formatted:
<br>

<br>
            new formatted columns = (all columns - previously unformatted columns)
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:reset_format' href='parser/test3/arrow_dataset.py#L1369'>Dataset:reset_format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Reset __getitem__ return format to python objects and all columns.
<br>

<br>
        Same as ``self.set_format()``
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:set_transform' href='parser/test3/arrow_dataset.py#L1376'>Dataset:set_transform</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>transform:  Optional[Callable],<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>,<br></ul>
        <li>Docs:<br>        """Set __getitem__ return format using this transform. The transform is applied on-the-fly on batches when __getitem__ is called.
<br>
        As :func:`datasets.Dataset.set_format`, this can be reset using :func:`datasets.Dataset.reset_format`
<br>

<br>
        Args:
<br>
            transform (Optional ``Callable``): user-defined formatting transform, replaces the format defined by :func:`datasets.Dataset.set_format`
<br>
                A formatting function is a callable that takes a batch (as a dict) as input and returns a batch.
<br>
                This function is applied right before returning the objects in __getitem__.
<br>
            columns (Optional ``List[str]``): columns to format in the output
<br>
                If specified, then the input batch of the transform only contains those columns.
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
                If set to True, then the other un-formatted columns are kept with the output of the transform.
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:with_format' href='parser/test3/arrow_dataset.py#L1397'>Dataset:with_format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>type:  Optional[str]  =  None,<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>**format_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Set __getitem__ return format (type and columns). The data formatting is applied on-the-fly.
<br>
        The format ``type`` (for example "numpy") is used to format batches when using __getitem__.
<br>

<br>
        It's also possible to use custom transforms for formatting using :func:`datasets.Dataset.with_transform`.
<br>

<br>
        Contrary to :func:`datasets.Dataset.set_format`, ``with_format`` returns a new Dataset object.
<br>

<br>
        Args:
<br>
            type (Optional ``str``):
<br>
                Either output type selected in [None, 'numpy', 'torch', 'tensorflow', 'pandas', 'arrow'].
<br>
                None means __getitem__ returns python objects (default)
<br>
            columns (Optional ``List[str]``): columns to format in the output
<br>
                None means __getitem__ returns all columns (default)
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
            format_kwargs: keywords arguments passed to the convert function like `np.array`, `torch.tensor` or `tensorflow.ragged.constant`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:with_transform' href='parser/test3/arrow_dataset.py#L1424'>Dataset:with_transform</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>transform:  Optional[Callable],<br>columns:  Optional[List]  =  None,<br>output_all_columns:  bool  =  False,<br>,<br></ul>
        <li>Docs:<br>        """Set __getitem__ return format using this transform. The transform is applied on-the-fly on batches when __getitem__ is called.
<br>

<br>
        As :func:`datasets.Dataset.set_format`, this can be reset using :func:`datasets.Dataset.reset_format`.
<br>

<br>
        Contrary to :func:`datasets.Dataset.set_transform`, ``with_transform`` returns a new Dataset object.
<br>

<br>
        Args:
<br>
            transform (Optional ``Callable``): user-defined formatting transform, replaces the format defined by :func:`datasets.Dataset.set_format`
<br>
                A formatting function is a callable that takes a batch (as a dict) as input and returns a batch.
<br>
                This function is applied right before returning the objects in __getitem__.
<br>
            columns (Optional ``List[str]``): columns to format in the output
<br>
                If specified, then the input batch of the transform only contains those columns.
<br>
            output_all_columns (``bool`` default to False): keep un-formatted columns as well in the output (as python objects)
<br>
                If set to True, then the other un-formatted columns are kept with the output of the transform.
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:prepare_for_task' href='parser/test3/arrow_dataset.py#L1450'>Dataset:prepare_for_task</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>task:  Union[str,<br>TaskTemplate],<br></ul>
        <li>Docs:<br>        """Prepare a dataset for the given task by casting the dataset's :class:`Features` to standardized column names and types as detailed in :py:mod:`datasets.tasks`.
<br>

<br>
        Casts :attr:`datasets.DatasetInfo.features` according to a task-specific schema. Intended for single-use only, so all task templates are removed from :attr:`datasets.DatasetInfo.task_templates` after casting.
<br>

<br>
        Args:
<br>
            task (:obj:`Union[str, TaskTemplate]`): The task to prepare the dataset for during training and evaluation. If :obj:`str`, supported tasks include:
<br>

<br>
                - :obj:`"text-classification"`
<br>
                - :obj:`"question-answering"`
<br>

<br>
                If :obj:`TaskTemplate`, must be one of the task templates in :py:mod:`datasets.tasks`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:_getitem' href='parser/test3/arrow_dataset.py#L1496'>Dataset:_getitem</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>key:  Union[int,<br>slice,<br>str],<br>format_type = None,<br>format_columns = None,<br>output_all_columns = False,<br>format_kwargs = None,<br>,<br></ul>
        <li>Docs:<br>        """
<br>
        Can be used to index columns (by string names) or rows (by integer index, slices, or iter of indices or bools)
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:__getitem__' href='parser/test3/arrow_dataset.py#L1515'>Dataset:__getitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>key:  Union[int,<br>slice,<br>str],<br></ul>
        <li>Docs:<br>        """Can be used to index columns (by string names) or rows (by integer index or iterable of indices or bools)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:cleanup_cache_files' href='parser/test3/arrow_dataset.py#L1525'>Dataset:cleanup_cache_files</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Clean up all cache files in the dataset cache directory, excepted the currently used cache file if there is
<br>
        one.
<br>

<br>
        Be careful when running this command that no other process is currently using other cache files.
<br>

<br>
        Returns:
<br>
            :obj:`int`: Number of removed files.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:_get_cache_file_path' href='parser/test3/arrow_dataset.py#L1553'>Dataset:_get_cache_file_path</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>fingerprint,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:map' href='parser/test3/arrow_dataset.py#L1563'>Dataset:map</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>function:  Optional[Callable]  =  None,<br>with_indices:  bool  =  False,<br>input_columns:  Optional[Union[str,<br>List[str]]]  =  None,<br>batched:  bool  =  False,<br>batch_size:  Optional[int]  =  1000,<br>drop_last_batch:  bool  =  False,<br>remove_columns:  Optional[List[str]]  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  None,<br>cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>features:  Optional[Features]  =  None,<br>disable_nullable:  bool  =  False,<br>fn_kwargs:  Optional[dict]  =  None,<br>num_proc:  Optional[int]  =  None,<br>suffix_template:  str  =  "_{rank:05d}_of_{num_proc:05d}",<br>new_fingerprint:  Optional[str]  =  None,<br>desc:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Apply a function to all the elements in the table (individually or in batches)
<br>
        and update the table (if function does update examples).
<br>

<br>
        Args:
<br>
            function (:obj:`Callable`): Function with one of the following signatures:
<br>

<br>
                - `function(example: Union[Dict, Any]) -> Union[Dict, Any]` if `batched=False` and `with_indices=False`
<br>
                - `function(example: Union[Dict, Any], indices: int) -> Union[Dict, Any]` if `batched=False` and `with_indices=True`
<br>
                - `function(batch: Union[Dict[List], List[Any]]) -> Union[Dict, Any]` if `batched=True` and `with_indices=False`
<br>
                - `function(batch: Union[Dict[List], List[Any]], indices: List[int]) -> Union[Dict, Any]` if `batched=True` and `with_indices=True`
<br>

<br>
                If no function is provided, default to identity function: ``lambda x: x``.
<br>
            with_indices (:obj:`bool`, default `False`): Provide example indices to `function`. Note that in this case the
<br>
                signature of `function` should be `def function(example, idx): ...`.
<br>
            input_columns (`Optional[Union[str, List[str]]]`, default `None`): The columns to be passed into `function`
<br>
                as positional arguments. If `None`, a dict mapping to all formatted columns is passed as one argument.
<br>
            batched (:obj:`bool`, default `False`): Provide batch of examples to `function`.
<br>
            batch_size (`Optional[int]`, default `1000`): Number of examples per batch provided to `function` if `batched=True`
<br>
                `batch_size <= 0` or `batch_size == None`: Provide the full dataset as a single batch to `function`.
<br>
            drop_last_batch (:obj:`bool`, default `False`): Whether a last batch smaller than the batch_size should be
<br>
                dropped instead of being processed by the function.
<br>
            remove_columns (`Optional[List[str]]`, default `None`): Remove a selection of columns while doing the mapping.
<br>
                Columns will be removed before updating the examples with the output of `function`, i.e. if `function` is adding
<br>
                columns with names in `remove_columns`, these columns will be kept.
<br>
            keep_in_memory (:obj:`bool`, default `False`): Keep the dataset in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (:obj:`bool`, default `True` if caching is enabled): If a cache file storing the current computation from `function`
<br>
                can be identified, use it instead of recomputing.
<br>
            cache_file_name (`Optional[str]`, default `None`): Provide the name of a path for the cache file. It is used to store the
<br>
                results of the computation instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            features (`Optional[datasets.Features]`, default `None`): Use a specific Features to store the cache file
<br>
                instead of the automatically generated one.
<br>
            disable_nullable (:obj:`bool`, default `True`): Disallow null values in the table.
<br>
            fn_kwargs (`Optional[Dict]`, default `None`): Keyword arguments to be passed to `function`.
<br>
            num_proc (`Optional[int]`, default `None`): Number of processes for multiprocessing. By default it doesn't
<br>
                use multiprocessing.
<br>
            suffix_template (:obj:`str`):
<br>
                If cache_file_name is specified, then this suffix
<br>
                will be added at the end of the base name of each: defaults to "_{rank:05d}_of_{num_proc:05d}". For example, if cache_file_name is "processed.arrow", then for
<br>
                rank=1 and num_proc=4, the resulting file would be "processed_00001_of_00004.arrow" for the default suffix.
<br>
            new_fingerprint (`Optional[str]`, default `None`): the new fingerprint of the dataset after transform.
<br>
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.
<br>
            desc (`Optional[str]`, defaults to `None`): Meaningful description to be displayed alongside with the progress bar while mapping examples.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:_map_single' href='parser/test3/arrow_dataset.py#L1745'>Dataset:_map_single</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>function:  Optional[Callable]  =  None,<br>with_indices:  bool  =  False,<br>input_columns:  Optional[Union[str,<br>List[str]]]  =  None,<br>batched:  bool  =  False,<br>batch_size:  Optional[int]  =  1000,<br>drop_last_batch:  bool  =  False,<br>remove_columns:  Optional[List[str]]  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  None,<br>cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>features:  Optional[Features]  =  None,<br>disable_nullable:  bool  =  False,<br>fn_kwargs:  Optional[dict]  =  None,<br>new_fingerprint:  Optional[str]  =  None,<br>rank:  Optional[int]  =  None,<br>offset:  int  =  0,<br>desc:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Apply a function to all the elements in the table (individually or in batches)
<br>
        and update the table (if function does update examples).
<br>

<br>
        Args:
<br>
            function (:obj:`Callable`): with one of the following signature:
<br>
                - `function(example: Union[Dict, Any]) -> Union[Dict, Any]` if `batched=False` and `with_indices=False`
<br>
                - `function(example: Union[Dict, Any], indices: int) -> Union[Dict, Any]` if `batched=False` and `with_indices=True`
<br>
                - `function(batch: Union[Dict[List], List[Any]]) -> Union[Dict, Any]` if `batched=True` and `with_indices=False`
<br>
                - `function(batch: Union[Dict[List], List[Any]], indices: List[int]) -> Union[Dict, Any]` if `batched=True` and `with_indices=True`
<br>
                If no function is provided, default to identity function: lambda x: x
<br>
            with_indices (:obj:`bool`, defaults to `False`): Provide example indices to `function`. Note that in this case the signature of `function` should be `def function(example, idx): ...`.
<br>
            input_columns (`Optional[Union[str, List[str]]]`, defaults to `None`): The columns to be passed into `function` as
<br>
                positional arguments. If `None`, a dict mapping to all formatted columns is passed as one argument.
<br>
            batched (:obj:`bool`, defaults to `False`): Provide batch of examples to `function`
<br>
            batch_size (`Optional[int]`, defaults to `1000`): Number of examples per batch provided to `function` if `batched=True`
<br>
                `batch_size <= 0` or `batch_size == None`: Provide the full dataset as a single batch to `function`
<br>
            drop_last_batch (:obj:`bool`, default: `False`): Whether a last batch smaller than the batch_size should be
<br>
                dropped instead of being processed by the function.
<br>
            remove_columns (`Optional[List[str]]`, defaults to `None`): Remove a selection of columns while doing the mapping.
<br>
                Columns will be removed before updating the examples with the output of `function`, i.e. if `function` is adding
<br>
                columns with names in `remove_columns`, these columns will be kept.
<br>
            keep_in_memory (:obj:`bool`, defaults to `False`): Keep the dataset in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (:obj:`bool`, defaults to `True` if caching is enabled): If a cache file storing the current computation from `function`
<br>
                can be identified, use it instead of recomputing.
<br>
            cache_file_name (`Optional[str]`, defaults to `None`): Provide the name of a path for the cache file. It is used to store the
<br>
                results of the computation instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            features (`Optional[datasets.Features]`, defaults to `None`): Use a specific Features to store the cache file
<br>
                instead of the automatically generated one.
<br>
            disable_nullable (:obj:`bool`, defaults to `True`): Disallow null values in the table.
<br>
            fn_kwargs (`Optional[Dict]`, defaults to `None`): Keyword arguments to be passed to `function`
<br>
            new_fingerprint (`Optional[str]`, defaults to `None`): the new fingerprint of the dataset after transform.
<br>
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments
<br>
            rank: (`Optional[int]`, defaults to `None`): If specified, this is the process rank when doing multiprocessing
<br>
            offset: (:obj:`int`, defaults to 0): If specified, this is an offset applied to the indices passed to `function` if `with_indices=True`
<br>
            desc (`Optional[str]`, defaults to `None`): Meaningful description to be displayed alongside with the progress bar while mapping examples.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:filter' href='parser/test3/arrow_dataset.py#L2064'>Dataset:filter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>function:  Optional[Callable]  =  None,<br>with_indices = False,<br>input_columns:  Optional[Union[str,<br>List[str]]]  =  None,<br>batch_size:  Optional[int]  =  1000,<br>remove_columns:  Optional[List[str]]  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>fn_kwargs:  Optional[dict]  =  None,<br>num_proc:  Optional[int]  =  None,<br>suffix_template:  str  =  "_{rank:05d}_of_{num_proc:05d}",<br>new_fingerprint:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Apply a filter function to all the elements in the table in batches
<br>
        and update the table so that the dataset only includes examples according to the filter function.
<br>

<br>
        Args:
<br>
            function (:obj:`Callable`): Callable with one of the following signatures:
<br>

<br>
                - ``function(example: Union[Dict, Any]) -> bool`` if ``with_indices=False``
<br>
                - ``function(example: Union[Dict, Any], indices: int) -> bool`` if ``with_indices=True``
<br>

<br>
                If no function is provided, defaults to an always True function: ``lambda x: True``.
<br>
            with_indices (:obj:`bool`, default `False`): Provide example indices to `function`. Note that in this case the signature of `function` should be `def function(example, idx): ...`.
<br>
            input_columns (:obj:`str` or `List[str]`, optional): The columns to be passed into `function` as
<br>
                positional arguments. If `None`, a dict mapping to all formatted columns is passed as one argument.
<br>
            batch_size (:obj:`int`, optional, default `1000`): Number of examples per batch provided to `function` if
<br>
                ``batched = True``. If ``batch_size <= 0`` or ``batch_size == None``: provide the full dataset as a
<br>
                single batch to `function`
<br>
            remove_columns (`List[str]`, optional): Remove a selection of columns while doing the mapping.
<br>
                Columns will be removed before updating the examples with the output of `function`, i.e. if `function` is adding
<br>
                columns with names in `remove_columns`, these columns will be kept.
<br>
            keep_in_memory (:obj:`bool`, default `False`): Keep the dataset in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (:obj:`bool`, default `True`): If a cache file storing the current computation from `function`
<br>
                can be identified, use it instead of recomputing.
<br>
            cache_file_name (:obj:`str`, optional): Provide the name of a path for the cache file. It is used to store the
<br>
                results of the computation instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            fn_kwargs (:obj:`dict`, optional): Keyword arguments to be passed to `function`
<br>
            num_proc (:obj:`int`, optional): Number of processes for multiprocessing. By default it doesn't
<br>
                use multiprocessing.
<br>
            suffix_template (:obj:`str`):
<br>
                If `cache_file_name` is specified, then this suffix will be added at the end of the base name of each.
<br>
                For example, if `cache_file_name` is `"processed.arrow"`, then for ``rank = 1`` and ``num_proc = 4``,
<br>
                the resulting file would be `"processed_00001_of_00004.arrow"` for the default suffix (default
<br>
                `_{rank:05d}_of_{num_proc:05d}`)
<br>
            new_fingerprint (:obj:`str`, optional): The new fingerprint of the dataset after transform.
<br>
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:flatten_indices' href='parser/test3/arrow_dataset.py#L2162'>Dataset:flatten_indices</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>keep_in_memory:  bool  =  False,<br>cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>features:  Optional[Features]  =  None,<br>disable_nullable:  bool  =  True,<br>new_fingerprint:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Create and cache a new Dataset by flattening the indices mapping.
<br>

<br>
        Args:
<br>
            keep_in_memory (:obj:`bool`, default `False`): Keep the dataset in memory instead of writing it to a cache file.
<br>
            cache_file_name (`Optional[str]`, default `None`): Provide the name of a path for the cache file. It is used to store the
<br>
                results of the computation instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            features (`Optional[datasets.Features]`, default `None`): Use a specific Features to store the cache file
<br>
                instead of the automatically generated one.
<br>
            disable_nullable (:obj:`bool`, default `True`): Allow null values in the table.
<br>
            new_fingerprint (`Optional[str]`, default `None`): The new fingerprint of the dataset after transform.
<br>
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:_new_dataset_with_indices' href='parser/test3/arrow_dataset.py#L2197'>Dataset:_new_dataset_with_indices</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>indices_cache_file_name:  Optional[str]  =  None,<br>indices_buffer:  Optional[pa.Buffer]  =  None,<br>fingerprint:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Return a new Dataset obtained by adding indices (provided in indices_cache_file_name or in a buffer) to the
<br>
        current Dataset.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:select' href='parser/test3/arrow_dataset.py#L2229'>Dataset:select</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>indices:  Iterable,<br>keep_in_memory:  bool  =  False,<br>indices_cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>new_fingerprint:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Create a new dataset with rows selected following the list/array of indices.
<br>

<br>
        Args:
<br>
            indices (sequence, iterable, ndarray or Series): List or 1D-array of integer indices for indexing.
<br>
            keep_in_memory (:obj:`bool`, default `False`): Keep the indices mapping in memory instead of writing it to a cache file.
<br>
            indices_cache_file_name (`Optional[str]`, default `None`): Provide the name of a path for the cache file. It is used to store the
<br>
                indices mapping instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            new_fingerprint (`Optional[str]`, default `None`): the new fingerprint of the dataset after transform.
<br>
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:sort' href='parser/test3/arrow_dataset.py#L2312'>Dataset:sort</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br>reverse:  bool  =  False,<br>kind:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>indices_cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>new_fingerprint:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Create a new dataset sorted according to a column.
<br>

<br>
        Currently sorting according to a column name uses numpy sorting algorithm under the hood.
<br>
        The column should thus be a numpy compatible type (in particular not a nested type).
<br>
        This also means that the column used for sorting is fully loaded in memory (which should be fine in most cases).
<br>

<br>
        Args:
<br>
            column (:obj:`str`): column name to sort by.
<br>
            reverse (:obj:`bool`, default `False`): If True, sort by descending order rather then ascending.
<br>
            kind (:obj:`str`, optional): Numpy algorithm for sorting selected in {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’},
<br>
                The default is ‘quicksort’. Note that both ‘stable’ and ‘mergesort’ use timsort under the covers and, in general,
<br>
                the actual implementation will vary with data type. The ‘mergesort’ option is retained for backwards compatibility.
<br>
            keep_in_memory (:obj:`bool`, default `False`): Keep the sorted indices in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (:obj:`bool`, default `True`): If a cache file storing the sorted indices
<br>
                can be identified, use it instead of recomputing.
<br>
            indices_cache_file_name (`Optional[str]`, default `None`): Provide the name of a path for the cache file. It is used to store the
<br>
                sorted indices instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                Higher value gives smaller cache files, lower value consume less temporary memory.
<br>
            new_fingerprint (`Optional[str]`, default `None`): the new fingerprint of the dataset after transform.
<br>
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:shuffle' href='parser/test3/arrow_dataset.py#L2392'>Dataset:shuffle</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>seed:  Optional[int]  =  None,<br>generator:  Optional[np.random.Generator]  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>indices_cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>new_fingerprint:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Create a new Dataset where the rows are shuffled.
<br>

<br>
        Currently shuffling uses numpy random generators.
<br>
        You can either supply a NumPy BitGenerator to use, or a seed to initiate NumPy's default random generator (PCG64).
<br>

<br>
        Args:
<br>
            seed (:obj:`int`, optional): A seed to initialize the default BitGenerator if ``generator=None``.
<br>
                If None, then fresh, unpredictable entropy will be pulled from the OS.
<br>
                If an int or array_like[ints] is passed, then it will be passed to SeedSequence to derive the initial BitGenerator state.
<br>
            generator (:obj:`numpy.random.Generator`, optional): Numpy random Generator to use to compute the permutation of the dataset rows.
<br>
                If ``generator=None`` (default), uses np.random.default_rng (the default BitGenerator (PCG64) of NumPy).
<br>
            keep_in_memory (:obj:`bool`, default `False`): Keep the shuffled indices in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (:obj:`bool`, default `True`): If a cache file storing the shuffled indices
<br>
                can be identified, use it instead of recomputing.
<br>
            indices_cache_file_name (:obj:`str`, optional): Provide the name of a path for the cache file. It is used to store the
<br>
                shuffled indices instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            new_fingerprint (:obj:`str`, optional, default `None`): the new fingerprint of the dataset after transform.
<br>
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:train_test_split' href='parser/test3/arrow_dataset.py#L2473'>Dataset:train_test_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>test_size:  Union[float,<br>int,<br>None]  =  None,<br>train_size:  Union[float,<br>int,<br>None]  =  None,<br>shuffle:  bool  =  True,<br>seed:  Optional[int]  =  None,<br>generator:  Optional[np.random.Generator]  =  None,<br>keep_in_memory:  bool  =  False,<br>load_from_cache_file:  bool  =  True,<br>train_indices_cache_file_name:  Optional[str]  =  None,<br>test_indices_cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>train_new_fingerprint:  Optional[str]  =  None,<br>test_new_fingerprint:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Return a dictionary (:obj:`datasets.DatsetDict`) with two random train and test subsets (`train` and `test` ``Dataset`` splits).
<br>
        Splits are created from the dataset according to `test_size`, `train_size` and `shuffle`.
<br>

<br>
        This method is similar to scikit-learn `train_test_split` with the omission of the stratified options.
<br>

<br>
        Args:
<br>
            test_size (:obj:`numpy.random.Generator`, optional): Size of the test split
<br>
                If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split.
<br>
                If int, represents the absolute number of test samples.
<br>
                If None, the value is set to the complement of the train size.
<br>
                If train_size is also None, it will be set to 0.25.
<br>
            train_size (:obj:`numpy.random.Generator`, optional): Size of the train split
<br>
                If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split.
<br>
                If int, represents the absolute number of train samples.
<br>
                If None, the value is automatically set to the complement of the test size.
<br>
            shuffle (:obj:`bool`, optional, default `True`): Whether or not to shuffle the data before splitting.
<br>
            seed (:obj:`int`, optional): A seed to initialize the default BitGenerator if ``generator=None``.
<br>
                If None, then fresh, unpredictable entropy will be pulled from the OS.
<br>
                If an int or array_like[ints] is passed, then it will be passed to SeedSequence to derive the initial BitGenerator state.
<br>
            generator (:obj:`numpy.random.Generator`, optional): Numpy random Generator to use to compute the permutation of the dataset rows.
<br>
                If ``generator=None`` (default), uses np.random.default_rng (the default BitGenerator (PCG64) of NumPy).
<br>
            keep_in_memory (:obj:`bool`, default `False`): Keep the splits indices in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (:obj:`bool`, default `True`): If a cache file storing the splits indices
<br>
                can be identified, use it instead of recomputing.
<br>
            train_cache_file_name (:obj:`str`, optional): Provide the name of a path for the cache file. It is used to store the
<br>
                train split indices instead of the automatically generated cache file name.
<br>
            test_cache_file_name (:obj:`str`, optional): Provide the name of a path for the cache file. It is used to store the
<br>
                test split indices instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
            train_new_fingerprint (:obj:`str`, optional, defaults to `None`): the new fingerprint of the train set after transform.
<br>
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments
<br>
            test_new_fingerprint (:obj:`str`, optional, defaults to `None`): the new fingerprint of the test set after transform.
<br>
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:shard' href='parser/test3/arrow_dataset.py#L2667'>Dataset:shard</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>num_shards:  int,<br>index:  int,<br>contiguous:  bool  =  False,<br>keep_in_memory:  bool  =  False,<br>indices_cache_file_name:  Optional[str]  =  None,<br>writer_batch_size:  Optional[int]  =  1000,<br>,<br></ul>
        <li>Docs:<br>        """Return the `index`-nth shard from dataset split into `num_shards` pieces.
<br>

<br>
        This shards deterministically. dset.shard(n, i) will contain all elements of dset whose
<br>
        index mod n = i.
<br>

<br>
        dset.shard(n, i, contiguous=True) will instead split dset into contiguous chunks,
<br>
        so it can be easily concatenated back together after processing. If n % i == l, then the
<br>
        first l shards will have length (n // i) + 1, and the remaining shards will have length (n // i).
<br>
        `datasets.concatenate([dset.shard(n, i, contiguous=True) for i in range(n)])` will return
<br>
        a dataset with the same order as the original.
<br>

<br>
        Be sure to shard before using any randomizing operator (such as shuffle).
<br>
        It is best if the shard operator is used early in the dataset pipeline.
<br>

<br>

<br>
        Args:
<br>
            num_shards (:obj:`int`): How many shards to split the dataset into.
<br>
            index (:obj:`int`): Which shard to select and return.
<br>
            contiguous: (:obj:`bool`, default `False`): Whether to select contiguous blocks of indices for shards.
<br>
            keep_in_memory (:obj:`bool`, default `False`): Keep the dataset in memory instead of writing it to a cache file.
<br>
            load_from_cache_file (:obj:`bool`, default `True`): If a cache file storing the current computation from `function`
<br>
                can be identified, use it instead of recomputing.
<br>
            indices_cache_file_name (:obj:`str`, optional): Provide the name of a path for the cache file. It is used to store the
<br>
                indices of each shard instead of the automatically generated cache file name.
<br>
            writer_batch_size (:obj:`int`, default `1000`): Number of rows per write operation for the cache file writer.
<br>
                This value is a good trade-off between memory usage during the processing, and processing speed.
<br>
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `.map()`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:export' href='parser/test3/arrow_dataset.py#L2721'>Dataset:export</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>filename:  str,<br>format:  str  =  "tfrecord",<br>,<br></ul>
        <li>Docs:<br>        """Writes the Arrow dataset to a TFRecord file.
<br>

<br>
        The dataset must already be in tensorflow format. The records will be written with
<br>
        keys from `dataset._format_columns`.
<br>

<br>
        Args:
<br>
            filename (:obj:`str`): The filename, including the `.tfrecord` extension, to write to.
<br>
            format (`str`, optional, default `"tfrecord"`): The type of output file. Currently this is a no-op, as
<br>
                TFRecords are the only option. This enables a more flexible function signature later.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:to_csv' href='parser/test3/arrow_dataset.py#L2803'>Dataset:to_csv</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_buf:  Union[PathLike,<br>BinaryIO],<br>batch_size:  Optional[int]  =  None,<br>**to_csv_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Exports the dataset to csv
<br>

<br>
        Args:
<br>
            path_or_buf (``PathLike`` or ``FileOrBuffer``): Either a path to a file or a BinaryIO.
<br>
            batch_size (Optional ``int``): Size of the batch to load in memory and write at once.
<br>
                Defaults to :obj:`datasets.config.DEFAULT_MAX_BATCH_SIZE`.
<br>
            to_csv_kwargs: Parameters to pass to pandas's :func:`pandas.DataFrame.to_csv`
<br>

<br>
        Returns:
<br>
            int: The number of characters or bytes written
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:to_dict' href='parser/test3/arrow_dataset.py#L2825'>Dataset:to_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>batch_size:  Optional[int]  =  None,<br>batched:  bool  =  False,<br></ul>
        <li>Docs:<br>        """Returns the dataset as a Python dict. Can also return a generator for large datasets.
<br>

<br>
        Args:
<br>
            batched (``bool``): Set to :obj:`True` to return a generator that yields the dataset as batches
<br>
                of ``batch_size`` rows. Defaults to :obj:`False` (returns the whole datasetas once)
<br>
            bacth_size (Optional ``int``): The size (number of rows) of the batches if ``batched`` is `True`.
<br>
                Defaults to :obj:`datasets.config.DEFAULT_MAX_BATCH_SIZE`.
<br>

<br>
        Returns:
<br>
            `dict` or `Iterator[dict]`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:to_json' href='parser/test3/arrow_dataset.py#L2854'>Dataset:to_json</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_buf:  Union[PathLike,<br>BinaryIO],<br>batch_size:  Optional[int]  =  None,<br>**to_json_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Export the dataset to JSON Lines or JSON.
<br>

<br>
        Args:
<br>
            path_or_buf (``PathLike`` or ``FileOrBuffer``): Either a path to a file or a BinaryIO.
<br>
            batch_size (:obj:`int`, optional): Size of the batch to load in memory and write at once.
<br>
                Defaults to :obj:`datasets.config.DEFAULT_MAX_BATCH_SIZE`.
<br>
            lines (:obj:`bool`, default ``True``): Whether output JSON lines format.
<br>
                Only possible if ``orient="records"`. It will throw ValueError with ``orient`` different from
<br>
                ``"records"``, since the others are not list-like.
<br>
            orient (:obj:`str`, default ``"records"``): Format of the JSON:
<br>

<br>
                - ``"records"``: list like ``[{column -> value}, … , {column -> value}]``
<br>
                - ``"split"``: dict like ``{"index" -> [index], "columns" -> [columns], "data" -> [values]}``
<br>
                - ``"index"``: dict like ``{index -> {column -> value}}``
<br>
                - ``"columns"``: dict like ``{column -> {index -> value}}``
<br>
                - ``"values"``: just the values array
<br>
                - ``"table"``: dict like ``{"schema": {schema}, "data": {data}}``
<br>
            **to_json_kwargs: Parameters to pass to pandas's `pandas.DataFrame.to_json
<br>
                <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html>`_.
<br>

<br>
        Returns:
<br>
            int: The number of characters or bytes written.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:to_pandas' href='parser/test3/arrow_dataset.py#L2888'>Dataset:to_pandas</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>batch_size:  Optional[int]  =  None,<br>batched:  bool  =  False,<br></ul>
        <li>Docs:<br>        """Returns the dataset as a :class:`pandas.DataFrame`. Can also return a generator for large datasets.
<br>

<br>
        Args:
<br>
            batched (``bool``): Set to :obj:`True` to return a generator that yields the dataset as batches
<br>
                of ``batch_size`` rows. Defaults to :obj:`False` (returns the whole datasetas once)
<br>
            bacth_size (Optional ``int``): The size (number of rows) of the batches if ``batched`` is `True`.
<br>
                Defaults to :obj:`datasets.config.DEFAULT_MAX_BATCH_SIZE`.
<br>

<br>
        Returns:
<br>
            `pandas.DataFrame` or `Iterator[pandas.DataFrame]`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:to_parquet' href='parser/test3/arrow_dataset.py#L2919'>Dataset:to_parquet</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_buf:  Union[PathLike,<br>BinaryIO],<br>batch_size:  Optional[int]  =  None,<br>**parquet_writer_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Exports the dataset to parquet
<br>

<br>
        Args:
<br>
            path_or_buf (``PathLike`` or ``FileOrBuffer``): Either a path to a file or a BinaryIO.
<br>
            batch_size (Optional ``int``): Size of the batch to load in memory and write at once.
<br>
                Defaults to :obj:`datasets.config.DEFAULT_MAX_BATCH_SIZE`.
<br>
            parquet_writer_kwargs: Parameters to pass to PyArrow's :class:`pyarrow.parquet.ParquetWriter`
<br>

<br>
        Returns:
<br>
            int: The number of characters or bytes written
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:add_column' href='parser/test3/arrow_dataset.py#L2943'>Dataset:add_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>name:  str,<br>column:  Union[list,<br>np.array],<br>new_fingerprint:  str,<br></ul>
        <li>Docs:<br>        """Add column to Dataset.
<br>

<br>
        .. versionadded:: 1.7
<br>

<br>
        Args:
<br>
            name (str): Column name.
<br>
            column (list or np.array): Column data to be added.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:add_faiss_index' href='parser/test3/arrow_dataset.py#L2964'>Dataset:add_faiss_index</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br>index_name:  Optional[str]  =  None,<br>device:  Optional[int]  =  None,<br>string_factory:  Optional[str]  =  None,<br>metric_type:  Optional[int]  =  None,<br>custom_index:  Optional["faiss.Index"]  =  None,<br># noqa:  F821train_size: Optional[int]  =  None,<br>faiss_verbose:  bool  =  False,<br>dtype = np.float32,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:add_faiss_index_from_external_arrays' href='parser/test3/arrow_dataset.py#L3037'>Dataset:add_faiss_index_from_external_arrays</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>external_arrays:  np.array,<br>index_name:  str,<br>device:  Optional[int]  =  None,<br>string_factory:  Optional[str]  =  None,<br>metric_type:  Optional[int]  =  None,<br>custom_index:  Optional["faiss.Index"]  =  None,<br># noqa:  F821train_size: Optional[int]  =  None,<br>faiss_verbose:  bool  =  False,<br>dtype = np.float32,<br>,<br></ul>
        <li>Docs:<br>        """Add a dense index using Faiss for fast retrieval.
<br>
        The index is created using the vectors of `external_arrays`.
<br>
        You can specify `device` if you want to run it on GPU (`device` must be the GPU index).
<br>
        You can find more information about Faiss here:
<br>

<br>
        - For `string factory <https://github.com/facebookresearch/faiss/wiki/The-index-factory>`__
<br>

<br>
        Args:
<br>
            external_arrays (:obj:`np.array`):
<br>
                If you want to use arrays from outside the lib for the index, you can set :obj:`external_arrays`.
<br>
                It will use :obj:`external_arrays` to create the Faiss index instead of the arrays in the given :obj:`column`.
<br>
            index_name (:obj:`str`):
<br>
                The index_name/identifier of the index.
<br>
                This is the index_name that is used to call :func:`datasets.Dataset.get_nearest_examples` or :func:`datasets.Dataset.search`.
<br>
            device (Optional :obj:`int`):
<br>
                If not None, this is the index of the GPU to use.
<br>
                By default it uses the CPU.
<br>
            string_factory (Optional :obj:`str`):
<br>
                This is passed to the index factory of Faiss to create the index.
<br>
                Default index class is ``IndexFlat``.
<br>
            metric_type (Optional :obj:`int`):
<br>
                Type of metric. Ex: faiss.faiss.METRIC_INNER_PRODUCT or faiss.METRIC_L2.
<br>
            custom_index (Optional :obj:`faiss.Index`):
<br>
                Custom Faiss index that you already have instantiated and configured for your needs.
<br>
            train_size (Optional :obj:`int`):
<br>
                If the index needs a training step, specifies how many vectors will be used to train the index.
<br>
            faiss_verbose (:obj:`bool`, defaults to False):
<br>
                Enable the verbosity of the Faiss index.
<br>
            dtype (:obj:`numpy.dtype`): The dtype of the numpy arrays that are indexed. Default is np.float32.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:add_elasticsearch_index' href='parser/test3/arrow_dataset.py#L3090'>Dataset:add_elasticsearch_index</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>column:  str,<br>index_name:  Optional[str]  =  None,<br>host:  Optional[str]  =  None,<br>port:  Optional[int]  =  None,<br>es_client:  Optional["elasticsearch.Elasticsearch"]  =  None,<br># noqa:  F821es_index_name: Optional[str]  =  None,<br>es_index_config:  Optional[dict]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Add a text index using ElasticSearch for fast retrieval. This is done in-place.
<br>

<br>
        Args:
<br>
            column (:obj:`str`):
<br>
                The column of the documents to add to the index.
<br>
            index_name (Optional :obj:`str`):
<br>
                The index_name/identifier of the index.
<br>
                This is the index name that is used to call :meth:`Dataset.get_nearest_examples` or :meth:`Dataset.search`.
<br>
                By default it corresponds to :obj:`column`.
<br>
            host (Optional :obj:`str`, defaults to localhost):
<br>
                host of where ElasticSearch is running
<br>
            port (Optional :obj:`str`, defaults to 9200):
<br>
                port of where ElasticSearch is running
<br>
            es_client (Optional :obj:`elasticsearch.Elasticsearch`):
<br>
                The elasticsearch client used to create the index if host and port are None.
<br>
            es_index_name (Optional :obj:`str`):
<br>
                The elasticsearch index name used to create the index.
<br>
            es_index_config (Optional :obj:`dict`):
<br>
                The configuration of the elasticsearch index.
<br>
                Default config is::
<br>

<br>
                    {
<br>
                        "settings": {
<br>
                            "number_of_shards": 1,
<br>
                            "analysis": {"analyzer": {"stop_standard": {"type": "standard", " stopwords": "_english_"}}},
<br>
                        },
<br>
                        "mappings": {
<br>
                            "properties": {
<br>
                                "text": {
<br>
                                    "type": "text",
<br>
                                    "analyzer": "standard",
<br>
                                    "similarity": "BM25"
<br>
                                },
<br>
                            }
<br>
                        },
<br>
                    }
<br>

<br>
        Example:
<br>
            .. code-block:: python
<br>

<br>
                es_client = elasticsearch.Elasticsearch()
<br>
                ds = datasets.load_dataset('crime_and_punish', split='train')
<br>
                ds.add_elasticsearch_index(column='line', es_client=es_client, es_index_name="my_es_index")
<br>
                scores, retrieved_examples = ds.get_nearest_examples('line', 'my new query', k=10)
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:add_item' href='parser/test3/arrow_dataset.py#L3160'>Dataset:add_item</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>item:  dict,<br>new_fingerprint:  str,<br></ul>
        <li>Docs:<br>        """Add item to Dataset.
<br>

<br>
        .. versionadded:: 1.7
<br>

<br>
        Args:
<br>
            item (dict): Item data to be added.
<br>

<br>
        Returns:
<br>
            :class:`Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_dataset.py:Dataset:align_labels_with_mapping' href='parser/test3/arrow_dataset.py#L3191'>Dataset:align_labels_with_mapping</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>label2id:  Dict,<br>label_column:  str,<br></ul>
        <li>Docs:<br>        """Align the dataset's label ID and label name mapping to match an input :obj:`label2id` mapping.
<br>
        This is useful when you want to ensure that a model's predicted labels are aligned with the dataset.
<br>
        The alignment in done using the lowercase label names.
<br>

<br>
        Args:
<br>
            label2id (:obj:`dict`):
<br>
                The label name to ID mapping to align the dataset with.
<br>
            label_column (:obj:`str`):
<br>
                The column name of labels to align on.
<br>

<br>
        Example:
<br>
            .. code-block:: python
<br>

<br>
                # dataset with mapping {'entailment': 0, 'neutral': 1, 'contradiction': 2}
<br>
                ds = load_dataset("glue", "mnli", split="train")
<br>
                # mapping to align with
<br>
                label2id = {'CONTRADICTION': 0, 'NEUTRAL': 1, 'ENTAILMENT': 2}
<br>
                ds_aligned = ds.align_labels_with_mapping(label2id, "label")
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/tasks/question_answering.py' href='parser/test3/tasks/question_answering.py'>parser/test3/tasks/question_answering.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/tasks/question_answering.py:QuestionAnsweringExtractive' href='parser/test3/tasks/question_answering.py#L9'>QuestionAnsweringExtractive</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/tasks/question_answering.py:QuestionAnsweringExtractive:column_mapping' href='parser/test3/tasks/question_answering.py#L28'>QuestionAnsweringExtractive:column_mapping</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/builder.py' href='parser/test3/builder.py'>parser/test3/builder.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/builder.py:InvalidConfigName' href='parser/test3/builder.py#L53'>InvalidConfigName</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/builder.py:BuilderConfig' href='parser/test3/builder.py#L58'>BuilderConfig</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/builder.py:DatasetBuilder' href='parser/test3/builder.py#L173'>DatasetBuilder</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/builder.py:GeneratorBasedBuilder' href='parser/test3/builder.py#L995'>GeneratorBasedBuilder</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/builder.py:ArrowBasedBuilder' href='parser/test3/builder.py#L1086'>ArrowBasedBuilder</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/builder.py:MissingBeamOptions' href='parser/test3/builder.py#L1144'>MissingBeamOptions</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/builder.py:BeamBasedBuilder' href='parser/test3/builder.py#L1148'>BeamBasedBuilder</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:BuilderConfig:__post_init__' href='parser/test3/builder.py#L78'>BuilderConfig:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:BuilderConfig:__eq__' href='parser/test3/builder.py#L91'>BuilderConfig:__eq__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>o,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:BuilderConfig:create_config_id' href='parser/test3/builder.py#L98'>BuilderConfig:create_config_id</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>config_kwargs:  dict,<br>custom_features:  Optional[Features]  =  None,<br></ul>
        <li>Docs:<br>        """
<br>
        The config id is used to build the cache directory.
<br>
        By default it is equal to the config name.
<br>
        However the name of a config is not sufficent to have a unique identifier for the dataset being generated since
<br>
        it doesn't take into account:
<br>
        - the config kwargs that can be used to overwrite attributes
<br>
        - the custom features used to write the dataset
<br>
        - the data_files for json/text/csv/pandas datasets
<br>
        Therefore the config id is just the config name with an optional suffix based on these.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:__init__' href='parser/test3/builder.py#L202'>DatasetBuilder:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>cache_dir:  Optional[str]  =  None,<br>name:  Optional[str]  =  None,<br>hash:  Optional[str]  =  None,<br>base_path:  Optional[str]  =  None,<br>features:  Optional[Features]  =  None,<br>**config_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Constructs a DatasetBuilder.
<br>

<br>
        Callers must pass arguments as keyword arguments.
<br>

<br>
        Args:
<br>
            cache_dir: `str`, directory to read/write data. Defaults to "~/datasets".
<br>
            name: `str` name, optional configuration for the dataset that affects the data generated on disk. Different
<br>
                `builder_config`s will have their own subdirectories and versions.
<br>
                If not provided, uses the first configuration in self.BUILDER_CONFIGS
<br>
            hash: a hash specific to the dataset code. Used to update the caching directory when the dataset loading
<br>
                script code is updated (to avoid reusing old data).
<br>
                The typical caching directory (defined in ``self._relative_data_dir``) is: ``name/version/hash/``
<br>
            base_path: `str`, base path for relative paths that are used to download files. This can be a remote url.
<br>
            features: `Features`, optional features that will be used to read/write the dataset
<br>
                It can be used to changed the :obj:`datasets.Features` description of a dataset for example.
<br>
            config_kwargs: will override the defaults kwargs in config
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:manual_download_instructions' href='parser/test3/builder.py#L288'>DatasetBuilder:manual_download_instructions</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:get_all_exported_dataset_infos' href='parser/test3/builder.py#L292'>DatasetBuilder:get_all_exported_dataset_infos</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br></ul>
        <li>Docs:<br>        """Empty dict if doesn't exist"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:get_exported_dataset_info' href='parser/test3/builder.py#L299'>DatasetBuilder:get_exported_dataset_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Empty DatasetInfo if doesn't exist"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_create_builder_config' href='parser/test3/builder.py#L303'>DatasetBuilder:_create_builder_config</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>name = None,<br>custom_features = None,<br>**config_kwargs,<br></ul>
        <li>Docs:<br>        """Create and validate BuilderConfig object as well as a unique config id for this config.
<br>
        Raises ValueError if there are multiple builder configs and name and DEFAULT_CONFIG_NAME are None.
<br>
        config_kwargs override the defaults kwargs in config
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:builder_configs' href='parser/test3/builder.py#L376'>DatasetBuilder:builder_configs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br></ul>
        <li>Docs:<br>        """Pre-defined list of configurations for this builder class."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:cache_dir' href='parser/test3/builder.py#L385'>DatasetBuilder:cache_dir</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_relative_data_dir' href='parser/test3/builder.py#L388'>DatasetBuilder:_relative_data_dir</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>with_version = True,<br>with_hash = True,<br></ul>
        <li>Docs:<br>        """Relative path of this dataset in cache_dir:
<br>
        Will be:
<br>
            self.name/self.config.version/self.hash/
<br>
        If any of these element is missing or if ``with_version=False`` the corresponding subfolders are dropped.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_build_cache_dir' href='parser/test3/builder.py#L406'>DatasetBuilder:_build_cache_dir</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Return the data directory for the current version."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_info' href='parser/test3/builder.py#L445'>DatasetBuilder:_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Construct the DatasetInfo object. See `DatasetInfo` for details.
<br>

<br>
        Warning: This function is only called once and the result is cached for all
<br>
        following .info() calls.
<br>

<br>
        Returns:
<br>
            info: (DatasetInfo) The dataset information
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:get_imported_module_dir' href='parser/test3/builder.py#L457'>DatasetBuilder:get_imported_module_dir</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br></ul>
        <li>Docs:<br>        """Return the path of the module of this class or subclass."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:download_and_prepare' href='parser/test3/builder.py#L461'>DatasetBuilder:download_and_prepare</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>download_config:  Optional[DownloadConfig]  =  None,<br>download_mode:  Optional[GenerateMode]  =  None,<br>ignore_verifications:  bool  =  False,<br>try_from_hf_gcs:  bool  =  True,<br>dl_manager:  Optional[DownloadManager]  =  None,<br>base_path:  Optional[str]  =  None,<br>use_auth_token:  Optional[Union[bool,<br>str]]  =  None,<br>**download_and_prepare_kwargs,<br>,<br></ul>
        <li>Docs:<br>        """Downloads and prepares dataset for reading.
<br>

<br>
        Args:
<br>
            download_config (Optional ``datasets.DownloadConfig``: specific download configuration parameters.
<br>
            download_mode (Optional `datasets.GenerateMode`): select the download/generate mode - Default to REUSE_DATASET_IF_EXISTS
<br>
            ignore_verifications (bool): Ignore the verifications of the downloaded/processed dataset information (checksums/size/splits/...)
<br>
            save_infos (bool): Save the dataset information (checksums/size/splits/...)
<br>
            try_from_hf_gcs (bool): If True, it will try to download the already prepared dataset from the Hf google cloud storage
<br>
            dl_manager (Optional ``datasets.DownloadManager``): specific Download Manger to use
<br>
            base_path ( Optional ``str``): base path for relative paths that are used to download files. This can be a remote url.
<br>
                If not specified, the value of the ``base_path`` attribute (``self.base_path``) will be used instead.
<br>
            use_auth_token (Optional ``Union[str, bool]``): Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
<br>
                If True, will get token from ~/.huggingface.
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_download_prepared_from_hf_gcs' href='parser/test3/builder.py#L601'>DatasetBuilder:_download_prepared_from_hf_gcs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>download_config:  DownloadConfig,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_download_and_prepare' href='parser/test3/builder.py#L623'>DatasetBuilder:_download_and_prepare</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager,<br>verify_infos,<br>**prepare_split_kwargs,<br></ul>
        <li>Docs:<br>        """Downloads and prepares dataset for reading.
<br>

<br>
        This is the internal implementation to overwrite called when user calls
<br>
        `download_and_prepare`. It should download all required data and generate
<br>
        the pre-processed datasets files.
<br>

<br>
        Args:
<br>
            dl_manager: (DownloadManager) `DownloadManager` used to download and cache
<br>
                data.
<br>
            verify_infos: bool, if False, do not perform checksums and size tests.
<br>
            prepare_split_kwargs: Additional options.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:download_post_processing_resources' href='parser/test3/builder.py#L677'>DatasetBuilder:download_post_processing_resources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_load_info' href='parser/test3/builder.py#L693'>DatasetBuilder:_load_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_save_info' href='parser/test3/builder.py#L696'>DatasetBuilder:_save_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_save_infos' href='parser/test3/builder.py#L701'>DatasetBuilder:_save_infos</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_make_split_generators_kwargs' href='parser/test3/builder.py#L706'>DatasetBuilder:_make_split_generators_kwargs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>prepare_split_kwargs,<br></ul>
        <li>Docs:<br>        """Get kwargs for `self._split_generators()` from `prepare_split_kwargs`."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:as_dataset' href='parser/test3/builder.py#L711'>DatasetBuilder:as_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split:  Optional[Split]  =  None,<br>run_post_process = True,<br>ignore_verifications = False,<br>in_memory = False,<br></ul>
        <li>Docs:<br>        """Return a Dataset for the specified split.
<br>

<br>
        Args:
<br>
            split (`datasets.Split`): Which subset of the data to return.
<br>
            run_post_process (bool, default=True): Whether to run post-processing dataset transforms and/or add
<br>
                indexes.
<br>
            ignore_verifications (bool, default=False): Whether to ignore the verifications of the
<br>
                downloaded/processed dataset information (checksums/size/splits/...).
<br>
            in_memory (bool, default=False): Whether to copy the data in-memory.
<br>

<br>
        Returns:
<br>
            datasets.Dataset
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_build_single_dataset' href='parser/test3/builder.py#L760'>DatasetBuilder:_build_single_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split:  Union[str,<br>ReadInstruction,<br>Split],<br>run_post_process:  bool,<br>ignore_verifications:  bool,<br>in_memory:  bool  =  False,<br>,<br></ul>
        <li>Docs:<br>        """as_dataset for a single split."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_as_dataset' href='parser/test3/builder.py#L836'>DatasetBuilder:_as_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split:  Union[ReadInstruction,<br>Split]  =  Split.TRAIN,<br>in_memory:  bool  =  False,<br></ul>
        <li>Docs:<br>        """Constructs a `Dataset`.
<br>

<br>
        This is the internal implementation to overwrite called when user calls
<br>
        `as_dataset`. It should read the pre-processed datasets files and generate
<br>
        the `Dataset` object.
<br>

<br>
        Args:
<br>
            split: `datasets.Split` which subset of the data to read.
<br>
            in_memory (bool, default False): Whether to copy the data in-memory.
<br>

<br>
        Returns:
<br>
            `Dataset`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_get_dataset_fingerprint' href='parser/test3/builder.py#L860'>DatasetBuilder:_get_dataset_fingerprint</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split:  Union[ReadInstruction,<br>Split],<br></ul>
        <li>Docs:<br>        """The dataset fingerprint is the hash of the relative directory dataset_name/config_name/version/hash, as well as the split specs."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:as_streaming_dataset' href='parser/test3/builder.py#L868'>DatasetBuilder:as_streaming_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split:  Optional[str]  =  None,<br>base_path:  Optional[str]  =  None,<br>use_auth_token:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_as_streaming_dataset_single' href='parser/test3/builder.py#L909'>DatasetBuilder:_as_streaming_dataset_single</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>splits_generator,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_post_process' href='parser/test3/builder.py#L916'>DatasetBuilder:_post_process</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset:  Dataset,<br>resources_paths:  Dict[str,<br>str],<br></ul>
        <li>Docs:<br>        """Run dataset transforms or add indexes"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_post_processing_resources' href='parser/test3/builder.py#L920'>DatasetBuilder:_post_processing_resources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split:  str,<br></ul>
        <li>Docs:<br>        """Mapping resource_name -> resource_file_name"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_download_post_processing_resources' href='parser/test3/builder.py#L924'>DatasetBuilder:_download_post_processing_resources</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split:  str,<br>resource_name:  str,<br>dl_manager:  DownloadManager,<br></ul>
        <li>Docs:<br>        """Download the resource using the download manager and return the downloaded path"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_split_generators' href='parser/test3/builder.py#L930'>DatasetBuilder:_split_generators</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager:  DownloadManager,<br></ul>
        <li>Docs:<br>        """Specify feature dictionary generators and dataset splits.
<br>

<br>
        This function returns a list of `SplitGenerator`s defining how to generate
<br>
        data and what splits to use.
<br>

<br>
        Example:
<br>

<br>
            return [
<br>
                    datasets.SplitGenerator(
<br>
                            name=datasets.Split.TRAIN,
<br>
                            gen_kwargs={'file': 'train_data.zip'},
<br>
                    ),
<br>
                    datasets.SplitGenerator(
<br>
                            name=datasets.Split.TEST,
<br>
                            gen_kwargs={'file': 'test_data.zip'},
<br>
                    ),
<br>
            ]
<br>

<br>
        The above code will first call `_generate_examples(file='train_data.zip')`
<br>
        to write the train data, then `_generate_examples(file='test_data.zip')` to
<br>
        write the test data.
<br>

<br>
        Datasets are typically split into different subsets to be used at various
<br>
        stages of training and evaluation.
<br>

<br>
        Note that for datasets without a `VALIDATION` split, you can use a
<br>
        fraction of the `TRAIN` data for evaluation as you iterate on your model
<br>
        so as not to overfit to the `TEST` data.
<br>

<br>
        For downloads and extractions, use the given `download_manager`.
<br>
        Note that the `DownloadManager` caches downloads, so it is fine to have each
<br>
        generator attempt to download the source data.
<br>

<br>
        A good practice is to download all data in this function, and then
<br>
        distribute the relevant parts to each split with the `gen_kwargs` argument
<br>

<br>
        Args:
<br>
            dl_manager: (DownloadManager) Download manager to download the data
<br>

<br>
        Returns:
<br>
            `list<SplitGenerator>`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_prepare_split' href='parser/test3/builder.py#L976'>DatasetBuilder:_prepare_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_generator:  SplitGenerator,<br>**kwargs,<br></ul>
        <li>Docs:<br>        """Generate the examples and record them on disk.
<br>

<br>
        Args:
<br>
            split_generator: `SplitGenerator`, Split generator to process
<br>
            **kwargs: Additional kwargs forwarded from _download_and_prepare (ex:
<br>
                beam pipeline)
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:DatasetBuilder:_get_examples_iterable_for_split' href='parser/test3/builder.py#L986'>DatasetBuilder:_get_examples_iterable_for_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_generator:  SplitGenerator,<br></ul>
        <li>Docs:<br>        """Generate the examples on the fly.
<br>

<br>
        Args:
<br>
            split_generator: `SplitGenerator`, Split generator to process
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:GeneratorBasedBuilder:__init__' href='parser/test3/builder.py#L1013'>GeneratorBasedBuilder:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>writer_batch_size = None,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:GeneratorBasedBuilder:_generate_examples' href='parser/test3/builder.py#L1022'>GeneratorBasedBuilder:_generate_examples</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>**kwargs,<br></ul>
        <li>Docs:<br>        """Default function generating examples for each `SplitGenerator`.
<br>

<br>
        This function preprocess the examples from the raw data to the preprocessed
<br>
        dataset files.
<br>
        This function is called once for each `SplitGenerator` defined in
<br>
        `_split_generators`. The examples yielded here will be written on
<br>
        disk.
<br>

<br>
        Args:
<br>
            **kwargs: `dict`, Arguments forwarded from the SplitGenerator.gen_kwargs
<br>

<br>
        Yields:
<br>
            key: `str` or `int`, a unique deterministic example identification key.
<br>
                * Unique: An error will be raised if two examples are yield with the
<br>
                    same key.
<br>
                * Deterministic: When generating the dataset twice, the same example
<br>
                    should have the same key.
<br>
                Good keys can be the image id, or line number if examples are extracted
<br>
                from a text file.
<br>
                The key will be hashed and sorted to shuffle examples deterministically,
<br>
                such as generating the dataset multiple times keep examples in the
<br>
                same order.
<br>
            example: `dict<str feature_name, feature_value>`, a feature dictionary
<br>
                ready to be encoded and written to disk. The example will be
<br>
                encoded with `self.info.features.encode_example({...})`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:GeneratorBasedBuilder:_prepare_split' href='parser/test3/builder.py#L1051'>GeneratorBasedBuilder:_prepare_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_generator,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:GeneratorBasedBuilder:_get_examples_iterable_for_split' href='parser/test3/builder.py#L986'>GeneratorBasedBuilder:_get_examples_iterable_for_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_generator:  SplitGenerator,<br></ul>
        <li>Docs:<br>        """Generate the examples on the fly.
<br>

<br>
        Args:
<br>
            split_generator: `SplitGenerator`, Split generator to process
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:ArrowBasedBuilder:_generate_tables' href='parser/test3/builder.py#L1093'>ArrowBasedBuilder:_generate_tables</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>**kwargs,<br></ul>
        <li>Docs:<br>        """Default function generating examples for each `SplitGenerator`.
<br>

<br>
        This function preprocess the examples from the raw data to the preprocessed
<br>
        dataset files.
<br>
        This function is called once for each `SplitGenerator` defined in
<br>
        `_split_generators`. The examples yielded here will be written on
<br>
        disk.
<br>

<br>
        Args:
<br>
            **kwargs: `dict`, Arguments forwarded from the SplitGenerator.gen_kwargs
<br>

<br>
        Yields:
<br>
            key: `str` or `int`, a unique deterministic example identification key.
<br>
                * Unique: An error will be raised if two examples are yield with the
<br>
                    same key.
<br>
                * Deterministic: When generating the dataset twice, the same example
<br>
                    should have the same key.
<br>
                Good keys can be the image id, or line number if examples are extracted
<br>
                from a text file.
<br>
                The key will be hashed and sorted to shuffle examples deterministically,
<br>
                such as generating the dataset multiple times keep examples in the
<br>
                same order.
<br>
            example: `pyarrow.Table`, a feature table
<br>
                ready to be encoded and written to disk.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:ArrowBasedBuilder:_prepare_split' href='parser/test3/builder.py#L1051'>ArrowBasedBuilder:_prepare_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_generator,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:ArrowBasedBuilder:_get_examples_iterable_for_split' href='parser/test3/builder.py#L986'>ArrowBasedBuilder:_get_examples_iterable_for_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_generator:  SplitGenerator,<br></ul>
        <li>Docs:<br>        """Generate the examples on the fly.
<br>

<br>
        Args:
<br>
            split_generator: `SplitGenerator`, Split generator to process
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:BeamBasedBuilder:__init__' href='parser/test3/builder.py#L1154'>BeamBasedBuilder:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:BeamBasedBuilder:_make_split_generators_kwargs' href='parser/test3/builder.py#L706'>BeamBasedBuilder:_make_split_generators_kwargs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>prepare_split_kwargs,<br></ul>
        <li>Docs:<br>        """Get kwargs for `self._split_generators()` from `prepare_split_kwargs`."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:BeamBasedBuilder:_build_pcollection' href='parser/test3/builder.py#L1171'>BeamBasedBuilder:_build_pcollection</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pipeline,<br>**kwargs,<br></ul>
        <li>Docs:<br>        """Build the beam pipeline examples for each `SplitGenerator`.
<br>

<br>
        This function extracts examples from the raw data with parallel transforms
<br>
        in a Beam pipeline. It is called once for each `SplitGenerator` defined in
<br>
        `_split_generators`. The examples from the PCollection will be
<br>
        encoded and written to disk.
<br>

<br>
        Warning: When running in a distributed setup, make sure that the data
<br>
        which will be read (download_dir, manual_dir,...) and written (cache_dir)
<br>
        can be accessed by the workers jobs. The data should be located in a
<br>
        shared filesystem, like GCS.
<br>

<br>
        Example:
<br>

<br>
        ```
<br>
        def _build_pcollection(pipeline, extracted_dir):
<br>
            return (
<br>
                    pipeline
<br>
                    | beam.Create(gfile.io.listdir(extracted_dir))
<br>
                    | beam.Map(_process_file)
<br>
            )
<br>
        ```
<br>

<br>
        Args:
<br>
            pipeline: `beam.Pipeline`, root Beam pipeline
<br>
            **kwargs: Arguments forwarded from the SplitGenerator.gen_kwargs
<br>

<br>
        Returns:
<br>
            pcollection: `PCollection`, an Apache Beam PCollection containing the
<br>
                example to send to `self.info.features.encode_example(...)`.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:BeamBasedBuilder:_download_and_prepare' href='parser/test3/builder.py#L1205'>BeamBasedBuilder:_download_and_prepare</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager,<br>verify_infos,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:BeamBasedBuilder:_save_info' href='parser/test3/builder.py#L696'>BeamBasedBuilder:_save_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Get kwargs for `self._split_generators()` from `prepare_split_kwargs`."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/builder.py:BeamBasedBuilder:_prepare_split' href='parser/test3/builder.py#L1269'>BeamBasedBuilder:_prepare_split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_generator,<br>pipeline,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/tasks/summarization.py' href='parser/test3/tasks/summarization.py'>parser/test3/tasks/summarization.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/tasks/summarization.py:Summarization' href='parser/test3/tasks/summarization.py#L9'>Summarization</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/tasks/summarization.py:Summarization:column_mapping' href='parser/test3/tasks/summarization.py#L18'>Summarization:column_mapping</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test/keys.py' href='parser/test/keys.py'>parser/test/keys.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:prepare_target_and_clean_up_test' href='parser/test/keys.py#L376'>prepare_target_and_clean_up_test</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """Set up target init and clean up test config."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:clean_up_config_test' href='parser/test/keys.py#L396'>clean_up_config_test</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """Clean up configuration after testing."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:check_default_network_config' href='parser/test/keys.py#L406'>check_default_network_config</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br></ul>
        <li>Docs:<br>    """Check and set default network config."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:check_module_env' href='parser/test/keys.py#L447'>check_module_env</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """Verify information about module status and network status."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:provision_certificates_to_target' href='parser/test/keys.py#L474'>provision_certificates_to_target</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>auth,<br>nist,<br>root_ca_path,<br>client_cert_path,<br>client_key_path,<br></ul>
        <li>Docs:<br>    """Provide certificates to target."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:config_session_connection' href='parser/test/keys.py#L491'>config_session_connection</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br>sid = 1,<br></ul>
        <li>Docs:<br>    """Session configuration."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:config_cipher_suite_and_tcps_action' href='parser/test/keys.py#L495'>config_cipher_suite_and_tcps_action</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>auth,<br>nist_value,<br>profile_id = 0,<br>config_cipher = 1,<br>valid = 1,<br></ul>
        <li>Docs:<br>    """Verify TCPS operations by using specified cipher suite."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0001' href='parser/test/keys.py#L511'>L_RTOS_KTCPTLS_0001</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Server authentication.
<br>
    No certificates loaded. Should not connect to server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0002' href='parser/test/keys.py#L534'>L_RTOS_KTCPTLS_0002</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Server authentication.
<br>
    Server Root CA loaded. Connects to server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0003' href='parser/test/keys.py#L555'>L_RTOS_KTCPTLS_0003</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Server authentication.
<br>
    Server Root CA, Client key, Client root CA loaded. Connects to
<br>
    server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0004' href='parser/test/keys.py#L576'>L_RTOS_KTCPTLS_0004</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    No certificates loaded. Should not connect to server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0005' href='parser/test/keys.py#L596'>L_RTOS_KTCPTLS_0005</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA loaded. Should not connect to server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0006' href='parser/test/keys.py#L616'>L_RTOS_KTCPTLS_0006</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA loaded. Client root CA loaded. Should not connect to
<br>
    server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0014' href='parser/test/keys.py#L637'>L_RTOS_KTCPTLS_0014</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256
<br>
    (AT+KSSLCRYPTO=0,8,1,8192,4,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0016' href='parser/test/keys.py#L659'>L_RTOS_KTCPTLS_0016</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-128-GCM-
<br>
    SHA256 (AT+KSSLCRYPTO=0,8,2,8192,4,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0017' href='parser/test/keys.py#L681'>L_RTOS_KTCPTLS_0017</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-256-GCM-
<br>
    SHA384 (AT+KSSLCRYPTO=0,8,2,16384,8,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0018' href='parser/test/keys.py#L703'>L_RTOS_KTCPTLS_0018</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-128-CCM
<br>
    (AT+KSSLCRYPTO=0,8,2,16,0,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0019' href='parser/test/keys.py#L725'>L_RTOS_KTCPTLS_0019</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-256-CCM
<br>
    (AT+KSSLCRYPTO=0,8,2,32,0,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0020' href='parser/test/keys.py#L747'>L_RTOS_KTCPTLS_0020</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-128-CCM-8
<br>
    (AT+KSSLCRYPTO=0,8,2,256,0,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0021' href='parser/test/keys.py#L769'>L_RTOS_KTCPTLS_0021</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-256-CCM-8
<br>
    (AT+KSSLCRYPTO=0,8,2,512,0,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/keys.py:L_RTOS_KTCPTLS_0022' href='parser/test/keys.py#L791'>L_RTOS_KTCPTLS_0022</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Module as Server.
<br>
    Server certicate, Server key loaded.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test/keys.py:BadSignatureError' href='parser/test/keys.py#L14'>BadSignatureError</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test/keys.py:BadDigestError' href='parser/test/keys.py#L18'>BadDigestError</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test/keys.py:VerifyingKey' href='parser/test/keys.py#L22'>VerifyingKey</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test/keys.py:SigningKey' href='parser/test/keys.py#L145'>SigningKey</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:__init__' href='parser/test/keys.py#L23'>VerifyingKey:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>_error__please_use_generate = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:from_public_point' href='parser/test/keys.py#L29'>VerifyingKey:from_public_point</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>point,<br>curve = NIST192p,<br>hashfunc = sha1,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:from_string' href='parser/test/keys.py#L38'>VerifyingKey:from_string</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>string,<br>curve = NIST192p,<br>hashfunc = sha1,<br>validate_point = True,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:from_pem' href='parser/test/keys.py#L56'>VerifyingKey:from_pem</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>string,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:from_der' href='parser/test/keys.py#L60'>VerifyingKey:from_der</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>string,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:from_public_key_recovery' href='parser/test/keys.py#L83'>VerifyingKey:from_public_key_recovery</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>signature,<br>data,<br>curve,<br>hashfunc = sha1,<br>sigdecode = sigdecode_string,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:from_public_key_recovery_with_digest' href='parser/test/keys.py#L91'>VerifyingKey:from_public_key_recovery_with_digest</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>signature,<br>digest,<br>curve,<br>hashfunc = sha1,<br>sigdecode = sigdecode_string,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:to_string' href='parser/test/keys.py#L106'>VerifyingKey:to_string</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:to_pem' href='parser/test/keys.py#L115'>VerifyingKey:to_pem</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:to_der' href='parser/test/keys.py#L118'>VerifyingKey:to_der</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:verify' href='parser/test/keys.py#L127'>VerifyingKey:verify</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>signature,<br>data,<br>hashfunc = None,<br>sigdecode = sigdecode_string,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:VerifyingKey:verify_digest' href='parser/test/keys.py#L132'>VerifyingKey:verify_digest</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>signature,<br>digest,<br>sigdecode = sigdecode_string,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:__init__' href='parser/test/keys.py#L23'>SigningKey:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>_error__please_use_generate = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:generate' href='parser/test/keys.py#L151'>SigningKey:generate</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>curve = NIST192p,<br>entropy = None,<br>hashfunc = sha1,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:from_secret_exponent' href='parser/test/keys.py#L161'>SigningKey:from_secret_exponent</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>secexp,<br>curve = NIST192p,<br>hashfunc = sha1,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:from_string' href='parser/test/keys.py#L178'>SigningKey:from_string</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>string,<br>curve = NIST192p,<br>hashfunc = sha1,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:from_pem' href='parser/test/keys.py#L184'>SigningKey:from_pem</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>string,<br>hashfunc = sha1,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:from_der' href='parser/test/keys.py#L193'>SigningKey:from_der</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>klass,<br>string,<br>hashfunc = sha1,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:to_string' href='parser/test/keys.py#L106'>SigningKey:to_string</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:to_pem' href='parser/test/keys.py#L115'>SigningKey:to_pem</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:to_der' href='parser/test/keys.py#L118'>SigningKey:to_der</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:get_verifying_key' href='parser/test/keys.py#L250'>SigningKey:get_verifying_key</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:sign_deterministic' href='parser/test/keys.py#L253'>SigningKey:sign_deterministic</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data,<br>hashfunc = None,<br>sigencode = sigencode_string,<br>extra_entropy = b'',<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:sign_digest_deterministic' href='parser/test/keys.py#L263'>SigningKey:sign_digest_deterministic</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>digest,<br>hashfunc = None,<br>sigencode = sigencode_string,<br>extra_entropy = b'',<br></ul>
        <li>Docs:<br>        """
<br>
        Calculates 'k' from data itself, removing the need for strong
<br>
        random generator and producing deterministic (reproducible) signatures.
<br>
        See RFC 6979 for more details.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:sign' href='parser/test/keys.py#L289'>SigningKey:sign</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data,<br>hashfunc = None,<br>sigencode = sigencode_string,<br>extra_entropy = b'',<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:sign_digest' href='parser/test/keys.py#L306'>SigningKey:sign_digest</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>digest,<br>hashfunc = None,<br>sigencode = sigencode_string,<br>extra_entropy = b'',<br></ul>
        <li>Docs:<br>"""Automation of L_RTOS_KTCPTLS_*."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test/keys.py:SigningKey:sign_number' href='parser/test/keys.py#L315'>SigningKey:sign_number</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>number,<br>entropy = None,<br>k = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/tasks/__init__.py' href='parser/test3/tasks/__init__.py'>parser/test3/tasks/__init__.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/tasks/__init__.py:task_template_from_dict' href='parser/test3/tasks/__init__.py#L30'>task_template_from_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>task_template_dict:  dict,<br></ul>
        <li>Docs:<br>    """Create one of the supported task templates in :py:mod:`datasets.tasks` from a dictionary."""
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/version.py' href='parser/test3/utils/version.py'>parser/test3/utils/version.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/version.py:_str_to_version' href='parser/test3/utils/version.py#L109'>_str_to_version</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>version_str,<br>allow_wildcard = False,<br></ul>
        <li>Docs:<br>    """Return the tuple (major, minor, patch) version extracted from the str."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/version.py:Version' href='parser/test3/utils/version.py#L31'>Version</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:__post_init__' href='parser/test3/utils/version.py#L52'>Version:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:__repr__' href='parser/test3/utils/version.py#L55'>Version:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:tuple' href='parser/test3/utils/version.py#L59'>Version:tuple</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:_validate_operand' href='parser/test3/utils/version.py#L62'>Version:_validate_operand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:__eq__' href='parser/test3/utils/version.py#L69'>Version:__eq__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:__ne__' href='parser/test3/utils/version.py#L73'>Version:__ne__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:__lt__' href='parser/test3/utils/version.py#L77'>Version:__lt__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:__le__' href='parser/test3/utils/version.py#L81'>Version:__le__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:__gt__' href='parser/test3/utils/version.py#L85'>Version:__gt__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:__ge__' href='parser/test3/utils/version.py#L89'>Version:__ge__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:match' href='parser/test3/utils/version.py#L93'>Version:match</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other_version,<br></ul>
        <li>Docs:<br>        """Returns True if other_version matches.
<br>

<br>
        Args:
<br>
            other_version: string, of the form "x[.y[.x]]" where {x,y,z} can be a
<br>
                number or a wildcard.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/version.py:Version:from_dict' href='parser/test3/utils/version.py#L104'>Version:from_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>dic,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/packaged_modules/text/text.py' href='parser/test3/packaged_modules/text/text.py'>parser/test3/packaged_modules/text/text.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/packaged_modules/text/text.py:TextConfig' href='parser/test3/packaged_modules/text/text.py#L13'>TextConfig</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/packaged_modules/text/text.py:Text' href='parser/test3/packaged_modules/text/text.py#L22'>Text</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/text/text.py:Text:_info' href='parser/test3/packaged_modules/text/text.py#L25'>Text:_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/text/text.py:Text:_split_generators' href='parser/test3/packaged_modules/text/text.py#L28'>Text:_split_generators</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager,<br></ul>
        <li>Docs:<br>        """The `data_files` kwarg in load_dataset() can be a str, List[str], Dict[str,str], or Dict[str,List[str]].
<br>

<br>
        If str or List[str], then the dataset returns only the 'train' split.
<br>
        If dict, then keys should be from the `datasets.Split` enum.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/text/text.py:Text:_generate_tables' href='parser/test3/packaged_modules/text/text.py#L49'>Text:_generate_tables</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>files,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/io/csv.py' href='parser/test3/io/csv.py'>parser/test3/io/csv.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/io/csv.py:CsvDatasetReader' href='parser/test3/io/csv.py#L11'>CsvDatasetReader</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/io/csv.py:CsvDatasetWriter' href='parser/test3/io/csv.py#L55'>CsvDatasetWriter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/csv.py:CsvDatasetReader:__init__' href='parser/test3/io/csv.py#L12'>CsvDatasetReader:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_or_paths:  NestedDataStructureLike[PathLike],<br>split:  Optional[NamedSplit]  =  None,<br>features:  Optional[Features]  =  None,<br>cache_dir:  str  =  None,<br>keep_in_memory:  bool  =  False,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/csv.py:CsvDatasetReader:read' href='parser/test3/io/csv.py#L32'>CsvDatasetReader:read</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/csv.py:CsvDatasetWriter:__init__' href='parser/test3/io/csv.py#L12'>CsvDatasetWriter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset:  Dataset,<br>path_or_buf:  Union[PathLike,<br>BinaryIO],<br>batch_size:  Optional[int]  =  None,<br>**to_csv_kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/csv.py:CsvDatasetWriter:write' href='parser/test3/io/csv.py#L68'>CsvDatasetWriter:write</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/io/csv.py:CsvDatasetWriter:_write' href='parser/test3/io/csv.py#L78'>CsvDatasetWriter:_write</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>file_obj:  BinaryIO,<br>batch_size:  int,<br>header:  bool  =  True,<br>encoding:  str  =  "utf-8",<br>**to_csv_kwargs,<br></ul>
        <li>Docs:<br>        """Writes the pyarrow table as CSV to a binary file handle.
<br>

<br>
        Caller is responsible for opening and closing the handle.
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/logging.py' href='parser/test3/utils/logging.py'>parser/test3/utils/logging.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:_get_default_logging_level' href='parser/test3/utils/logging.py#L41'>_get_default_logging_level</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """
<br>
    If DATASETS_VERBOSITY env var is set to one of the valid choices return that as the new default level.
<br>
    If it is not - fall back to ``_default_log_level``
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:_get_library_name' href='parser/test3/utils/logging.py#L58'>_get_library_name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:_get_library_root_logger' href='parser/test3/utils/logging.py#L62'>_get_library_root_logger</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:_configure_library_root_logger' href='parser/test3/utils/logging.py#L66'>_configure_library_root_logger</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:_reset_library_root_logger' href='parser/test3/utils/logging.py#L72'>_reset_library_root_logger</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:get_logger' href='parser/test3/utils/logging.py#L77'>get_logger</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>name:  Optional[str]  =  None,<br></ul>
        <li>Docs:<br>    """Return a logger with the specified name.
<br>
    This function can be used in dataset and metrics scripts.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:get_verbosity' href='parser/test3/utils/logging.py#L86'>get_verbosity</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Return the current level for the HuggingFace datasets library's root logger.
<br>
    Returns:
<br>
        Logging level, e.g., ``datasets.logging.DEBUG`` and ``datasets.logging.INFO``.
<br>
    .. note::
<br>
        HuggingFace datasets library has following logging levels:
<br>
        - ``datasets.logging.CRITICAL``, ``datasets.logging.FATAL``
<br>
        - ``datasets.logging.ERROR``
<br>
        - ``datasets.logging.WARNING``, ``datasets.logging.WARN``
<br>
        - ``datasets.logging.INFO``
<br>
        - ``datasets.logging.DEBUG``
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:set_verbosity' href='parser/test3/utils/logging.py#L101'>set_verbosity</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>verbosity:  int,<br></ul>
        <li>Docs:<br>    """Set the level for the HuggingFace datasets library's root logger.
<br>
    Args:
<br>
        verbosity:
<br>
            Logging level, e.g., ``datasets.logging.DEBUG`` and ``datasets.logging.INFO``.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:set_verbosity_info' href='parser/test3/utils/logging.py#L110'>set_verbosity_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Set the level for the HuggingFace datasets library's root logger to INFO.
<br>

<br>
    This will display most of the logging information and tqdm bars.
<br>

<br>
    Shortcut to ``datasets.logging.set_verbosity(datasets.logging.INFO)``
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:set_verbosity_warning' href='parser/test3/utils/logging.py#L120'>set_verbosity_warning</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Set the level for the HuggingFace datasets library's root logger to WARNING.
<br>

<br>
    This will display only the warning and errors logging information (no tqdm bars).
<br>

<br>
    Shortcut to ``datasets.logging.set_verbosity(datasets.logging.WARNING)``
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:set_verbosity_debug' href='parser/test3/utils/logging.py#L130'>set_verbosity_debug</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Set the level for the HuggingFace datasets library's root logger to DEBUG.
<br>

<br>
    This will display all the logging information and tqdm bars.
<br>

<br>
    Shortcut to ``datasets.logging.set_verbosity(datasets.logging.DEBUG)``
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:set_verbosity_error' href='parser/test3/utils/logging.py#L140'>set_verbosity_error</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Set the level for the HuggingFace datasets library's root logger to ERROR.
<br>

<br>
    This will display only the errors logging information (no tqdm bars).
<br>

<br>
    Shortcut to ``datasets.logging.set_verbosity(datasets.logging.ERROR)``
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:disable_propagation' href='parser/test3/utils/logging.py#L150'>disable_propagation</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Disable propagation of the library log outputs.
<br>
    Note that log propagation is disabled by default.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/logging.py:enable_propagation' href='parser/test3/utils/logging.py#L157'>enable_propagation</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Enable propagation of the library log outputs.
<br>
    Please disable the HuggingFace datasets library's default handler to prevent double logging if the root logger has
<br>
    been configured.
<br>
    """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/packaged_modules/csv/csv.py' href='parser/test3/packaged_modules/csv/csv.py'>parser/test3/packaged_modules/csv/csv.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/packaged_modules/csv/csv.py:CsvConfig' href='parser/test3/packaged_modules/csv/csv.py#L19'>CsvConfig</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/packaged_modules/csv/csv.py:Csv' href='parser/test3/packaged_modules/csv/csv.py#L112'>Csv</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/csv/csv.py:CsvConfig:__post_init__' href='parser/test3/packaged_modules/csv/csv.py#L60'>CsvConfig:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/csv/csv.py:CsvConfig:read_csv_kwargs' href='parser/test3/packaged_modules/csv/csv.py#L67'>CsvConfig:read_csv_kwargs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/csv/csv.py:Csv:_info' href='parser/test3/packaged_modules/csv/csv.py#L115'>Csv:_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/csv/csv.py:Csv:_split_generators' href='parser/test3/packaged_modules/csv/csv.py#L118'>Csv:_split_generators</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager,<br></ul>
        <li>Docs:<br>        """We handle string, list and dicts in datafiles"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/csv/csv.py:Csv:_generate_tables' href='parser/test3/packaged_modules/csv/csv.py#L135'>Csv:_generate_tables</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>files,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/file_utils.py' href='parser/test3/utils/file_utils.py'>parser/test3/utils/file_utils.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:init_hf_modules' href='parser/test3/utils/file_utils.py#L44'>init_hf_modules</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>hf_modules_cache:  Optional[Union[Path,<br>str]]  =  None,<br></ul>
        <li>Docs:<br>    """
<br>
    Add hf_modules_cache to the python path.
<br>
    By default hf_modules_cache='~/.cache/huggingface/modules'.
<br>
    It can also be set with the environment variable HF_MODULES_CACHE.
<br>
    This is used to add modules such as `datasets_modules`
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:temp_seed' href='parser/test3/utils/file_utils.py#L64'>temp_seed</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>seed:  int,<br>set_pytorch = False,<br>set_tensorflow = False,<br></ul>
        <li>Docs:<br>    """Temporarily set the random seed. This works for python numpy, pytorch and tensorflow."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:is_remote_url' href='parser/test3/utils/file_utils.py#L117'>is_remote_url</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url_or_filename:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:is_local_path' href='parser/test3/utils/file_utils.py#L122'>is_local_path</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url_or_filename:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:is_relative_path' href='parser/test3/utils/file_utils.py#L129'>is_relative_path</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url_or_filename:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:hf_bucket_url' href='parser/test3/utils/file_utils.py#L133'>hf_bucket_url</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>identifier:  str,<br>filename:  str,<br>use_cdn = False,<br>dataset = True,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:head_hf_s3' href='parser/test3/utils/file_utils.py#L141'>head_hf_s3</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>identifier:  str,<br>filename:  str,<br>use_cdn = False,<br>dataset = True,<br>max_retries = 0,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:hf_github_url' href='parser/test3/utils/file_utils.py#L153'>hf_github_url</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br>name:  str,<br>dataset = True,<br>version:  Optional[str]  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:hf_hub_url' href='parser/test3/utils/file_utils.py#L163'>hf_hub_url</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br>name:  str,<br>version:  Optional[str]  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:url_or_path_join' href='parser/test3/utils/file_utils.py#L168'>url_or_path_join</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>base_name:  str,<br>*pathnames:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:url_or_path_parent' href='parser/test3/utils/file_utils.py#L175'>url_or_path_parent</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url_or_path:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:hash_url_to_filename' href='parser/test3/utils/file_utils.py#L182'>hash_url_to_filename</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url,<br>etag = None,<br></ul>
        <li>Docs:<br>    """
<br>
    Convert `url` into a hashed filename in a repeatable way.
<br>
    If `etag` is specified, append its hash to the url's, delimited
<br>
    by a period.
<br>
    If the url ends with .h5 (Keras HDF5 weights) adds '.h5' to the name
<br>
    so that TF 2.0 can identify it as a HDF5 file
<br>
    (see https://github.com/tensorflow/tensorflow/blob/00fad90125b18b80fe054de1055770cfb8fe4ba3/tensorflow/python/keras/engine/network.py#L1380)
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:cached_path' href='parser/test3/utils/file_utils.py#L248'>cached_path</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url_or_filename,<br>download_config = None,<br>**download_kwargs,<br>,<br></ul>
        <li>Docs:<br>    """
<br>
    Given something that might be a URL (or might be a local path),
<br>
    determine which. If it's a URL, download the file and cache it, and
<br>
    return the path to the cached file. If it's already a local path,
<br>
    make sure the file exists and then return the path.
<br>

<br>
    Return:
<br>
        Local path (string)
<br>

<br>
    Raises:
<br>
        FileNotFoundError: in case of non-recoverable file
<br>
            (non-existent or no cache on disk)
<br>
        ConnectionError: in case of unreachable url
<br>
            and no cache on disk
<br>
        ValueError: if it couldn't parse the url or filename correctly
<br>
        requests.exceptions.ConnectionError: in case of internet connection issue
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:get_datasets_user_agent' href='parser/test3/utils/file_utils.py#L376'>get_datasets_user_agent</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>user_agent:  Optional[Union[str,<br>dict]]  =  None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:get_authentication_headers_for_url' href='parser/test3/utils/file_utils.py#L394'>get_authentication_headers_for_url</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url:  str,<br>use_auth_token:  Optional[Union[str,<br>bool]]  =  None,<br></ul>
        <li>Docs:<br>    """Handle the HF authentication"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:_raise_if_offline_mode_is_enabled' href='parser/test3/utils/file_utils.py#L414'>_raise_if_offline_mode_is_enabled</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>msg:  Optional[str]  =  None,<br></ul>
        <li>Docs:<br>    """Raise a OfflineModeIsEnabled error (subclass of ConnectionError) if HF_DATASETS_OFFLINE is True."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:_request_with_retry' href='parser/test3/utils/file_utils.py#L422'>_request_with_retry</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>method:  str,<br>url:  str,<br>max_retries:  int  =  0,<br>base_wait_time:  float  =  0.5,<br>max_wait_time:  float  =  2,<br>timeout:  float  =  10.0,<br>**params,<br>,<br></ul>
        <li>Docs:<br>    """Wrapper around requests to retry in case it fails with a ConnectTimeout, with exponential backoff.
<br>

<br>
    Note that if the environment variable HF_DATASETS_OFFLINE is set to 1, then a OfflineModeIsEnabled error is raised.
<br>

<br>
    Args:
<br>
        method (str): HTTP method, such as 'GET' or 'HEAD'
<br>
        url (str): The URL of the ressource to fetch
<br>
        max_retries (int): Maximum number of retries, defaults to 0 (no retries)
<br>
        base_wait_time (float): Duration (in seconds) to wait before retrying the first time. Wait time between
<br>
            retries then grows exponentially, capped by max_wait_time.
<br>
        max_wait_time (float): Maximum amount of time between two retries, in seconds
<br>
        **params: Params to pass to `requests.request`
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:ftp_head' href='parser/test3/utils/file_utils.py#L461'>ftp_head</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url,<br>timeout = 10.0,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:ftp_get' href='parser/test3/utils/file_utils.py#L471'>ftp_get</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url,<br>temp_file,<br>timeout = 10.0,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:http_get' href='parser/test3/utils/file_utils.py#L481'>http_get</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url,<br>temp_file,<br>proxies = None,<br>resume_size = 0,<br>headers = None,<br>cookies = None,<br>timeout = 10.0,<br>max_retries = 0,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:http_head' href='parser/test3/utils/file_utils.py#L515'>http_head</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url,<br>proxies = None,<br>headers = None,<br>cookies = None,<br>allow_redirects = True,<br>timeout = 10.0,<br>max_retries = 0,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:get_from_cache' href='parser/test3/utils/file_utils.py#L533'>get_from_cache</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url,<br>cache_dir = None,<br>force_download = False,<br>proxies = None,<br>etag_timeout = 10,<br>resume_download = False,<br>user_agent = None,<br>local_files_only = False,<br>use_etag = True,<br>max_retries = 0,<br>use_auth_token = None,<br>,<br></ul>
        <li>Docs:<br>    """
<br>
    Given a URL, look for the corresponding file in the local cache.
<br>
    If it's not there, download it. Then return the path to the cached file.
<br>

<br>
    Return:
<br>
        Local path (string)
<br>

<br>
    Raises:
<br>
        FileNotFoundError: in case of non-recoverable file
<br>
            (non-existent or no cache on disk)
<br>
        ConnectionError: in case of unreachable url
<br>
            and no cache on disk
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:is_gzip' href='parser/test3/utils/file_utils.py#L696'>is_gzip</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br></ul>
        <li>Docs:<br>    """from https://stackoverflow.com/a/60634210"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:is_xz' href='parser/test3/utils/file_utils.py#L706'>is_xz</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br></ul>
        <li>Docs:<br>    """https://tukaani.org/xz/xz-file-format-1.0.4.txt"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:is_rarfile' href='parser/test3/utils/file_utils.py#L719'>is_rarfile</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br></ul>
        <li>Docs:<br>    """https://github.com/markokr/rarfile/blob/master/rarfile.py"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:add_start_docstrings' href='parser/test3/utils/file_utils.py#L757'>add_start_docstrings</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*docstr,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:add_end_docstrings' href='parser/test3/utils/file_utils.py#L765'>add_end_docstrings</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*docstr,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/file_utils.py:estimate_dataset_size' href='parser/test3/utils/file_utils.py#L773'>estimate_dataset_size</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>paths,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/file_utils.py:DownloadConfig' href='parser/test3/utils/file_utils.py#L207'>DownloadConfig</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/file_utils.py:OfflineModeIsEnabled' href='parser/test3/utils/file_utils.py#L410'>OfflineModeIsEnabled</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/file_utils.py:ZstdExtractor' href='parser/test3/utils/file_utils.py#L732'>ZstdExtractor</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/file_utils.py:DownloadConfig:copy' href='parser/test3/utils/file_utils.py#L244'>DownloadConfig:copy</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/file_utils.py:ZstdExtractor:is_extractable' href='parser/test3/utils/file_utils.py#L734'>ZstdExtractor:is_extractable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br></ul>
        <li>Docs:<br>        """https://datatracker.ietf.org/doc/html/rfc8878
<br>

<br>
        Magic_Number:  4 bytes, little-endian format.  Value: 0xFD2FB528.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/utils/file_utils.py:ZstdExtractor:extract' href='parser/test3/utils/file_utils.py#L747'>ZstdExtractor:extract</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>input_path:  str,<br>output_path:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/generate_md.py' href='parser/generate_md.py'>parser/generate_md.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/generate_md.py:create_markdown_function' href='parser/generate_md.py#L5'>create_markdown_function</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>uri,<br>name,<br>type,<br>args_name,<br>args_type,<br>args_value,<br>start_line,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/generate_md.py:create_markdown_file' href='parser/generate_md.py#L31'>create_markdown_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>list_info,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/commands/dummy_data.py' href='parser/test3/commands/dummy_data.py'>parser/test3/commands/dummy_data.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/commands/dummy_data.py:test_command_factory' href='parser/test3/commands/dummy_data.py#L26'>test_command_factory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>args,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/commands/dummy_data.py:DummyDataGeneratorDownloadManager' href='parser/test3/commands/dummy_data.py#L40'>DummyDataGeneratorDownloadManager</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/commands/dummy_data.py:DummyDataCommand' href='parser/test3/commands/dummy_data.py#L215'>DummyDataCommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataGeneratorDownloadManager:__init__' href='parser/test3/commands/dummy_data.py#L41'>DummyDataGeneratorDownloadManager:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>mock_download_manager,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataGeneratorDownloadManager:download' href='parser/test3/commands/dummy_data.py#L47'>DummyDataGeneratorDownloadManager:download</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>url_or_urls,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataGeneratorDownloadManager:download_and_extract' href='parser/test3/commands/dummy_data.py#L54'>DummyDataGeneratorDownloadManager:download_and_extract</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>url_or_urls,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataGeneratorDownloadManager:auto_generate_dummy_data_folder' href='parser/test3/commands/dummy_data.py#L61'>DummyDataGeneratorDownloadManager:auto_generate_dummy_data_folder</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>n_lines:  int  =  5,<br>json_field:  Optional[str]  =  None,<br>xml_tag:  Optional[str]  =  None,<br>match_text_files:  Optional[str]  =  None,<br>encoding:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataGeneratorDownloadManager:_create_dummy_data' href='parser/test3/commands/dummy_data.py#L103'>DummyDataGeneratorDownloadManager:_create_dummy_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>src_path:  str,<br>dst_path:  str,<br>n_lines:  int,<br>json_field:  Optional[str]  =  None,<br>xml_tag:  Optional[str]  =  None,<br>match_text_files:  Optional[str]  =  None,<br>encoding:  Optional[str]  =  None,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataGeneratorDownloadManager:_create_xml_dummy_data' href='parser/test3/commands/dummy_data.py#L188'>DummyDataGeneratorDownloadManager:_create_xml_dummy_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>src_path,<br>dst_path,<br>xml_tag,<br>n_lines = 5,<br>encoding = DEFAULT_ENCODING,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataGeneratorDownloadManager:compress_autogenerated_dummy_data' href='parser/test3/commands/dummy_data.py#L206'>DummyDataGeneratorDownloadManager:compress_autogenerated_dummy_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_to_dataset,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataCommand:register_subcommand' href='parser/test3/commands/dummy_data.py#L217'>DummyDataCommand:register_subcommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>parser:  ArgumentParser,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataCommand:__init__' href='parser/test3/commands/dummy_data.py#L261'>DummyDataCommand:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path_to_dataset:  str,<br>auto_generate:  bool,<br>n_lines:  int,<br>json_field:  Optional[str],<br>xml_tag:  Optional[str],<br>match_text_files:  Optional[str],<br>keep_uncompressed:  bool,<br>cache_dir:  Optional[str],<br>encoding:  Optional[str],<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataCommand:run' href='parser/test3/commands/dummy_data.py#L288'>DummyDataCommand:run</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataCommand:_autogenerate_dummy_data' href='parser/test3/commands/dummy_data.py#L332'>DummyDataCommand:_autogenerate_dummy_data</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_builder,<br>mock_dl_manager,<br>keep_uncompressed,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/dummy_data.py:DummyDataCommand:_print_dummy_data_instructions' href='parser/test3/commands/dummy_data.py#L390'>DummyDataCommand:_print_dummy_data_instructions</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset_builder,<br>mock_dl_manager,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/packaged_modules/json/json.py' href='parser/test3/packaged_modules/json/json.py'>parser/test3/packaged_modules/json/json.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/packaged_modules/json/json.py:JsonConfig' href='parser/test3/packaged_modules/json/json.py#L15'>JsonConfig</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/packaged_modules/json/json.py:Json' href='parser/test3/packaged_modules/json/json.py#L37'>Json</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/json/json.py:JsonConfig:pa_read_options' href='parser/test3/packaged_modules/json/json.py#L25'>JsonConfig:pa_read_options</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/json/json.py:JsonConfig:pa_parse_options' href='parser/test3/packaged_modules/json/json.py#L29'>JsonConfig:pa_parse_options</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/json/json.py:JsonConfig:schema' href='parser/test3/packaged_modules/json/json.py#L33'>JsonConfig:schema</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/json/json.py:Json:_info' href='parser/test3/packaged_modules/json/json.py#L40'>Json:_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/json/json.py:Json:_split_generators' href='parser/test3/packaged_modules/json/json.py#L43'>Json:_split_generators</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager,<br></ul>
        <li>Docs:<br>        """We handle string, list and dicts in datafiles"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/json/json.py:Json:_generate_tables' href='parser/test3/packaged_modules/json/json.py#L60'>Json:_generate_tables</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>files,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/formatting/jax_formatter.py' href='parser/test3/formatting/jax_formatter.py'>parser/test3/formatting/jax_formatter.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/formatting/jax_formatter.py:JaxFormatter' href='parser/test3/formatting/jax_formatter.py#L30'>JaxFormatter</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/jax_formatter.py:JaxFormatter:__init__' href='parser/test3/formatting/jax_formatter.py#L31'>JaxFormatter:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>**jnp_array_kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/jax_formatter.py:JaxFormatter:_tensorize' href='parser/test3/formatting/jax_formatter.py#L35'>JaxFormatter:_tensorize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/jax_formatter.py:JaxFormatter:_recursive_tensorize' href='parser/test3/formatting/jax_formatter.py#L54'>JaxFormatter:_recursive_tensorize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data_struct:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/jax_formatter.py:JaxFormatter:recursive_tensorize' href='parser/test3/formatting/jax_formatter.py#L62'>JaxFormatter:recursive_tensorize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>data_struct:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/jax_formatter.py:JaxFormatter:format_row' href='parser/test3/formatting/jax_formatter.py#L65'>JaxFormatter:format_row</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/jax_formatter.py:JaxFormatter:format_column' href='parser/test3/formatting/jax_formatter.py#L69'>JaxFormatter:format_column</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/formatting/jax_formatter.py:JaxFormatter:format_batch' href='parser/test3/formatting/jax_formatter.py#L73'>JaxFormatter:format_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>pa_table:  pa.Table,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/inspect.py' href='parser/test3/inspect.py'>parser/test3/inspect.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/inspect.py:list_datasets' href='parser/test3/inspect.py#L30'>list_datasets</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>with_community_datasets = True,<br>with_details = False,<br></ul>
        <li>Docs:<br>    """List all the datasets scripts available on HuggingFace AWS bucket.
<br>

<br>
    Args:
<br>
        with_community_datasets (``bool``, optional, default ``True``): Include the community provided datasets.
<br>
        with_details (``bool``, optional, default ``False``): Return the full details on the datasets instead of only the short name.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/inspect.py:list_metrics' href='parser/test3/inspect.py#L41'>list_metrics</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>with_community_metrics = True,<br>with_details = False,<br></ul>
        <li>Docs:<br>    """List all the metrics script available on HuggingFace AWS bucket
<br>

<br>
    Args:
<br>
        with_community_metrics (Optional ``bool``): Include the community provided metrics (default: ``True``)
<br>
        with_details (Optional ``bool``): Return the full details on the metrics instead of only the short name (default: ``False``)
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/inspect.py:inspect_dataset' href='parser/test3/inspect.py#L52'>inspect_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br>local_path:  str,<br>download_config:  Optional[DownloadConfig]  =  None,<br>**download_kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/inspect.py:get_dataset_config_names' href='parser/test3/inspect.py#L115'>get_dataset_config_names</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br></ul>
        <li>Docs:<br>    """Get the list of available config names for a particular dataset.
<br>

<br>
    Args:
<br>
        path (``str``): path to the dataset processing script with the dataset builder. Can be either:
<br>
            - a local path to processing script or the directory containing the script (if the script has the same name as the directory),
<br>
                e.g. ``'./dataset/squad'`` or ``'./dataset/squad/squad.py'``
<br>
            - a dataset identifier on HuggingFace AWS bucket (list all available datasets and ids with ``datasets.list_datasets()``)
<br>
                e.g. ``'squad'``, ``'glue'`` or ``'openai/webtext'``
<br>
    """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/load.py' href='parser/test3/load.py'>parser/test3/load.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/load.py:init_dynamic_modules' href='parser/test3/load.py#L68'>init_dynamic_modules</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>name:  str  =  config.MODULE_NAME_FOR_DYNAMIC_MODULES,<br>hf_modules_cache:  Optional[Union[Path,<br>str]]  =  None,<br></ul>
        <li>Docs:<br>    """
<br>
    Create a module with name `name` in which you can add dynamic modules
<br>
    such as metrics or datasets. The module can be imported using its name.
<br>
    The module is created in the HF_MODULE_CACHE directory by default (~/.cache/huggingface/modules) but it can
<br>
    be overriden by specifying a path to another directory in `hf_modules_cache`.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/load.py:import_main_class' href='parser/test3/load.py#L86'>import_main_class</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>module_path,<br>dataset = True,<br></ul>
        <li>Docs:<br>    """Import a module at module_path and return its main class:
<br>
    - a DatasetBuilder if dataset is True
<br>
    - a Metric if dataset is False
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/load.py:files_to_hash' href='parser/test3/load.py#L110'>files_to_hash</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_paths:  List[str],<br></ul>
        <li>Docs:<br>    """
<br>
    Convert a list of scripts or text files provided in file_paths into a hashed filename in a repeatable way.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/load.py:convert_github_url' href='parser/test3/load.py#L130'>convert_github_url</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>url_path:  str,<br></ul>
        <li>Docs:<br>    """Convert a link to a file on a github repo in a link to the raw github object."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/load.py:get_imports' href='parser/test3/load.py#L150'>get_imports</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>file_path:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/load.py:load_dataset_builder' href='parser/test3/load.py#L629'>load_dataset_builder</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br>name:  Optional[str]  =  None,<br>data_dir:  Optional[str]  =  None,<br>data_files:  Union[Dict,<br>List]  =  None,<br>cache_dir:  Optional[str]  =  None,<br>features:  Optional[Features]  =  None,<br>download_config:  Optional[DownloadConfig]  =  None,<br>download_mode:  Optional[GenerateMode]  =  None,<br>script_version:  Optional[Union[str,<br>Version]]  =  None,<br>use_auth_token:  Optional[Union[bool,<br>str]]  =  None,<br>**config_kwargs,<br>,<br></ul>
        <li>Docs:<br>    """Load a builder for the dataset. A dataset builder can be used to inspect general information that is required to build a dataset (cache directory, config, dataset info, etc.)
<br>
    without downloading the dataset itself.
<br>

<br>
    This method will download and import the dataset loading script from ``path`` if it's not already cached inside the library.
<br>

<br>
    Args:
<br>

<br>
        path (:obj:`str`): Path to the dataset processing script with the dataset builder. Can be either:
<br>

<br>
            - a local path to processing script or the directory containing the script (if the script has the same name as the directory),
<br>
              e.g. ``'./dataset/squad'`` or ``'./dataset/squad/squad.py'``.
<br>
            - a dataset identifier in the HuggingFace Datasets Hub (list all available datasets and ids with ``datasets.list_datasets()``)
<br>
              e.g. ``'squad'``, ``'glue'`` or ``'openai/webtext'``.
<br>
        name (:obj:`str`, optional): Defining the name of the dataset configuration.
<br>
        data_dir (:obj:`str`, optional): Defining the data_dir of the dataset configuration.
<br>
        data_files (:obj:`str`, optional): Defining the data_files of the dataset configuration.
<br>
        cache_dir (:obj:`str`, optional): Directory to read/write data. Defaults to "~/datasets".
<br>
        features (:class:`Features`, optional): Set the features type to use for this dataset.
<br>
        download_config (:class:`~utils.DownloadConfig`, optional): Specific download configuration parameters.
<br>
        download_mode (:class:`GenerateMode`, optional): Select the download/generate mode - Default to REUSE_DATASET_IF_EXISTS
<br>
        script_version (:class:`~utils.Version` or :obj:`str`, optional): Version of the dataset script to load:
<br>

<br>
            - For canonical datasets in the `huggingface/datasets` library like "squad", the default version of the module is the local version fo the lib.
<br>
              You can specify a different version from your local version of the lib (e.g. "master" or "1.2.0") but it might cause compatibility issues.
<br>
            - For community provided datasets like "lhoestq/squad" that have their own git repository on the Datasets Hub, the default version "main" corresponds to the "main" branch.
<br>
              You can specify a different version that the default "main" by using a commit sha or a git tag of the dataset repository.
<br>
        use_auth_token (``str`` or ``bool``, optional): Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
<br>
            If True, will get token from `"~/.huggingface"`.
<br>

<br>
    Returns:
<br>
        :class:`DatasetBuilder`
<br>

<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/load.py:load_dataset' href='parser/test3/load.py#L710'>load_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br>name:  Optional[str]  =  None,<br>data_dir:  Optional[str]  =  None,<br>data_files:  Union[Dict,<br>List]  =  None,<br>cache_dir:  Optional[str]  =  None,<br>features:  Optional[Features]  =  None,<br>download_config:  Optional[DownloadConfig]  =  None,<br>download_mode:  Optional[GenerateMode]  =  None,<br>script_version:  Optional[Union[str,<br>Version]]  =  None,<br>use_auth_token:  Optional[Union[bool,<br>str]]  =  None,<br>**config_kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/load.py:load_from_disk' href='parser/test3/load.py#L878'>load_from_disk</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset_path:  str,<br>fs = None,<br>keep_in_memory:  Optional[bool]  =  None,<br></ul>
        <li>Docs:<br>    """
<br>
    Loads a dataset that was previously saved using ``dataset.save_to_disk(dataset_path)`` from a dataset directory, or from a filesystem using either :class:`datasets.filesystems.S3FileSystem` or any implementation of ``fsspec.spec.AbstractFileSystem``.
<br>

<br>
    Args:
<br>
        dataset_path (:obj:`str`): Path (e.g. ``"dataset/train"``) or remote uri (e.g.
<br>
            ``"s3://my-bucket/dataset/train"``) of the Dataset or DatasetDict directory where the dataset will be
<br>
            loaded from.
<br>
        fs (:class:`~filesystems.S3FileSystem` or ``fsspec.spec.AbstractFileSystem``, optional, default ``None``):
<br>
            Instance of of the remote filesystem used to download the files from.
<br>
        keep_in_memory (:obj:`bool`, default ``None``): Whether to copy the dataset in-memory. If `None`, the dataset
<br>
            will not be copied in-memory unless explicitly enabled by setting `datasets.config.IN_MEMORY_MAX_SIZE` to
<br>
            nonzero. See more details in the :ref:`load_dataset_enhancing_performance` section.
<br>

<br>
    Returns:
<br>
        ``datasets.Dataset`` or ``datasets.DatasetDict``
<br>
            if `dataset_path` is a path of a dataset directory: the dataset requested,
<br>
            if `dataset_path` is a path of a dataset dict directory: a ``datasets.DatasetDict`` with each split.
<br>
            keep_in_memory (``bool``, default False): Whether to copy the data in-memory.
<br>
    """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/arrow_reader.py' href='parser/test3/arrow_reader.py'>parser/test3/arrow_reader.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_reader.py:make_file_instructions' href='parser/test3/arrow_reader.py#L94'>make_file_instructions</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>name,<br>split_infos,<br>instruction,<br>filetype_suffix = None,<br></ul>
        <li>Docs:<br>    """Returns instructions of the split dict.
<br>

<br>
    Args:
<br>
        name: Name of the dataset.
<br>
        split_infos: `List[SplitInfo]`, Dataset splits information
<br>
        instruction: `ReadInstruction` or `str`
<br>
        filetype_suffix: `Optional[str]` suffix of dataset files, e.g. 'arrow' or 'parquet'
<br>

<br>
    Returns:
<br>
        file_intructions: FileInstructions instance
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_reader.py:_make_file_instructions_from_absolutes' href='parser/test3/arrow_reader.py#L117'>_make_file_instructions_from_absolutes</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>name,<br>name2len,<br>absolute_instructions,<br>filetype_suffix = None,<br></ul>
        <li>Docs:<br>    """Returns the files instructions from the absolute instructions list."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_reader.py:_str_to_read_instruction' href='parser/test3/arrow_reader.py#L393'>_str_to_read_instruction</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>spec,<br></ul>
        <li>Docs:<br>    """Returns ReadInstruction for given string."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_reader.py:_pct_to_abs_pct1' href='parser/test3/arrow_reader.py#L408'>_pct_to_abs_pct1</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>boundary,<br>num_examples,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_reader.py:_pct_to_abs_closest' href='parser/test3/arrow_reader.py#L419'>_pct_to_abs_closest</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>boundary,<br>num_examples,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/arrow_reader.py:_rel_to_abs_instr' href='parser/test3/arrow_reader.py#L423'>_rel_to_abs_instr</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>rel_instr,<br>name2len,<br></ul>
        <li>Docs:<br>    """Returns _AbsoluteInstruction instance for given RelativeInstruction.
<br>

<br>
    Args:
<br>
        rel_instr: RelativeInstruction instance.
<br>
        name2len: dict {split_name: num_examples}.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_reader.py:MissingFilesOnHfGcs' href='parser/test3/arrow_reader.py#L73'>MissingFilesOnHfGcs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_reader.py:FileInstructions' href='parser/test3/arrow_reader.py#L80'>FileInstructions</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_reader.py:BaseReader' href='parser/test3/arrow_reader.py#L138'>BaseReader</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_reader.py:ArrowReader' href='parser/test3/arrow_reader.py#L285'>ArrowReader</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_reader.py:ParquetReader' href='parser/test3/arrow_reader.py#L330'>ParquetReader</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_reader.py:_AbsoluteInstruction' href='parser/test3/arrow_reader.py#L362'>_AbsoluteInstruction</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_reader.py:_RelativeInstruction' href='parser/test3/arrow_reader.py#L371'>_RelativeInstruction</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/arrow_reader.py:ReadInstruction' href='parser/test3/arrow_reader.py#L457'>ReadInstruction</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:BaseReader:__init__' href='parser/test3/arrow_reader.py#L143'>BaseReader:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path:  str,<br>info:  Optional["DatasetInfo"],<br></ul>
        <li>Docs:<br>        """Initializes ArrowReader.
<br>

<br>
        Args:
<br>
            path (str): path where tfrecords are stored.
<br>
            info (DatasetInfo): info about the dataset.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:BaseReader:_get_table_from_filename' href='parser/test3/arrow_reader.py#L154'>BaseReader:_get_table_from_filename</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>filename_skip_take,<br>in_memory = False,<br></ul>
        <li>Docs:<br>        """Returns a Dataset instance from given (filename, skip, take)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:BaseReader:_read_files' href='parser/test3/arrow_reader.py#L158'>BaseReader:_read_files</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>files,<br>in_memory = False,<br></ul>
        <li>Docs:<br>        """Returns Dataset for given file instructions.
<br>

<br>
        Args:
<br>
            files: List[dict(filename, skip, take)], the files information.
<br>
                The filenames contain the absolute path, not relative.
<br>
                skip/take indicates which example read in the file: `ds.slice(skip, take)`
<br>
            in_memory (bool, default False): Whether to copy the data in-memory.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:BaseReader:get_file_instructions' href='parser/test3/arrow_reader.py#L184'>BaseReader:get_file_instructions</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>name,<br>instruction,<br>split_infos,<br></ul>
        <li>Docs:<br>        """Return list of dict {'filename': str, 'skip': int, 'take': int}"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:BaseReader:read' href='parser/test3/arrow_reader.py#L192'>BaseReader:read</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>name,<br>instructions,<br>split_infos,<br>in_memory = False,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:BaseReader:read_files' href='parser/test3/arrow_reader.py#L219'>BaseReader:read_files</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>files:  List[dict],<br>original_instructions:  Union[None,<br>"ReadInstruction",<br>"Split"]  =  None,<br>in_memory = False,<br>,<br></ul>
        <li>Docs:<br>        """Returns single Dataset instance for the set of file instructions.
<br>

<br>
        Args:
<br>
            files: List[dict(filename, skip, take)], the files information.
<br>
                The filenames contains the relative path, not absolute.
<br>
                skip/take indicates which example read in the file: `ds.skip().take()`
<br>
            original_instructions: store the original instructions used to build the dataset split in the dataset.
<br>
            in_memory (bool, default False): Whether to copy the data in-memory.
<br>

<br>
        Returns:
<br>
            kwargs to build a Dataset instance.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:BaseReader:download_from_hf_gcs' href='parser/test3/arrow_reader.py#L249'>BaseReader:download_from_hf_gcs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>download_config:  DownloadConfig,<br>relative_data_dir,<br></ul>
        <li>Docs:<br>        """
<br>
        Download the dataset files from the Hf GCS
<br>

<br>
        Args:
<br>
            dl_cache_dir: `str`, the local cache directory used to download files
<br>
            relative_data_dir: `str`, the relative directory of the remote files from
<br>
                the `datasets` directory on GCS.
<br>

<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ArrowReader:__init__' href='parser/test3/arrow_reader.py#L143'>ArrowReader:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path:  str,<br>info:  Optional["DatasetInfo"],<br></ul>
        <li>Docs:<br>        """Initializes ArrowReader.
<br>

<br>
        Args:
<br>
            path (str): path where tfrecords are stored.
<br>
            info (DatasetInfo): info about the dataset.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ArrowReader:_get_table_from_filename' href='parser/test3/arrow_reader.py#L154'>ArrowReader:_get_table_from_filename</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>filename_skip_take,<br>in_memory = False,<br></ul>
        <li>Docs:<br>        """Returns a Dataset instance from given (filename, skip, take)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ArrowReader:read_table' href='parser/test3/arrow_reader.py#L315'>ArrowReader:read_table</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>filename,<br>in_memory = False,<br></ul>
        <li>Docs:<br>        """
<br>
        Read table from file.
<br>

<br>
        Args:
<br>
            filename (str): File name of the table.
<br>
            in_memory (bool, default=False): Whether to copy the data in-memory.
<br>

<br>
        Returns:
<br>
            pyarrow.Table
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ParquetReader:__init__' href='parser/test3/arrow_reader.py#L143'>ParquetReader:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path:  str,<br>info:  Optional["DatasetInfo"],<br></ul>
        <li>Docs:<br>        """Initializes ArrowReader.
<br>

<br>
        Args:
<br>
            path (str): path where tfrecords are stored.
<br>
            info (DatasetInfo): info about the dataset.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ParquetReader:_get_table_from_filename' href='parser/test3/arrow_reader.py#L346'>ParquetReader:_get_table_from_filename</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>filename_skip_take,<br>**kwargs,<br></ul>
        <li>Docs:<br>        """Returns a Dataset instance from given (filename, skip, take)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:_RelativeInstruction:__post_init__' href='parser/test3/arrow_reader.py#L380'>_RelativeInstruction:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ReadInstruction:_init' href='parser/test3/arrow_reader.py#L498'>ReadInstruction:_init</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>relative_instructions,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ReadInstruction:_read_instruction_from_relative_instructions' href='parser/test3/arrow_reader.py#L503'>ReadInstruction:_read_instruction_from_relative_instructions</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>relative_instructions,<br></ul>
        <li>Docs:<br>        """Returns ReadInstruction obj initialized with relative_instructions."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ReadInstruction:__init__' href='parser/test3/arrow_reader.py#L510'>ReadInstruction:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_name,<br>rounding = None,<br>from_ = None,<br>to = None,<br>unit = None,<br></ul>
        <li>Docs:<br>        """Initialize ReadInstruction.
<br>

<br>
        Args:
<br>
            split_name (str): name of the split to read. Eg: 'train'.
<br>
            rounding (str, optional): The rounding behaviour to use when percent slicing is
<br>
                used. Ignored when slicing with absolute indices.
<br>
                Possible values:
<br>
                 - 'closest' (default): The specified percentages are rounded to the
<br>
                     closest value. Use this if you want specified percents to be as
<br>
                     much exact as possible.
<br>
                 - 'pct1_dropremainder': the specified percentages are treated as
<br>
                     multiple of 1%. Use this option if you want consistency. Eg:
<br>
                         len(5%) == 5 * len(1%).
<br>
                     Using this option, one might not be able to use the full set of
<br>
                     examples, if the number of those is not a multiple of 100.
<br>
            from_ (int):
<br>
            to (int): alternative way of specifying slicing boundaries. If any of
<br>
                {from_, to, unit} argument is used, slicing cannot be specified as
<br>
                string.
<br>
            unit (str): optional, one of:
<br>
                '%': to set the slicing unit as percents of the split size.
<br>
                'abs': to set the slicing unit as absolute numbers.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ReadInstruction:from_spec' href='parser/test3/arrow_reader.py#L540'>ReadInstruction:from_spec</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>spec,<br></ul>
        <li>Docs:<br>        """Creates a ReadInstruction instance out of a string spec.
<br>

<br>
        Args:
<br>
            spec (str): split(s) + optional slice(s) to read + optional rounding
<br>
                        if percents are used as the slicing unit. A slice can be specified,
<br>
                        using absolute numbers (int) or percentages (int). E.g.
<br>
                            `test`: test split.
<br>
                            `test + validation`: test split + validation split.
<br>
                            `test[10:]`: test split, minus its first 10 records.
<br>
                            `test[:10%]`: first 10% records of test split.
<br>
                            `test[:20%](pct1_dropremainder)`: first 10% records, rounded with
<br>
                                                              the `pct1_dropremainder` rounding.
<br>
                            `test[:-5%]+train[40%:60%]`: first 95% of test + middle 20% of
<br>
                                                         train.
<br>

<br>
        Returns:
<br>
            ReadInstruction instance.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ReadInstruction:to_spec' href='parser/test3/arrow_reader.py#L566'>ReadInstruction:to_spec</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ReadInstruction:__add__' href='parser/test3/arrow_reader.py#L586'>ReadInstruction:__add__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br>        """Returns a new ReadInstruction obj, result of appending other to self."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ReadInstruction:__str__' href='parser/test3/arrow_reader.py#L601'>ReadInstruction:__str__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ReadInstruction:__repr__' href='parser/test3/arrow_reader.py#L604'>ReadInstruction:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/arrow_reader.py:ReadInstruction:to_absolute' href='parser/test3/arrow_reader.py#L607'>ReadInstruction:to_absolute</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>name2len,<br></ul>
        <li>Docs:<br>        """Translate instruction into a list of absolute instructions.
<br>

<br>
        Those absolute instructions are then to be added together.
<br>

<br>
        Args:
<br>
            name2len: dict associating split names to number of examples.
<br>

<br>
        Returns:
<br>
            list of _AbsoluteInstruction instances (corresponds to the + in spec).
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/metric.py' href='parser/test3/metric.py'>parser/test3/metric.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/metric.py:FileFreeLock' href='parser/test3/metric.py#L43'>FileFreeLock</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/metric.py:MetricInfoMixin' href='parser/test3/metric.py#L65'>MetricInfoMixin</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/metric.py:Metric' href='parser/test3/metric.py#L127'>Metric</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:FileFreeLock:__init__' href='parser/test3/metric.py#L46'>FileFreeLock:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>lock_file,<br>*args,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:FileFreeLock:_acquire' href='parser/test3/metric.py#L50'>FileFreeLock:_acquire</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:FileFreeLock:_release' href='parser/test3/metric.py#L61'>FileFreeLock:_release</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:__init__' href='parser/test3/metric.py#L70'>MetricInfoMixin:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>info:  MetricInfo,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:info' href='parser/test3/metric.py#L74'>MetricInfoMixin:info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """:class:`datasets.MetricInfo` object containing all the metadata in the metric."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:name' href='parser/test3/metric.py#L79'>MetricInfoMixin:name</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:experiment_id' href='parser/test3/metric.py#L83'>MetricInfoMixin:experiment_id</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:description' href='parser/test3/metric.py#L87'>MetricInfoMixin:description</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:citation' href='parser/test3/metric.py#L91'>MetricInfoMixin:citation</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:features' href='parser/test3/metric.py#L95'>MetricInfoMixin:features</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:inputs_description' href='parser/test3/metric.py#L99'>MetricInfoMixin:inputs_description</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:homepage' href='parser/test3/metric.py#L103'>MetricInfoMixin:homepage</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:license' href='parser/test3/metric.py#L107'>MetricInfoMixin:license</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:codebase_urls' href='parser/test3/metric.py#L111'>MetricInfoMixin:codebase_urls</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:reference_urls' href='parser/test3/metric.py#L115'>MetricInfoMixin:reference_urls</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:streamable' href='parser/test3/metric.py#L119'>MetricInfoMixin:streamable</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:MetricInfoMixin:format' href='parser/test3/metric.py#L123'>MetricInfoMixin:format</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:__init__' href='parser/test3/metric.py#L147'>Metric:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>config_name:  Optional[str]  =  None,<br>keep_in_memory:  bool  =  False,<br>cache_dir:  Optional[str]  =  None,<br>num_process:  int  =  1,<br>process_id:  int  =  0,<br>seed:  Optional[int]  =  None,<br>experiment_id:  Optional[str]  =  None,<br>max_concurrent_cache_files:  int  =  10000,<br>timeout:  Union[int,<br>float]  =  100,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:__len__' href='parser/test3/metric.py#L211'>Metric:__len__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Return the number of examples (predictions or predictions/references pair)
<br>
        currently stored in the metric's cache.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:__repr__' href='parser/test3/metric.py#L217'>Metric:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_build_data_dir' href='parser/test3/metric.py#L224'>Metric:_build_data_dir</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Path of this metric in cache_dir:
<br>
        Will be:
<br>
            self._data_dir_root/self.name/self.config_name/self.hash (if not none)/
<br>
        If any of these element is missing or if ``with_version=False`` the corresponding subfolders are dropped.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_create_cache_file' href='parser/test3/metric.py#L235'>Metric:_create_cache_file</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>timeout = 1,<br></ul>
        <li>Docs:<br>        """Create a new cache file. If the default cache file is used, we generated a new hash."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_get_all_cache_files' href='parser/test3/metric.py#L268'>Metric:_get_all_cache_files</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Get a lock on all the cache files in a distributed setup.
<br>
        We wait for timeout second to let all the distributed node finish their tasks (default is 100 seconds).
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_check_all_processes_locks' href='parser/test3/metric.py#L301'>Metric:_check_all_processes_locks</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_check_rendez_vous' href='parser/test3/metric.py#L317'>Metric:_check_rendez_vous</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_finalize' href='parser/test3/metric.py#L337'>Metric:_finalize</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Close all the writing process and load/gather the data
<br>
        from all the nodes if main node or all_process is True.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:compute' href='parser/test3/metric.py#L371'>Metric:compute</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*,<br>predictions = None,<br>references = None,<br>**kwargs,<br></ul>
        <li>Docs:<br>        """Compute the metrics.
<br>

<br>
        Usage of positional arguments is not allowed to prevent mistakes.
<br>

<br>
        Args:
<br>
            predictions (list/array/tensor, optional): Predictions.
<br>
            references (list/array/tensor, optional): References.
<br>
            **kwargs (optional): Keyword arguments that will be forwarded to the metrics :meth:`_compute`
<br>
                method (see details in the docstring).
<br>

<br>
        Return:
<br>
            dict or None
<br>

<br>
            - Dictionary with the metrics if this metric is run on the main process (``process_id == 0``).
<br>
            - None if the metric is not run on the main process (``process_id != 0``).
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:add_batch' href='parser/test3/metric.py#L423'>Metric:add_batch</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*,<br>predictions = None,<br>references = None,<br></ul>
        <li>Docs:<br>        """Add a batch of predictions and references for the metric's stack.
<br>

<br>
        Args:
<br>
            predictions (list/array/tensor, optional): Predictions.
<br>
            references (list/array/tensor, optional): References.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:add' href='parser/test3/metric.py#L444'>Metric:add</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*,<br>predictions = None,<br>references = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_init_writer' href='parser/test3/metric.py#L465'>Metric:_init_writer</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>timeout = 1,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_info' href='parser/test3/metric.py#L504'>Metric:_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Construct the MetricInfo object. See `MetricInfo` for details.
<br>

<br>
        Warning: This function is only called once and the result is cached for all
<br>
        following .info() calls.
<br>

<br>
        Returns:
<br>
            info: (MetricInfo) The metrics information
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:download_and_prepare' href='parser/test3/metric.py#L515'>Metric:download_and_prepare</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>download_config:  Optional[DownloadConfig]  =  None,<br>dl_manager:  Optional[DownloadManager]  =  None,<br>,<br></ul>
        <li>Docs:<br>        """Downloads and prepares dataset for reading.
<br>

<br>
        Args:
<br>
            download_config (:class:`DownloadConfig`, optional): Specific download configuration parameters.
<br>
            dl_manager (:class:`DownloadManager`, optional): Specific download manager to use.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_download_and_prepare' href='parser/test3/metric.py#L538'>Metric:_download_and_prepare</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager,<br></ul>
        <li>Docs:<br>        """Downloads and prepares resources for the metric.
<br>

<br>
        This is the internal implementation to overwrite called when user calls
<br>
        `download_and_prepare`. It should download all required resources for the metric.
<br>

<br>
        Args:
<br>
            dl_manager (:class:`DownloadManager`): `DownloadManager` used to download and cache data.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:_compute' href='parser/test3/metric.py#L549'>Metric:_compute</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*,<br>predictions = None,<br>references = None,<br>**kwargs,<br></ul>
        <li>Docs:<br>        """This method defines the common API for all the metrics in the library"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/metric.py:Metric:__del__' href='parser/test3/metric.py#L553'>Metric:__del__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/filesystems/compression/gzip.py' href='parser/test3/filesystems/compression/gzip.py'>parser/test3/filesystems/compression/gzip.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/filesystems/compression/gzip.py:GZipFileSystem' href='parser/test3/filesystems/compression/gzip.py#L9'>GZipFileSystem</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/filesystems/compression/gzip.py:GZipFileSystem:__init__' href='parser/test3/filesystems/compression/gzip.py#L15'>GZipFileSystem:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>fo:  str  =  "",<br>mode:  str  =  "rb",<br>target_protocol:  Optional[str]  =  None,<br>target_options:  Optional[dict]  =  None,<br>block_size:  int  =  DEFAULT_BLOCK_SIZE,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br>        """
<br>
        The GZipFileSystem can be instantiated from any gzip file.
<br>
        It read the contents of GZip archive as a file-system with one file inside.
<br>
        The single file inside the filesystem is named after the Gzip file, without ".gz" at the end.
<br>

<br>
        Args:
<br>
            fo (:obj:``str``): Path to file containing GZIP. Will fetch file using ``fsspec.open()``
<br>
            mode (:obj:``str``): Currently, only 'rb' accepted
<br>
            target_protocol(:obj:``str``, optional): To override the FS protocol inferred from a URL.
<br>
            target_options (:obj:``dict``, optional): Kwargs passed when instantiating the target FS.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/filesystems/compression/gzip.py:GZipFileSystem:_strip_protocol' href='parser/test3/filesystems/compression/gzip.py#L46'>GZipFileSystem:_strip_protocol</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>path,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/filesystems/compression/gzip.py:GZipFileSystem:_get_dirs' href='parser/test3/filesystems/compression/gzip.py#L50'>GZipFileSystem:_get_dirs</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/filesystems/compression/gzip.py:GZipFileSystem:cat' href='parser/test3/filesystems/compression/gzip.py#L55'>GZipFileSystem:cat</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path:  str,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/filesystems/compression/gzip.py:GZipFileSystem:_open' href='parser/test3/filesystems/compression/gzip.py#L58'>GZipFileSystem:_open</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>path:  str,<br>mode:  str  =  "rb",<br>block_size:  Optional[int]  =  None,<br>autocommit:  bool  =  True,<br>cache_options:  Optional[dict]  =  None,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/packaged_modules/pandas/pandas.py' href='parser/test3/packaged_modules/pandas/pandas.py'>parser/test3/packaged_modules/pandas/pandas.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/packaged_modules/pandas/pandas.py:Pandas' href='parser/test3/packaged_modules/pandas/pandas.py#L9'>Pandas</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/pandas/pandas.py:Pandas:_info' href='parser/test3/packaged_modules/pandas/pandas.py#L10'>Pandas:_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/pandas/pandas.py:Pandas:_split_generators' href='parser/test3/packaged_modules/pandas/pandas.py#L13'>Pandas:_split_generators</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dl_manager,<br></ul>
        <li>Docs:<br>        """We handle string, list and dicts in datafiles"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/packaged_modules/pandas/pandas.py:Pandas:_generate_tables' href='parser/test3/packaged_modules/pandas/pandas.py#L30'>Pandas:_generate_tables</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>files,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/commands/run_beam.py' href='parser/test3/commands/run_beam.py'>parser/test3/commands/run_beam.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/commands/run_beam.py:run_beam_command_factory' href='parser/test3/commands/run_beam.py#L14'>run_beam_command_factory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>args,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/commands/run_beam.py:RunBeamCommand' href='parser/test3/commands/run_beam.py#L28'>RunBeamCommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/run_beam.py:RunBeamCommand:register_subcommand' href='parser/test3/commands/run_beam.py#L30'>RunBeamCommand:register_subcommand</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>parser:  ArgumentParser,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/run_beam.py:RunBeamCommand:__init__' href='parser/test3/commands/run_beam.py#L60'>RunBeamCommand:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>dataset:  str,<br>name:  str,<br>cache_dir:  str,<br>beam_pipeline_options:  str,<br>data_dir:  str,<br>all_configs:  bool,<br>save_infos:  bool,<br>ignore_verifications:  bool,<br>force_redownload:  bool,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/commands/run_beam.py:RunBeamCommand:run' href='parser/test3/commands/run_beam.py#L82'>RunBeamCommand:run</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/tasks/text_classification.py' href='parser/test3/tasks/text_classification.py'>parser/test3/tasks/text_classification.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/tasks/text_classification.py:TextClassification' href='parser/test3/tasks/text_classification.py#L9'>TextClassification</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/tasks/text_classification.py:TextClassification:__post_init__' href='parser/test3/tasks/text_classification.py#L19'>TextClassification:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/tasks/text_classification.py:TextClassification:column_mapping' href='parser/test3/tasks/text_classification.py#L28'>TextClassification:column_mapping</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test/test2.py' href='parser/test/test2.py'>parser/test/test2.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:prepare_target_and_clean_up_test' href='parser/test/test2.py#L44'>prepare_target_and_clean_up_test</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """Set up target init and clean up test config."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:clean_up_config_test' href='parser/test/test2.py#L64'>clean_up_config_test</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """Clean up configuration after testing."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:check_default_network_config' href='parser/test/test2.py#L74'>check_default_network_config</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br></ul>
        <li>Docs:<br>    """Check and set default network config."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:check_module_env' href='parser/test/test2.py#L115'>check_module_env</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """Verify information about module status and network status."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:provision_certificates_to_target' href='parser/test/test2.py#L142'>provision_certificates_to_target</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>auth,<br>nist,<br>root_ca_path,<br>client_cert_path,<br>client_key_path,<br></ul>
        <li>Docs:<br>    """Provide certificates to target."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:config_session_connection' href='parser/test/test2.py#L159'>config_session_connection</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br>sid = 1,<br></ul>
        <li>Docs:<br>    """Session configuration."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:config_cipher_suite_and_tcps_action' href='parser/test/test2.py#L163'>config_cipher_suite_and_tcps_action</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>auth,<br>nist_value,<br>profile_id = 0,<br>config_cipher = 1,<br>valid = 1,<br></ul>
        <li>Docs:<br>    """Verify TCPS operations by using specified cipher suite."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0001' href='parser/test/test2.py#L179'>L_RTOS_KTCPTLS_0001</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Server authentication.
<br>
    No certificates loaded. Should not connect to server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0002' href='parser/test/test2.py#L202'>L_RTOS_KTCPTLS_0002</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Server authentication.
<br>
    Server Root CA loaded. Connects to server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0003' href='parser/test/test2.py#L223'>L_RTOS_KTCPTLS_0003</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Server authentication.
<br>
    Server Root CA, Client key, Client root CA loaded. Connects to
<br>
    server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0004' href='parser/test/test2.py#L244'>L_RTOS_KTCPTLS_0004</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    No certificates loaded. Should not connect to server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0005' href='parser/test/test2.py#L264'>L_RTOS_KTCPTLS_0005</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA loaded. Should not connect to server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0006' href='parser/test/test2.py#L284'>L_RTOS_KTCPTLS_0006</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA loaded. Client root CA loaded. Should not connect to
<br>
    server.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0014' href='parser/test/test2.py#L305'>L_RTOS_KTCPTLS_0014</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256
<br>
    (AT+KSSLCRYPTO=0,8,1,8192,4,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0016' href='parser/test/test2.py#L327'>L_RTOS_KTCPTLS_0016</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-128-GCM-
<br>
    SHA256 (AT+KSSLCRYPTO=0,8,2,8192,4,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0017' href='parser/test/test2.py#L349'>L_RTOS_KTCPTLS_0017</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-256-GCM-
<br>
    SHA384 (AT+KSSLCRYPTO=0,8,2,16384,8,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0018' href='parser/test/test2.py#L371'>L_RTOS_KTCPTLS_0018</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-128-CCM
<br>
    (AT+KSSLCRYPTO=0,8,2,16,0,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0019' href='parser/test/test2.py#L393'>L_RTOS_KTCPTLS_0019</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-256-CCM
<br>
    (AT+KSSLCRYPTO=0,8,2,32,0,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0020' href='parser/test/test2.py#L415'>L_RTOS_KTCPTLS_0020</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-128-CCM-8
<br>
    (AT+KSSLCRYPTO=0,8,2,256,0,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0021' href='parser/test/test2.py#L437'>L_RTOS_KTCPTLS_0021</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Mutual authentication.
<br>
    Server Root CA, Client root CA, Client key loaded. Connects to
<br>
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-256-CCM-8
<br>
    (AT+KSSLCRYPTO=0,8,2,512,0,4,3).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:L_RTOS_KTCPTLS_0022' href='parser/test/test2.py#L459'>L_RTOS_KTCPTLS_0022</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>target,<br>prep_target,<br></ul>
        <li>Docs:<br>    """TCP over TLS: Module as Server.
<br>
    Server certicate, Server key loaded.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:_new_function' href='parser/test/test2.py#L514'>_new_function</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>asd: str = None,<br>zxc = "asdad",<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:_new_2' href='parser/test/test2.py#L518'>_new_2</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:test_function_multiL_lines' href='parser/test/test2.py#L523'>test_function_multiL_lines</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>test: float,<br>multi:  str = "asd",<br>line:  int = 12,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test/test2.py:test_special_chars' href='parser/test/test2.py#L529'>test_special_chars</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>test:  str =  "Hello, World!",<br>interger:  int  =  0,<br>true  =  True,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/fingerprint.py' href='parser/test3/fingerprint.py'>parser/test3/fingerprint.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:maybe_register_dataset_for_temp_dir_deletion' href='parser/test3/fingerprint.py#L72'>maybe_register_dataset_for_temp_dir_deletion</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset,<br></ul>
        <li>Docs:<br>    """
<br>
    This function registers the datasets that have cache files in _TEMP_DIR_FOR_TEMP_CACHE_FILES in order
<br>
    to properly delete them before deleting the temporary directory.
<br>
    The temporary directory _TEMP_DIR_FOR_TEMP_CACHE_FILES is used when caching is disabled.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:get_datasets_with_cache_file_in_temp_dir' href='parser/test3/fingerprint.py#L91'>get_datasets_with_cache_file_in_temp_dir</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:set_caching_enabled' href='parser/test3/fingerprint.py#L95'>set_caching_enabled</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>boolean:  bool,<br></ul>
        <li>Docs:<br>    """
<br>
    When applying transforms on a dataset, the data are stored in cache files.
<br>
    The caching mechanism allows to reload an existing cache file if it's already been computed.
<br>

<br>
    Reloading a dataset is possible since the cache files are named using the dataset fingerprint, which is updated
<br>
    after each transform.
<br>

<br>
    If disabled, the library will no longer reload cached datasets files when applying transforms to the datasets.
<br>
    More precisely, if the caching is disabled:
<br>
    - cache files are always recreated
<br>
    - cache files are written to a temporary directory that is deleted when session closes
<br>
    - cache files are named using a random hash instead of the dataset fingerprint
<br>
    - use :func:`datasets.Dataset.save_to_disk` to save a transformed dataset or it will be deleted when session closes
<br>
    - caching doesn't affect :func:`datasets.load_dataset`. If you want to regenerate a dataset from scratch you should use
<br>
    the ``download_mode`` parameter in :func:`datasets.load_dataset`.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:is_caching_enabled' href='parser/test3/fingerprint.py#L116'>is_caching_enabled</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """
<br>
    When applying transforms on a dataset, the data are stored in cache files.
<br>
    The caching mechanism allows to reload an existing cache file if it's already been computed.
<br>

<br>
    Reloading a dataset is possible since the cache files are named using the dataset fingerprint, which is updated
<br>
    after each transform.
<br>

<br>
    If disabled, the library will no longer reload cached datasets files when applying transforms to the datasets.
<br>
    More precisely, if the caching is disabled:
<br>
    - cache files are always recreated
<br>
    - cache files are written to a temporary directory that is deleted when session closes
<br>
    - cache files are named using a random hash instead of the dataset fingerprint
<br>
    - use :func:`datasets.Dataset.save_to_disk` to save a transformed dataset or it will be deleted when session closes
<br>
    - caching doesn't affect :func:`datasets.load_dataset`. If you want to regenerate a dataset from scratch you should use
<br>
    the ``download_mode`` parameter in :func:`datasets.load_dataset`.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:get_temporary_cache_files_directory' href='parser/test3/fingerprint.py#L137'>get_temporary_cache_files_directory</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br>    """Return a directory that is deleted when session closes."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:hashregister' href='parser/test3/fingerprint.py#L157'>hashregister</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>*types,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:_hash_pa_table' href='parser/test3/fingerprint.py#L209'>_hash_pa_table</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>hasher,<br>value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:_hash_dataset_info' href='parser/test3/fingerprint.py#L221'>_hash_dataset_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>hasher,<br>value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:generate_fingerprint' href='parser/test3/fingerprint.py#L233'>generate_fingerprint</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:generate_random_fingerprint' href='parser/test3/fingerprint.py#L247'>generate_random_fingerprint</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>nbits = 64,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:update_fingerprint' href='parser/test3/fingerprint.py#L251'>update_fingerprint</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>fingerprint,<br>transform,<br>transform_args,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/fingerprint.py:fingerprint_transform' href='parser/test3/fingerprint.py#L301'>fingerprint_transform</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>inplace:  bool,<br>use_kwargs:  Optional[List[str]]  =  None,<br>ignore_kwargs:  Optional[List[str]]  =  None,<br>fingerprint_names:  Optional[List[str]]  =  None,<br>randomized_function:  bool  =  False,<br>,<br></ul>
        <li>Docs:<br>    """
<br>
    Wrapper for dataset transforms to update the dataset fingerprint using ``update_fingerprint``
<br>

<br>
    Args:
<br>
        inplace (``bool``):  If inplace is True, the fingerprint of the dataset is updated inplace.
<br>
            Otherwise, a parameter "new_fingerprint" is passed to the wrapped method that should take care of
<br>
            setting the fingerprint of the returned Dataset.
<br>
        use_kwargs (Optional ``List[str]``): optional white list of argument names to take into account
<br>
            to update the fingerprint to the wrapped method that should take care of
<br>
            setting the fingerprint of the returned Dataset. By default all the arguments are used.
<br>
        ignore_kwargs (Optional ``List[str]``): optional black list of argument names to take into account
<br>
            to update the fingerprint. Note that ignore_kwargs prevails on use_kwargs.
<br>
        fingerprint_names (Optional ``List[str]``, defaults to ["new_fingerprint"]):
<br>
            If the dataset transforms is not inplace and returns a DatasetDict, then it can require
<br>
            several fingerprints (one per dataset in the DatasetDict). By specifying fingerprint_names,
<br>
            one fingerprint named after each element of fingerprint_names is going to be passed.
<br>
        randomized_function (``bool``, defaults to False): If the dataset transform is random and has
<br>
            optional parameters "seed" and "generator", then you can set randomized_function to True.
<br>
            This way, even if users set "seed" and "generator" to None, then the fingerprint is
<br>
            going to be randomly generated depending on numpy's current state. In this case, the
<br>
            generator is set to np.random.default_rng(np.random.get_state()[1][0]).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/fingerprint.py:_TempDirWithCustomCleanup' href='parser/test3/fingerprint.py#L48'>_TempDirWithCustomCleanup</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/fingerprint.py:Hasher' href='parser/test3/fingerprint.py#L166'>Hasher</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/fingerprint.py:_TempDirWithCustomCleanup:__init__' href='parser/test3/fingerprint.py#L55'>_TempDirWithCustomCleanup:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>cleanup_func = None,<br>*cleanup_func_args,<br>**cleanup_func_kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/fingerprint.py:_TempDirWithCustomCleanup:_cleanup' href='parser/test3/fingerprint.py#L62'>_TempDirWithCustomCleanup:_cleanup</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/fingerprint.py:_TempDirWithCustomCleanup:cleanup' href='parser/test3/fingerprint.py#L67'>_TempDirWithCustomCleanup:cleanup</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/fingerprint.py:Hasher:__init__' href='parser/test3/fingerprint.py#L171'>Hasher:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/fingerprint.py:Hasher:hash_bytes' href='parser/test3/fingerprint.py#L175'>Hasher:hash_bytes</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>value:  Union[bytes,<br>List[bytes]],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/fingerprint.py:Hasher:hash_default' href='parser/test3/fingerprint.py#L183'>Hasher:hash_default</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>value:  Any,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/fingerprint.py:Hasher:hash' href='parser/test3/fingerprint.py#L187'>Hasher:hash</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>value:  Union[bytes,<br>List[bytes]],<br></ul>
        <li>Docs:<br>    """
<br>
    Wrapper for dataset transforms to update the dataset fingerprint using ``update_fingerprint``
<br>

<br>
    Args:
<br>
        inplace (``bool``):  If inplace is True, the fingerprint of the dataset is updated inplace.
<br>
            Otherwise, a parameter "new_fingerprint" is passed to the wrapped method that should take care of
<br>
            setting the fingerprint of the returned Dataset.
<br>
        use_kwargs (Optional ``List[str]``): optional white list of argument names to take into account
<br>
            to update the fingerprint to the wrapped method that should take care of
<br>
            setting the fingerprint of the returned Dataset. By default all the arguments are used.
<br>
        ignore_kwargs (Optional ``List[str]``): optional black list of argument names to take into account
<br>
            to update the fingerprint. Note that ignore_kwargs prevails on use_kwargs.
<br>
        fingerprint_names (Optional ``List[str]``, defaults to ["new_fingerprint"]):
<br>
            If the dataset transforms is not inplace and returns a DatasetDict, then it can require
<br>
            several fingerprints (one per dataset in the DatasetDict). By specifying fingerprint_names,
<br>
            one fingerprint named after each element of fingerprint_names is going to be passed.
<br>
        randomized_function (``bool``, defaults to False): If the dataset transform is random and has
<br>
            optional parameters "seed" and "generator", then you can set randomized_function to True.
<br>
            This way, even if users set "seed" and "generator" to None, then the fingerprint is
<br>
            going to be randomly generated depending on numpy's current state. In this case, the
<br>
            generator is set to np.random.default_rng(np.random.get_state()[1][0]).
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/fingerprint.py:Hasher:update' href='parser/test3/fingerprint.py#L193'>Hasher:update</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>value:  Any,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/fingerprint.py:Hasher:hexdigest' href='parser/test3/fingerprint.py#L199'>Hasher:hexdigest</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/filesystems/__init__.py' href='parser/test3/filesystems/__init__.py'>parser/test3/filesystems/__init__.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/filesystems/__init__.py:extract_path_from_uri' href='parser/test3/filesystems/__init__.py#L18'>extract_path_from_uri</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset_path:  str,<br></ul>
        <li>Docs:<br>    """
<br>
    preprocesses `dataset_path` and removes remote filesystem (e.g. removing ``s3://``)
<br>

<br>
    Args:
<br>
        dataset_path (``str``): path (e.g. ``dataset/train``) or remote uri (e.g. ``s3://my-bucket/dataset/train``) of the dataset directory
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/filesystems/__init__.py:is_remote_filesystem' href='parser/test3/filesystems/__init__.py#L30'>is_remote_filesystem</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>fs:  fsspec.spec.AbstractFileSystem,<br></ul>
        <li>Docs:<br>    """
<br>
    Validates if filesystem has remote protocol.
<br>

<br>
    Args:
<br>
        fs (``fsspec.spec.AbstractFileSystem``): An abstract super-class for pythonic file-systems, e.g. :code:`fsspec.filesystem(\'file\')` or :class:`datasets.filesystems.S3FileSystem`
<br>
    """
<br>
</li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/packaged_modules/__init__.py' href='parser/test3/packaged_modules/__init__.py'>parser/test3/packaged_modules/__init__.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/packaged_modules/__init__.py:hash_python_lines' href='parser/test3/packaged_modules/__init__.py#L13'>hash_python_lines</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>lines:  List[str],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/splits.py' href='parser/test3/splits.py'>parser/test3/splits.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:SplitInfo' href='parser/test3/splits.py#L32'>SplitInfo</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:SubSplitInfo' href='parser/test3/splits.py#L51'>SubSplitInfo</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:SplitBase' href='parser/test3/splits.py#L73'>SplitBase</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:PercentSliceMeta' href='parser/test3/splits.py#L244'>PercentSliceMeta</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:PercentSlice' href='parser/test3/splits.py#L251'>PercentSlice</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:_SplitMerged' href='parser/test3/splits.py#L266'>_SplitMerged</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:_SubSplit' href='parser/test3/splits.py#L282'>_SubSplit</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:NamedSplit' href='parser/test3/splits.py#L304'>NamedSplit</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:NamedSplitAll' href='parser/test3/splits.py#L373'>NamedSplitAll</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:Split' href='parser/test3/splits.py#L388'>Split</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:SplitReadInstruction' href='parser/test3/splits.py#L428'>SplitReadInstruction</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:SplitDict' href='parser/test3/splits.py#L483'>SplitDict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/splits.py:SplitGenerator' href='parser/test3/splits.py#L550'>SplitGenerator</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitInfo:file_instructions' href='parser/test3/splits.py#L39'>SplitInfo:file_instructions</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Returns the list of dict(filename, take, skip)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SubSplitInfo:num_examples' href='parser/test3/splits.py#L63'>SubSplitInfo:num_examples</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Returns the number of example in the subsplit."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SubSplitInfo:file_instructions' href='parser/test3/splits.py#L39'>SubSplitInfo:file_instructions</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Returns the list of dict(filename, take, skip)."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitBase:get_read_instruction' href='parser/test3/splits.py#L108'>SplitBase:get_read_instruction</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_dict,<br></ul>
        <li>Docs:<br>        """Parse the descriptor tree and compile all read instructions together.
<br>

<br>
        Args:
<br>
            split_dict: `dict`, The `dict[split_name, SplitInfo]` of the dataset
<br>

<br>
        Returns:
<br>
            split_read_instruction: `SplitReadInstruction`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitBase:__eq__' href='parser/test3/splits.py#L119'>SplitBase:__eq__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br>        """Equality: datasets.Split.TRAIN == 'train'."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitBase:__ne__' href='parser/test3/splits.py#L125'>SplitBase:__ne__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br>        """InEquality: datasets.Split.TRAIN != 'test'."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitBase:__add__' href='parser/test3/splits.py#L129'>SplitBase:__add__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br>        """Merging: datasets.Split.TRAIN + datasets.Split.TEST."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitBase:subsplit' href='parser/test3/splits.py#L133'>SplitBase:subsplit</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>arg = None,<br>k = None,<br>percent = None,<br>weighted=None):  = None):  # pylint: disable=redefined-outer-namebool(x) for x in (arg,<br>k,<br>percent,<br>weighted)) != 1:  =  1:,<br></ul>
        <li>Docs:<br>        """Divides this split into subsplits.
<br>

<br>
        There are 3 ways to define subsplits, which correspond to the 3
<br>
        arguments `k` (get `k` even subsplits), `percent` (get a slice of the
<br>
        dataset with `datasets.percent`), and `weighted` (get subsplits with proportions
<br>
        specified by `weighted`).
<br>

<br>
        Examples:
<br>

<br>
        ```
<br>
        # 50% train, 50% test
<br>
        train, test = split.subsplit(k=2)
<br>
        # 50% train, 25% test, 25% validation
<br>
        train, test, validation = split.subsplit(weighted=[2, 1, 1])
<br>
        # Extract last 20%
<br>
        subsplit = split.subsplit(datasets.percent[-20:])
<br>
        ```
<br>

<br>
        Warning: k and weighted will be converted into percent which mean that
<br>
        values below the percent will be rounded up or down. The final split may be
<br>
        bigger to deal with remainders. For instance:
<br>

<br>
        ```
<br>
        train, test, valid = split.subsplit(k=3)  # 33%, 33%, 34%
<br>
        s1, s2, s3, s4 = split.subsplit(weighted=[2, 2, 1, 1])  # 33%, 33%, 16%, 18%
<br>
        ```
<br>

<br>
        Args:
<br>
            arg: If no kwargs are given, `arg` will be interpreted as one of
<br>
                `k`, `percent`, or `weighted` depending on the type.
<br>
                For example:
<br>
                ```
<br>
                split.subsplit(10)  # Equivalent to split.subsplit(k=10)
<br>
                split.subsplit(datasets.percent[:-20])  # percent=datasets.percent[:-20]
<br>
                split.subsplit([1, 1, 2])  # weighted=[1, 1, 2]
<br>
                ```
<br>
            k: `int` If set, subdivide the split into `k` equal parts.
<br>
            percent: `datasets.percent slice`, return a single subsplit corresponding to
<br>
                a slice of the original split. For example:
<br>
                `split.subsplit(datasets.percent[-20:])  # Last 20% of the dataset`.
<br>
            weighted: `list[int]`, return a list of subsplits whose proportions match
<br>
                the normalized sum of the list. For example:
<br>
                `split.subsplit(weighted=[1, 1, 2])  # 25%, 25%, 50%`.
<br>

<br>
        Returns:
<br>
            A subsplit or list of subsplits extracted from this split object.
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:PercentSliceMeta:__getitem__' href='parser/test3/splits.py#L245'>PercentSliceMeta:__getitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>slice_value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:_SplitMerged:__init__' href='parser/test3/splits.py#L269'>_SplitMerged:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split1,<br>split2,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:_SplitMerged:get_read_instruction' href='parser/test3/splits.py#L108'>_SplitMerged:get_read_instruction</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_dict,<br></ul>
        <li>Docs:<br>        """Parse the descriptor tree and compile all read instructions together.
<br>

<br>
        Args:
<br>
            split_dict: `dict`, The `dict[split_name, SplitInfo]` of the dataset
<br>

<br>
        Returns:
<br>
            split_read_instruction: `SplitReadInstruction`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:_SplitMerged:__repr__' href='parser/test3/splits.py#L278'>_SplitMerged:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:_SubSplit:__init__' href='parser/test3/splits.py#L285'>_SubSplit:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split,<br>slice_value,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:_SubSplit:get_read_instruction' href='parser/test3/splits.py#L108'>_SubSplit:get_read_instruction</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_dict,<br></ul>
        <li>Docs:<br>        """Parse the descriptor tree and compile all read instructions together.
<br>

<br>
        Args:
<br>
            split_dict: `dict`, The `dict[split_name, SplitInfo]` of the dataset
<br>

<br>
        Returns:
<br>
            split_read_instruction: `SplitReadInstruction`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:_SubSplit:__repr__' href='parser/test3/splits.py#L278'>_SubSplit:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """Represent a sub split of a split descriptor."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:NamedSplitAll:__init__' href='parser/test3/splits.py#L376'>NamedSplitAll:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:NamedSplitAll:__repr__' href='parser/test3/splits.py#L278'>NamedSplitAll:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>    """Represent a sub split of a split descriptor."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:NamedSplitAll:get_read_instruction' href='parser/test3/splits.py#L108'>NamedSplitAll:get_read_instruction</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_dict,<br></ul>
        <li>Docs:<br>        """Parse the descriptor tree and compile all read instructions together.
<br>

<br>
        Args:
<br>
            split_dict: `dict`, The `dict[split_name, SplitInfo]` of the dataset
<br>

<br>
        Returns:
<br>
            split_read_instruction: `SplitReadInstruction`
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:Split:__new__' href='parser/test3/splits.py#L413'>Split:__new__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>name,<br></ul>
        <li>Docs:<br>        """Create a custom split with datasets.Split('custom_name')."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitReadInstruction:__init__' href='parser/test3/splits.py#L444'>SplitReadInstruction:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_info = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitReadInstruction:add' href='parser/test3/splits.py#L450'>SplitReadInstruction:add</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>sliced_split,<br></ul>
        <li>Docs:<br>        """Add a SlicedSplitInfo the read instructions."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitReadInstruction:__add__' href='parser/test3/splits.py#L129'>SplitReadInstruction:__add__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>other,<br></ul>
        <li>Docs:<br>        """Merging: datasets.Split.TRAIN + datasets.Split.TEST."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitReadInstruction:__getitem__' href='parser/test3/splits.py#L467'>SplitReadInstruction:__getitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>slice_value,<br></ul>
        <li>Docs:<br>        """Sub-splits."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitReadInstruction:get_list_sliced_split_info' href='parser/test3/splits.py#L479'>SplitReadInstruction:get_list_sliced_split_info</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitDict:__init__' href='parser/test3/splits.py#L486'>SplitDict:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>*args,<br>dataset_name = None,<br>**kwargs,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitDict:__getitem__' href='parser/test3/splits.py#L490'>SplitDict:__getitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>key:  Union[SplitBase,<br>str],<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitDict:__setitem__' href='parser/test3/splits.py#L503'>SplitDict:__setitem__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>key:  Union[SplitBase,<br>str],<br>value:  SplitInfo,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitDict:add' href='parser/test3/splits.py#L510'>SplitDict:add</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>split_info:  SplitInfo,<br></ul>
        <li>Docs:<br>        """Add the split info."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitDict:total_num_examples' href='parser/test3/splits.py#L518'>SplitDict:total_num_examples</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Return the total number of examples."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitDict:from_split_dict' href='parser/test3/splits.py#L523'>SplitDict:from_split_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>cls,<br>split_infos:  Union[List,<br>Dict],<br>dataset_name:  Optional[str]  =  None,<br></ul>
        <li>Docs:<br>        """Returns a new SplitDict initialized from a Dict or List of `split_infos`."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitDict:to_split_dict' href='parser/test3/splits.py#L540'>SplitDict:to_split_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br>        """Returns a list of SplitInfo protos that we have."""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitDict:copy' href='parser/test3/splits.py#L545'>SplitDict:copy</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/splits.py:SplitGenerator:__post_init__' href='parser/test3/splits.py#L569'>SplitGenerator:__post_init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/utils/info_utils.py' href='parser/test3/utils/info_utils.py'>parser/test3/utils/info_utils.py</a>
</summary>
<ul>
    <details>
        <summary>
        function | <a name='parser/test3/utils/info_utils.py:verify_checksums' href='parser/test3/utils/info_utils.py#L28'>verify_checksums</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>expected_checksums:  Optional[dict],<br>recorded_checksums:  dict,<br>verification_name = None,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/info_utils.py:verify_splits' href='parser/test3/utils/info_utils.py#L60'>verify_splits</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>expected_splits:  Optional[dict],<br>recorded_splits:  dict,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/info_utils.py:get_size_checksum_dict' href='parser/test3/utils/info_utils.py#L78'>get_size_checksum_dict</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>path:  str,<br></ul>
        <li>Docs:<br>    """Compute the file size and the sha256 checksum of a file"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        function | <a name='parser/test3/utils/info_utils.py:is_small_dataset' href='parser/test3/utils/info_utils.py#L87'>is_small_dataset</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>dataset_size,<br></ul>
        <li>Docs:<br>    """Check if `dataset_size` is smaller than `config.IN_MEMORY_MAX_SIZE`.
<br>

<br>
    Args:
<br>
        dataset_size (int): Dataset size in bytes.
<br>

<br>
    Returns:
<br>
        bool: Whether `dataset_size` is smaller than `config.IN_MEMORY_MAX_SIZE`.
<br>
    """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/info_utils.py:ChecksumVerificationException' href='parser/test3/utils/info_utils.py#L12'>ChecksumVerificationException</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/info_utils.py:UnexpectedDownloadedFile' href='parser/test3/utils/info_utils.py#L16'>UnexpectedDownloadedFile</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/info_utils.py:ExpectedMoreDownloadedFiles' href='parser/test3/utils/info_utils.py#L20'>ExpectedMoreDownloadedFiles</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/info_utils.py:NonMatchingChecksumError' href='parser/test3/utils/info_utils.py#L24'>NonMatchingChecksumError</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/info_utils.py:SplitsVerificationException' href='parser/test3/utils/info_utils.py#L44'>SplitsVerificationException</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/info_utils.py:UnexpectedSplits' href='parser/test3/utils/info_utils.py#L48'>UnexpectedSplits</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/info_utils.py:ExpectedMoreSplits' href='parser/test3/utils/info_utils.py#L52'>ExpectedMoreSplits</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/utils/info_utils.py:NonMatchingSplitsSizesError' href='parser/test3/utils/info_utils.py#L56'>NonMatchingSplitsSizesError</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details></ul>
</details>

<details>
<summary>
<a name='parser/test3/hf_api.py' href='parser/test3/hf_api.py'>parser/test3/hf_api.py</a>
</summary>
<ul>
    <details>
        <summary>
        class | <a name='parser/test3/hf_api.py:ObjectInfo' href='parser/test3/hf_api.py#L29'>ObjectInfo</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        class | <a name='parser/test3/hf_api.py:HfApi' href='parser/test3/hf_api.py#L64'>HfApi</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/hf_api.py:ObjectInfo:__init__' href='parser/test3/hf_api.py#L34'>ObjectInfo:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>id:  str,<br>key:  str,<br>lastModified:  Optional[str]  =  None,<br>description:  Optional[str]  =  None,<br>citation:  Optional[str]  =  None,<br>size:  Optional[int]  =  None,<br>etag:  Optional[str]  =  None,<br>siblings:  List[Dict]  =  None,<br>author:  str  =  None,<br>**kwargs,<br>,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/hf_api.py:ObjectInfo:__repr__' href='parser/test3/hf_api.py#L59'>ObjectInfo:__repr__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br></ul>
        <li>Docs:<br></li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/hf_api.py:HfApi:__init__' href='parser/test3/hf_api.py#L67'>HfApi:__init__</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>endpoint = None,<br></ul>
        <li>Docs:<br>        """Create Api using a specific endpoint and also the file types ('datasets' or 'metrics')"""
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/hf_api.py:HfApi:dataset_list' href='parser/test3/hf_api.py#L71'>HfApi:dataset_list</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>with_community_datasets = True,<br>id_only = False,<br></ul>
        <li>Docs:<br>        """
<br>
        Get the public list of all the datasets on huggingface, including the community datasets
<br>
        """
<br>
</li>
        </ul>
    </details>
    <details>
        <summary>
        method | <a name='parser/test3/hf_api.py:HfApi:metric_list' href='parser/test3/hf_api.py#L86'>HfApi:metric_list</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>self,<br>with_community_metrics = True,<br>id_only = False,<br></ul>
        <li>Docs:<br>        """
<br>
        Get the public list of all the metrics on huggingface, including the community metrics
<br>
        """
<br>
</li>
        </ul>
    </details></ul>
</details>
