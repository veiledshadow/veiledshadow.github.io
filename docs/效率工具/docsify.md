# 使用 docsify + github 搭建个人博客

docsify 可以快速帮你生成文档网站. 不同于 GitBook, Hexo 的地方是它不会生成静态的 .html 文件，所有转换工作都是在运行的. 如果你想要开始使用它，只需要创建一个 index.html 就可以开始编写文档并直接部署在 GitHub Pages.

[docsify 官网链接](https://docsify.js.org/)

## docsify 在 MacOs 下的安装

- 在终端下安装 `npm` 包管理器.
- 打开终端, 运行命令 `sudo npm i docsify-cli -g` 进行安装.

## docsify 的快速入门

- 进入项目文件夹, 使用 `docsify init blog` 来初始化名为 `blog` 的初使文件夹.
- 使用 `docsify serve blog` 命令打开一个网页查看基本效果.

## 多页文档

### 链接跳转

直接在 `markdown` 文件中加入链接即可, 例如, 想从 HomePage 跳转到 docsify 页面, 只需在 `README.md` 中插入

```
[>> go to docsify](docsify)
```

想要从当前页面跳回到初始界面, 直接加入
```
[<< go home](/)
```

会生成如下超链接

[<< go home](/)

### 侧边栏

当博客数量增多时,使用很多的链接跳转显然是不合理的,这个时候一个好的方式就是在主页添加侧边栏(目录), 通过目录进行跳转.

要现实侧边栏, 主要需要进行如下两步:

- 在项目目录下创建 `_sidebar.md`文件,在里面加入想要现实在侧边栏处的链接,如下所示:

```
<!-- docs/_sidebar.md -->

* [首页](/)

* [指南](/guide)
```

- 在 `index.html` 配置 `loadSidebar` 选项打开侧边栏:

```html
<!-- index.html -->

<script>
  window.$docsify = {
    loadSidebar: true
  }
</script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js"></script>
```

### 创建多级目录

创建多集目录方式非常简单, 在 `_sidebar.md` 中按照目录的层级如下添加内容即可.

```
<!-- docs/_sidebar.md -->

* [首页](/)
* [指南](/guide)

* 效率工具
    *[docsify](/效率工具/docsify)
```
注意,目录必须以 `/` 结束.

自定义侧边栏同时也可以开启目录功能. 如下设置 `subMaxLevel` 配置项:

```html
<!-- index.html -->

<script>
  window.$docsify = {
    loadSidebar: true,
    subMaxLevel: 2
  }
</script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js"></script>
```

[<< 返回首页](/)

### 导航栏

导航栏的开启与设置方法与侧边栏步骤类似.

- 在项目目录下新建 `_navbar.md` 文件, 如果需要将首页防止在导航栏, 则在该文件中输入:

```
<!-- _navbar.md -->

* [首页](/)
```

- 在 `index.html` 文件中配置相应选项

```html
<!-- index.html -->

<script>
  window.$docsify = {
    loadNavbar: true
  }
</script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js"></script>
```

## 封面

- 在项目跟目录下创建 `_coverpage.md` 文件, 添加如下内容:

```
<!-- _coverpage.md -->

<!-- ![logo](_media/icon.svg) -->

# BiuBiu 的博客园

<!-- > 一个神奇的文档网站生成器。 -->

<!-- - 简单、轻便 (压缩后 ~21kB) -->
<!-- - 无需生成 html 文件 -->
<!-- - 众多主题 -->

[GitHub](your github url)
[首页](/README)

<!-- 背景图片 -->

<!-- 背景色 -->

<!-- ![color](#) -->
```

- 在 `index.html` 文件中开启封面渲染功能.

```html
<!-- index.html -->

<script>
  window.$docsify = {
    coverpage: true,
    onlyCover: true
  }
</script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js"></script>
```

## 部署到 Github Page

- 在github上创建名为 `username.github.io` 的仓库 (注意, username 必须和 github 用户名一致)

- 点击仓库中的 `settings`, 找到 `Github Pages`
