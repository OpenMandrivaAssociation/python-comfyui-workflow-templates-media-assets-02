Name:		python-comfyui-workflow-templates-media-assets-02
Version:	0.1.27
Release:	1
Summary:	Workflow template preview assets for ComfyUI
License:	MIT
Group:		Development/Python
URL:		https://github.com/Comfy-Org/workflow_templates
Source0:	https://files.pythonhosted.org/packages/source/c/comfyui-workflow-templates-media-assets-02/comfyui_workflow_templates_media_assets_02-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Second preview-asset bundle for the ComfyUI workflow templates.
These are upstream media assets, not model weights.

%files
%{py_sitedir}/comfyui_workflow_templates_media_assets_02
%{py_sitedir}/comfyui_workflow_templates_media_assets_02-*.*-info
