// pages/authorize/index.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
  
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  },
  rejectLogin: function (e){
    wx.navigateBack({
      
    })
  },
  bindGetUserInfo: function (e) {
    if (!e.detail.userInfo){
      return;
    }
    wx.setStorageSync('userInfo', e.detail.userInfo)
    this.login();
  },
  login: function () {
    let that = this;
    let token = wx.getStorageSync('token');
    if (token) {
      wx.request({
        method: "post",
        url: 'http://127.0.0.1:8000/login/',
        data: {
          token: token
        },
        success: function (res) {
          if (res.data.code != 0) {
            wx.removeStorageSync('token')
            that.login();
          } else {
            // 回到原来的地方放
            wx.navigateBack();
          }
        },
        fail:function(res){
          wx.showModal({
            title: 'fail',
            content: '请重试',
            showCancel: false
          })
        }
      })
      return;
    }
    wx.login({
      success: function (res) {
        console.log(res)
        wx.request({
          method: "post",
          url: 'http://localhost:8000/login/',
          header: {  
                     'content-type': 'application/x-www-form-urlencoded'  
                  },  
          data: {
            code: res.code
          },
          success: function (res) {
            console.log(res)
            
            if (res.data.code == 10000) {
              // 去注册
              that.registerUser();
              return;
            }
            else if (res.data.code != 0) {
              // 登录错误
              wx.hideLoading();
              wx.showModal({
                title: '提示',
                content: '无法登录，请重试',
                showCancel: false
              })
              return;
            }
            wx.setStorageSync('token', res.data.token)
            // wx.setStorageSync('uid', res.data.data.uid)
            // 回到原来的页面
            wx.navigateBack();
          },
          fail:function(res){
            console.log(res);
          }
        })
      }
    })
  },
  registerUser: function () {
    var that = this;
    wx.login({
      success: function (res) {
        var code = res.code; // 微信登录接口返回的 code 参数，下面注册接口需要用到
        console.log("code"+code);
        wx.getUserInfo({
          success: function (res) {
            var iv = res.iv;
            var encryptedData = res.encryptedData;
            // 下面开始调用注册接口
            wx.request({
              method: "post",
              url: 'http://localhost:8000/register/',
              data: { code: code, encryptedData: encryptedData, iv: iv }, // 设置请求的 参数
              success: (res) => {
                wx.hideLoading();
                wx.setStorageSync('token', res.data.token)
            // wx.setStorageSync('uid', res.data.data.uid)
            // 回到原来的页面
            wx.navigateBack();
            setTimeout(() => {
              that.login();
            }, 2000);
                
                console.log('tttttttttt');
              }
            })
          }
        })
      }
    })
  }
})