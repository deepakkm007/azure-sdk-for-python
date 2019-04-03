# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .catalog_item import CatalogItem


class USqlTableStatistics(CatalogItem):
    """A Data Lake Analytics catalog U-SQL table statistics item.

    :param compute_account_name: the name of the Data Lake Analytics account.
    :type compute_account_name: str
    :param version: the version of the catalog item.
    :type version: str
    :param database_name: the name of the database.
    :type database_name: str
    :param schema_name: the name of the schema associated with this table and
     database.
    :type schema_name: str
    :param table_name: the name of the table.
    :type table_name: str
    :param name: the name of the table statistics.
    :type name: str
    :param user_stat_name: the name of the user statistics.
    :type user_stat_name: str
    :param stat_data_path: the path to the statistics data.
    :type stat_data_path: str
    :param create_time: the creation time of the statistics.
    :type create_time: datetime
    :param update_time: the last time the statistics were updated.
    :type update_time: datetime
    :param is_user_created: the switch indicating if these statistics are user
     created.
    :type is_user_created: bool
    :param is_auto_created: the switch indicating if these statistics are
     automatically created.
    :type is_auto_created: bool
    :param has_filter: the switch indicating if these statistics have a
     filter.
    :type has_filter: bool
    :param filter_definition: the filter definition for the statistics.
    :type filter_definition: str
    :param col_names: the list of column names associated with these
     statistics.
    :type col_names: list[str]
    """

    _attribute_map = {
        'compute_account_name': {'key': 'computeAccountName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'schema_name': {'key': 'schemaName', 'type': 'str'},
        'table_name': {'key': 'tableName', 'type': 'str'},
        'name': {'key': 'statisticsName', 'type': 'str'},
        'user_stat_name': {'key': 'userStatName', 'type': 'str'},
        'stat_data_path': {'key': 'statDataPath', 'type': 'str'},
        'create_time': {'key': 'createTime', 'type': 'iso-8601'},
        'update_time': {'key': 'updateTime', 'type': 'iso-8601'},
        'is_user_created': {'key': 'isUserCreated', 'type': 'bool'},
        'is_auto_created': {'key': 'isAutoCreated', 'type': 'bool'},
        'has_filter': {'key': 'hasFilter', 'type': 'bool'},
        'filter_definition': {'key': 'filterDefinition', 'type': 'str'},
        'col_names': {'key': 'colNames', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(USqlTableStatistics, self).__init__(**kwargs)
        self.database_name = kwargs.get('database_name', None)
        self.schema_name = kwargs.get('schema_name', None)
        self.table_name = kwargs.get('table_name', None)
        self.name = kwargs.get('name', None)
        self.user_stat_name = kwargs.get('user_stat_name', None)
        self.stat_data_path = kwargs.get('stat_data_path', None)
        self.create_time = kwargs.get('create_time', None)
        self.update_time = kwargs.get('update_time', None)
        self.is_user_created = kwargs.get('is_user_created', None)
        self.is_auto_created = kwargs.get('is_auto_created', None)
        self.has_filter = kwargs.get('has_filter', None)
        self.filter_definition = kwargs.get('filter_definition', None)
        self.col_names = kwargs.get('col_names', None)
