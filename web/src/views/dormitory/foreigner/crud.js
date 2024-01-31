import { request } from '@/api/service'
import { BUTTON_STATUS_NUMBER } from '@/config/button'
import { urlPrefix as bookPrefix } from './api'
import * as api from './api'
export const crudOptions = vm => {
  return {
    pageOptions: {
      compact: true
    },
    options: {
      tableType: 'vxe-table',
      rowKey: true, // 必须设置，true or false
      rowId: 'id',
      height: '100%', // 表格高度100%, 使用toolbar必须设置
      highlightCurrentRow: false
    },
    rowHandle: {
      width: 140,
      view: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Retrieve')
        }
      },
      edit: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Update')
        }
      },
      remove: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Delete')
        }
      }
    },
    indexRow: {
      // 或者直接传true,不显示title，不居中
      title: '序号',
      align: 'center',
      width: 100
    },
    viewOptions: {
      componentType: 'form'
    },
    formOptions: {
      defaultSpan: 24, // 默认的表单 span
      width: '35%'
    },
    columns: [{
      title: 'ID',
      key: 'id',
      show: false,
      disabled: true,
      width: 90,
      form: {
        disabled: true
      }
    },
    {
      title: '姓名',
      key: '外来人员姓名',
      sortable: true,
      treeNode: true,

      type: 'input',
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: '姓名必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入姓名'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: '电话',
      key: '电话',
      sortable: true,
      type: 'input',
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: '电话号码必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入电话号码'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: '宿舍号',
      key: '宿舍号',
      sortable: true,

      search: {
        component: {
          props: {
            clearable: true
          }
        }
      },

      type: 'number',
      form: {
        editDisabled: false, // 在修改页面显示
        rules: [
          // 表单校验规则
          { required: true, message: '宿舍号必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入宿舍号'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: '来访时间',
      key: '来访时间',
      sortable: true,
      type: 'datetime',
      form: {
        disabled: false,
        rules: [
          { required: true, message: '来访时间必填' }
        ],
        component: {
          props: {
            clearable: true,
            format: 'yyyy-MM-dd',
            valueFormat: 'yyyy-MM-dd'
          },
          placeholder: '请输入来访时间'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: '值班人员',
      key: '宿管ID',
      sortable: true,
      type: 'number',
      form: {
        editDisabled: false, // 在修改页面显示
        rules: [
          // 表单校验规则
          { required: true, message: '值班人员id必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入值班人员id'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: '目的',
      key: '目的',
      sortable: true,
      treeNode: true,

      type: 'input',
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: '目的必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入目的'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },{
      title: '离开时间',
      key: '离开时间',
      sortable: true,
      type: 'datetime',
      form: {
        disabled: false,
        component: {
          props: {
            clearable: true,
            format: 'yyyy-MM-dd',
            valueFormat: 'yyyy-MM-dd'
          },
          placeholder: '请输入离开时间'
        }
      }
    }
    ].concat(vm.commonEndColumns())
  }
}
