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
      title: '楼号',
      key: '楼号',
      sortable: true,
      treeNode: true,

      type: 'number',
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: '楼号必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入楼号'
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
      type: 'input',
      form: {
        editDisabled: false,
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
    }, {
      title: '床号',
      key: '床号',
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
          { required: true, message: '床号' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '床号'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: '学号',
      key: '学号',
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
          { required: true, message: 'Student_ID' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: 'Student_ID'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }
    ].concat(vm.commonEndColumns())
  }
}
