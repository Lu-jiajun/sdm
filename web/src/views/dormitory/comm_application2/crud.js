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
      title: '学号',
      key: '学号',
      sortable: true,
      type: 'number',
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: '学号必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入学号'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },

      {
      title: '申请类型',
      key: '选项',
      sortable: true,
      type: 'number',
      form: {
        disabled: true,
        editDisabled: true,
        itemProps: {
        class: { yxtInput: true }
        }
      }
    },
      {
      title: '审批状态',
      key: '审核状态',
      sortable: true,
      type: 'input',
      form: {
        disabled: false,
        editDisabled: false,
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: '原因',
      key: '原因',
      sortable: true,
      treeNode: true,

      type: 'input',
      form: {
        disabled: false,
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: '原因必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入原因'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: '开始时间',
      key: '开始时间',
      sortable: true,
      treeNode: true,

      type: 'datatime',
      form: {
        disabled:true,
        editDisabled: false,

    }} ,{
      title: '结束时间',
      key: '结束时间',
      sortable: true,
      treeNode: true,

      type: 'datatime',
      form: {
        disabled:true,
        editDisabled: false,

    }
    },{
      title: '床号',
      key: '床号',
      sortable: true,
      treeNode: true,

      type: 'datatime',
      form: {
        disabled:true,
        editDisabled: false,

    }
    },{
      title: '宿舍号',
      key: '宿舍号',
      sortable: true,
      treeNode: true,

      type: 'datatime',
      form: {
        disabled:true,
        editDisabled: false,

    }
    }
    ].concat(vm.commonEndColumns())
  }
}
