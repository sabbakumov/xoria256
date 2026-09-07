# Copyright (c) 2026, Sergey Abbakumov
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from pathlib import Path
import json
import shutil
import zipfile


VERSION = "1.0.0"
EXTENSION_NAME = "xoria256"
VSIX_NAME = f"Xoria256-{VERSION}.vsix"

BUILD_DIR = Path("xoria256-vscode")
EXTENSION_DIR = BUILD_DIR / "extension"
THEME_DIR = EXTENSION_DIR / "themes"


# ============================================================
# dark_vs.json
# ============================================================

dark_vs = {
    "$schema": "vscode://schemas/color-theme",
    "name": "Dark (Visual Studio)",
    "colors": {
        "checkbox.border": "#6B6B6B",
        "editor.background": "#1c1c1c",
        "editor.foreground": "#d0d0d0",
        "editor.inactiveSelectionBackground": "#3A3D41",
        "editorIndentGuide.background1": "#404040",
        "editorIndentGuide.activeBackground1": "#707070",
        "editor.selectionBackground": "#875f87",
        "editorCursor.foreground": "#ffaf00",
        "editor.lineHighlightBackground": "#3a3a3a",
        "list.dropBackground": "#383B3D",
        "activityBarBadge.background": "#007ACC",
        "sideBarTitle.foreground": "#BBBBBB",
        "input.placeholderForeground": "#A6A6A6",
        "menu.background": "#252526",
        "menu.foreground": "#CCCCCC",
        "menu.separatorBackground": "#454545",
        "menu.border": "#454545",
        "menu.selectionBackground": "#0078d4",
        "statusBarItem.remoteForeground": "#FFF",
        "statusBarItem.remoteBackground": "#16825D",
        "ports.iconRunningProcessForeground": "#369432",
        "sideBarSectionHeader.background": "#0000",
        "sideBarSectionHeader.border": "#ccc3",
        "tab.selectedBackground": "#37373D",
        "tab.selectedForeground": "#FFFFFF",
        "tab.lastPinnedBorder": "#ccc3",
        "list.activeSelectionIconForeground": "#FFF",
        "terminal.inactiveSelectionBackground": "#3A3D41",
        "widget.border": "#303031",
        "actionBar.toggledBackground": "#383a49",
        "agentsPanel.border": "#303031",
        "agentsCard.border": "#00000000",
        "agentsChatInput.border": "#303031",
        "agentsChatInput.focusBorder": "#007ACC",
        "agentsNewSessionButton.border": "#303031",
        "surface.border": "#252526",
        "modernActivityBarItem.activeBackground": "#1c1c1c",
        "modernActivityBarItem.hoverBackground": "#1E1E1E66",
        "modernActivityBar.border": "#00000000",
    },
    "tokenColors": [
        {
            "scope": [
                "meta.embedded",
                "source.groovy.embedded",
                "string meta.image.inline.markdown",
                "variable.legacy.builtin.python",
            ],
            "settings": {"foreground": "#d0d0d0"},
        },
        {
            "scope": "emphasis",
            "settings": {"fontStyle": "italic"},
        },
        {
            "scope": "strong",
            "settings": {"fontStyle": "bold"},
        },
        {
            "scope": "header",
            "settings": {"foreground": "#000080"},
        },
        {
            "scope": "comment",
            "settings": {"foreground": "#808080"},
        },
        {
            "scope": "keyword.other.parameter",
            "settings": {"foreground": "#808080"},
        },
        {
            "scope": "storage.type.namespace",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "storage.type.class",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "storage.type.enum",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "storage.type.struct",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "storage.type.modifier",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "storage.type.template",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "storage.type.class.gtkdoc",
            "settings": {"foreground": "#dfdf00"},
        },
        {
            "scope": "meta.template.call",
            "settings": {"foreground": "#afafdf"},
        },
        {
            "scope": "markup.inline.raw.string",
            "settings": {"foreground": "#808080"},
        },
        {
            "scope": "comment.line.double-slash.documentation.cpp variable.parameter",
            "settings": {"foreground": "#808080"},
        },
        {
            "scope": "punctuation.definition.comment",
            "settings": {"foreground": "#808080"},
        },
        {
            "scope": "entity.other.attribute",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "constant.language",
            "settings": {"foreground": "#569cd6"},
        },
        {
            "scope": [
                "constant.numeric",
                "keyword.operator.plus.exponent",
                "keyword.operator.minus.exponent",
            ],
            "settings": {"foreground": "#dfaf87"},
        },
        {
            "scope": "constant.regexp",
            "settings": {"foreground": "#646695"},
        },
        {
            "scope": "entity.name.tag",
            "settings": {"foreground": "#569cd6"},
        },
        {
            "scope": [
                "entity.name.tag.css",
                "entity.name.tag.less",
            ],
            "settings": {"foreground": "#d7ba7d"},
        },
        {
            "scope": "entity.other.attribute-name",
            "settings": {"foreground": "#d0d0d0"},
        },
        {
            "scope": [
                "entity.other.attribute-name.class.css",
                "source.css entity.other.attribute-name.class",
                "entity.other.attribute-name.id.css",
                "entity.other.attribute-name.parent-selector.css",
                "entity.other.attribute-name.parent.less",
                "source.css entity.other.attribute-name.pseudo-class",
                "entity.other.attribute-name.pseudo-element.css",
                "source.css.less entity.other.attribute-name.id",
                "entity.other.attribute-name.scss",
            ],
            "settings": {"foreground": "#d7ba7d"},
        },
        {
            "scope": "invalid",
            "settings": {"foreground": "#f44747"},
        },
        {
            "scope": "markup.underline",
            "settings": {"fontStyle": "underline"},
        },
        {
            "scope": "markup.bold",
            "settings": {
                "fontStyle": "bold",
                "foreground": "#569cd6",
            },
        },
        {
            "scope": "markup.heading",
            "settings": {
                "fontStyle": "bold",
                "foreground": "#569cd6",
            },
        },
        {
            "scope": "markup.italic",
            "settings": {
                "fontStyle": "italic",
                "foreground": "#C586C0",
            },
        },
        {
            "scope": "markup.strikethrough",
            "settings": {"fontStyle": "strikethrough"},
        },
        {
            "scope": "markup.inserted",
            "settings": {"foreground": "#b5cea8"},
        },
        {
            "scope": "markup.deleted",
            "settings": {"foreground": "#ce9178"},
        },
        {
            "scope": "markup.changed",
            "settings": {"foreground": "#569cd6"},
        },
        {
            "scope": "punctuation.definition.quote.begin.markdown",
            "settings": {"foreground": "#6A9955"},
        },
        {
            "scope": "punctuation.definition.list.begin.markdown",
            "settings": {"foreground": "#6796e6"},
        },
        {
            "scope": "markup.inline.raw",
            "settings": {"foreground": "#ce9178"},
        },
        {
            "name": "brackets of XML/HTML tags",
            "scope": "punctuation.definition.tag",
            "settings": {"foreground": "#808080"},
        },
        {
            "scope": [
                "meta.preprocessor",
                "entity.name.function.preprocessor",
            ],
            "settings": {"foreground": "#afdf87"},
        },
        {
            "scope": "meta.preprocessor.string",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "punctuation.definition.string",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "constant.language.nullptr",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "constant.language.true",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "constant.language.false",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "variable.language.this",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "variable.other.unknown.nullopt",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "meta.preprocessor.numeric",
            "settings": {"foreground": "#afdf87"},
        },
        {
            "scope": "entity.other.attribute-name.pragma.preprocessor",
            "settings": {"foreground": "#afdf87"},
        },
        {
            "scope": "meta.preprocessor.macro.cpp constant.character.escape.line-continuation",
            "settings": {"foreground": "#afdf87"},
        },
        {
            "scope": "entity.name.operator.type",
            "settings": {"foreground": "#afafdf"},
        },
        {
            "scope": "punctuation.definition.directive",
            "settings": {"foreground": "#afdf87"},
        },
        {
            "scope": "string.quoted.single",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "string.quoted.single.cpp punctuation.definition.string",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "constant.other.placeholder",
            "settings": {"foreground": "#df8787"},
        },
        {
            "scope": "keyword.control.directive",
            "settings": {"foreground": "#afdf87"},
        },
        {
            "scope": "meta.structure.dictionary.key.python",
            "settings": {"foreground": "#9cdcfe"},
        },
        {
            "scope": "meta.diff.header",
            "settings": {"foreground": "#569cd6"},
        },
        {
            "scope": "storage",
            "settings": {"foreground": "#569cd6"},
        },
        {
            "scope": "storage.type",
            "settings": {"foreground": "#afafdf"},
        },
        {
            "scope": "punctuation",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "storage.type.class.doxygen",
            "settings": {"foreground": "#808080"},
        },
        {
            "scope": "comment.line.double-slash.documentation",
            "settings": {"foreground": "#808080"},
        },
        {
            "scope": [
                "storage.modifier",
                "keyword.operator.noexcept",
            ],
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": [
                "string",
                "meta.embedded.assembly",
            ],
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "string.tag",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "string.value",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "scope": "string.regexp",
            "settings": {"foreground": "#ffffaf"},
        },
        {
            "name": "String interpolation",
            "scope": [
                "punctuation.definition.template-expression.begin",
                "punctuation.definition.template-expression.end",
                "punctuation.section.embedded",
            ],
            "settings": {"foreground": "#569cd6"},
        },
        {
            "name": "Reset JavaScript string interpolation expression",
            "scope": [
                "meta.template.expression",
            ],
            "settings": {"foreground": "#d0d0d0"},
        },
        {
            "scope": [
                "support.type.vendored.property-name",
                "support.type.property-name",
                "source.css variable",
                "source.coffee.embedded",
            ],
            "settings": {"foreground": "#9cdcfe"},
        },
        {
            "scope": "keyword",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "keyword.control",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "keyword.operator",
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": [
                "keyword.operator.new",
                "keyword.operator.expression",
                "keyword.operator.cast",
                "keyword.operator.sizeof",
                "keyword.operator.alignof",
                "keyword.operator.typeid",
                "keyword.operator.alignas",
                "keyword.operator.instanceof",
                "keyword.operator.logical.python",
                "keyword.operator.wordlike",
            ],
            "settings": {"foreground": "#87afdf"},
        },
        {
            "scope": "keyword.other.unit",
            "settings": {"foreground": "#dfaf87"},
        },
        {
            "scope": [
                "punctuation.section.embedded.begin.php",
                "punctuation.section.embedded.end.php",
            ],
            "settings": {"foreground": "#569cd6"},
        },
        {
            "scope": "support.function.git-rebase",
            "settings": {"foreground": "#9cdcfe"},
        },
        {
            "scope": "constant.sha.git-rebase",
            "settings": {"foreground": "#b5cea8"},
        },
        {
            "name": "coloring of the Java import and package identifiers",
            "scope": [
                "storage.modifier.import.java",
                "variable.language.wildcard.java",
                "storage.modifier.package.java",
            ],
            "settings": {"foreground": "#d0d0d0"},
        },
        {
            "name": "this.self",
            "scope": "variable.language",
            "settings": {"foreground": "#569cd6"},
        },
    ],
    "semanticHighlighting": True,
    "semanticTokenColors": {
        "newOperator": "#d0d0d0",
        "stringLiteral": "#ffffaf",
        "customLiteral": "#d0d0d0",
        "numberLiteral": "#b5cea8",
    },
}


# ============================================================
# dark_plus.json
# ============================================================

dark_plus = {
    "$schema": "vscode://schemas/color-theme",
    "name": "Dark+",
    "include": "./dark_vs.json",
    "tokenColors": [
        {
            "name": "Function declarations",
            "scope": [
                "entity.name.function",
                "support.function",
                "support.constant.handlebars",
                "source.powershell variable.other.member",
                "entity.name.operator.custom-literal",
            ],
            "settings": {"foreground": "#dfafdf"},
        },
        {
            "name": "Types declaration and references",
            "scope": [
                "support.class",
                "support.type",
                "entity.name.type",
                "entity.name.namespace",
                "entity.name.scope-resolution",
                "entity.name.class",
                "storage.type.numeric.go",
                "storage.type.byte.go",
                "storage.type.boolean.go",
                "storage.type.string.go",
                "storage.type.uintptr.go",
                "storage.type.error.go",
                "storage.type.rune.go",
                "storage.type.cs",
                "storage.type.generic.cs",
                "storage.type.modifier.cs",
                "storage.type.variable.cs",
                "storage.type.annotation.java",
                "storage.type.generic.java",
                "storage.type.java",
                "storage.type.object.array.java",
                "storage.type.primitive.array.java",
                "storage.type.primitive.java",
                "storage.type.token.java",
                "storage.type.groovy",
                "storage.type.annotation.groovy",
                "storage.type.parameters.groovy",
                "storage.type.generic.groovy",
                "storage.type.object.array.groovy",
                "storage.type.primitive.array.groovy",
                "storage.type.primitive.groovy",
            ],
            "settings": {"foreground": "#afafdf"},
        },
        {
            "name": "Types declaration and references, TS grammar specific",
            "scope": [
                "meta.type.cast.expr",
                "meta.type.new.expr",
                "support.constant.math",
                "support.constant.dom",
                "support.constant.json",
                "entity.other.inherited-class",
                "punctuation.separator.namespace.ruby",
            ],
            "settings": {"foreground": "#4EC9B0"},
        },
        {
            "name": "Control flow / Special keywords",
            "scope": [
                "keyword.control",
                "source.cpp keyword.operator.new",
                "keyword.operator.delete",
                "keyword.other.using",
                "keyword.other.directive.using",
                "keyword.other.operator",
                "entity.name.operator",
            ],
            "settings": {"foreground": "#87afdf"},
        },
        {
            "name": "Variable and parameter name",
            "scope": [
                "variable",
                "meta.definition.variable.name",
                "support.variable",
                "entity.name.variable",
            ],
            "settings": {"foreground": "#d0d0d0"},
        },
        {
            "name": "Constants and enums",
            "scope": [
                "variable.other.constant",
            ],
            "settings": {"foreground": "#4FC1FF"},
        },
        {
            "name": "Object keys, TS grammar specific",
            "scope": [
                "meta.object-literal.key",
            ],
            "settings": {"foreground": "#9CDCFE"},
        },
        {
            "name": "CSS property value",
            "scope": [
                "support.constant.property-value",
                "support.constant.font-name",
                "support.constant.media-type",
                "support.constant.media",
                "constant.other.color.rgb-value",
                "constant.other.rgb-value",
                "support.constant.color",
            ],
            "settings": {"foreground": "#CE9178"},
        },
        {
            "name": "Regular expression groups",
            "scope": [
                "punctuation.definition.group.regexp",
                "punctuation.definition.group.assertion.regexp",
                "punctuation.definition.character-class.regexp",
                "punctuation.character.set.begin.regexp",
                "punctuation.character.set.end.regexp",
                "keyword.operator.negation.regexp",
                "support.other.parenthesis.regexp",
            ],
            "settings": {"foreground": "#CE9178"},
        },
        {
            "scope": [
                "constant.character.character-class.regexp",
                "constant.other.character-class.set.regexp",
                "constant.other.character-class.regexp",
                "constant.character.set.regexp",
            ],
            "settings": {"foreground": "#d16969"},
        },
        {
            "scope": [
                "keyword.operator.or.regexp",
                "keyword.control.anchor.regexp",
            ],
            "settings": {"foreground": "#DCDCAA"},
        },
        {
            "scope": "keyword.operator.quantifier.regexp",
            "settings": {"foreground": "#d7ba7d"},
        },
        {
            "scope": [
                "constant.character",
                "constant.other.option",
            ],
            "settings": {"foreground": "#569cd6"},
        },
        {
            "scope": "constant.character.escape",
            "settings": {"foreground": "#df8787"},
        },
        {
            "scope": "entity.name.label",
            "settings": {"foreground": "#C8C8C8"},
        },
    ],
    "semanticTokenColors": {
        "newOperator": "#C586C0",
        "stringLiteral": "#ffffaf",
        "customLiteral": "#DCDCAA",
        "numberLiteral": "#b5cea8",
    },
}


# ============================================================
# dark_modern.json
# ============================================================

dark_modern = {
    "$schema": "vscode://schemas/color-theme",
    "name": "Dark Modern",
    "include": "./dark_plus.json",
    "colors": {
        "activityBar.activeBorder": "#0078D4",
        "activityBar.background": "#181818",
        "activityBar.border": "#2B2B2B",
        "activityBar.foreground": "#D7D7D7",
        "activityBar.inactiveForeground": "#868686",
        "activityBarBadge.background": "#0078D4",
        "activityBarBadge.foreground": "#FFFFFF",
        "badge.background": "#616161",
        "badge.foreground": "#F8F8F8",
        "button.background": "#0078D4",
        "button.border": "#ffffff1a",
        "button.foreground": "#FFFFFF",
        "button.hoverBackground": "#026EC1",
        "button.secondaryBackground": "#00000000",
        "button.secondaryForeground": "#CCCCCC",
        "button.secondaryHoverBackground": "#2B2B2B",
        "chat.slashCommandBackground": "#26477866",
        "chat.slashCommandForeground": "#85B6FF",
        "chat.editedFileForeground": "#E2C08D",
        "checkbox.background": "#313131",
        "checkbox.border": "#3C3C3C",
        "debugToolBar.background": "#181818",
        "descriptionForeground": "#9D9D9D",
        "dropdown.background": "#313131",
        "dropdown.border": "#3C3C3C",
        "dropdown.foreground": "#CCCCCC",
        "dropdown.listBackground": "#1c1c1c",
        "editor.background": "#1c1c1c",
        "editor.findMatchBackground": "#9E6A03",
        "editor.foreground": "#CCCCCC",
        "editorGroup.border": "#FFFFFF17",
        "editorGroupHeader.tabsBackground": "#181818",
        "editorGroupHeader.tabsBorder": "#2B2B2B",
        "editorGutter.addedBackground": "#2EA043",
        "editorGutter.deletedBackground": "#F85149",
        "editorGutter.modifiedBackground": "#0078D4",
        "editorLineNumber.activeForeground": "#CCCCCC",
        "editorLineNumber.foreground": "#6E7681",
        "editorOverviewRuler.border": "#010409",
        "editorWidget.background": "#202020",
        "errorForeground": "#F85149",
        "focusBorder": "#0078D4",
        "foreground": "#CCCCCC",
        "icon.foreground": "#CCCCCC",
        "input.background": "#313131",
        "input.border": "#3C3C3C",
        "input.foreground": "#CCCCCC",
        "input.placeholderForeground": "#989898",
        "inputOption.activeBackground": "#2489DB82",
        "inputOption.activeBorder": "#2488DB",
        "keybindingLabel.foreground": "#CCCCCC",
        "menu.background": "#1c1c1c",
        "menu.selectionBackground": "#0078d4",
        "notificationCenterHeader.background": "#1c1c1c",
        "notificationCenterHeader.foreground": "#CCCCCC",
        "notifications.background": "#1c1c1c",
        "notifications.border": "#2B2B2B",
        "notifications.foreground": "#CCCCCC",
        "panel.background": "#181818",
        "panel.border": "#2B2B2B",
        "panelInput.border": "#2B2B2B",
        "panelTitle.activeBorder": "#0078D4",
        "panelTitle.activeForeground": "#CCCCCC",
        "panelTitle.inactiveForeground": "#9D9D9D",
        "peekViewEditor.background": "#1c1c1c",
        "peekViewEditor.matchHighlightBackground": "#BB800966",
        "peekViewResult.background": "#1c1c1c",
        "peekViewResult.matchHighlightBackground": "#BB800966",
        "pickerGroup.border": "#3C3C3C",
        "progressBar.background": "#0078D4",
        "quickInput.background": "#222222",
        "quickInput.foreground": "#CCCCCC",
        "settings.dropdownBackground": "#313131",
        "settings.dropdownBorder": "#3C3C3C",
        "settings.headerForeground": "#FFFFFF",
        "settings.modifiedItemIndicator": "#BB800966",
        "sideBar.background": "#181818",
        "sideBar.border": "#2B2B2B",
        "sideBar.foreground": "#CCCCCC",
        "sideBarSectionHeader.background": "#181818",
        "sideBarSectionHeader.border": "#2B2B2B",
        "sideBarSectionHeader.foreground": "#CCCCCC",
        "sideBarTitle.foreground": "#CCCCCC",
        "statusBar.background": "#181818",
        "statusBar.border": "#2B2B2B",
        "statusBarItem.hoverBackground": "#F1F1F133",
        "statusBarItem.hoverForeground": "#FFFFFF",
        "statusBar.debuggingBackground": "#0078D4",
        "statusBar.debuggingForeground": "#FFFFFF",
        "statusBar.focusBorder": "#0078D4",
        "statusBar.foreground": "#CCCCCC",
        "statusBar.noFolderBackground": "#1c1c1c",
        "statusBarItem.focusBorder": "#0078D4",
        "statusBarItem.prominentBackground": "#6E768166",
        "statusBarItem.remoteBackground": "#0078D4",
        "statusBarItem.remoteForeground": "#FFFFFF",
        "tab.activeBackground": "#1c1c1c",
        "tab.activeBorder": "#1c1c1c",
        "tab.activeBorderTop": "#0078D4",
        "tab.activeForeground": "#FFFFFF",
        "tab.selectedBorderTop": "#6caddf",
        "tab.border": "#2B2B2B",
        "tab.hoverBackground": "#1c1c1c",
        "tab.inactiveBackground": "#181818",
        "tab.inactiveForeground": "#9D9D9D",
        "tab.unfocusedActiveBorder": "#1c1c1c",
        "tab.unfocusedActiveBorderTop": "#2B2B2B",
        "tab.unfocusedHoverBackground": "#1c1c1c",
        "terminal.foreground": "#CCCCCC",
        "terminal.tab.activeBorder": "#0078D4",
        "textBlockQuote.background": "#2B2B2B",
        "textBlockQuote.border": "#616161",
        "textCodeBlock.background": "#2B2B2B",
        "textLink.activeForeground": "#4daafc",
        "textLink.foreground": "#4daafc",
        "textPreformat.foreground": "#D0D0D0",
        "textPreformat.background": "#3C3C3C",
        "textSeparator.foreground": "#21262D",
        "titleBar.activeBackground": "#181818",
        "titleBar.activeForeground": "#CCCCCC",
        "titleBar.border": "#2B2B2B",
        "titleBar.inactiveBackground": "#1c1c1c",
        "titleBar.inactiveForeground": "#9D9D9D",
        "welcomePage.tileBackground": "#2B2B2B",
        "welcomePage.progress.foreground": "#0078D4",
        "widget.border": "#313131",
        "modernActivityBarItem.activeBackground": "#FFFFFF22",
        "modernActivityBarItem.hoverBackground": "#FFFFFF11",
        "modernActivityBar.border": "#252526",
    },
}


# ============================================================
# Extension package.json
# ============================================================

package_json = {
    "name": EXTENSION_NAME,
    "displayName": "Xoria256",
    "description": "Xoria256 color theme for Visual Studio Code",
    "version": VERSION,
    "publisher": "Sergei Abbakumov",
    "engines": {
        "vscode": "^1.70.0",
    },
    "categories": [
        "Themes",
    ],
    "contributes": {
        "themes": [
            {
                "label": "Xoria256",
                "uiTheme": "vs-dark",
                "path": "./themes/xoria256-color-theme.json",
            }
        ]
    },
    "license": "BSD-2-Clause",
}


# ============================================================
# README
# ============================================================

readme = """# Xoria256 for Visual Studio Code

Xoria256 color theme for Visual Studio Code.

Based on xoria256.vim: soft pastel gamma on dark background.
https://www.vim.org/scripts/script.php?script_id=2140
"""


# ============================================================
# Build
# ============================================================

def write_json(path, data):
    path.write_text(
        json.dumps(data, indent=2) + "\n",
        encoding="utf-8",
    )


def build():
    print("Cleaning old build...")

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    vsix_path = Path(VSIX_NAME)

    if vsix_path.exists():
        vsix_path.unlink()

    THEME_DIR.mkdir(parents=True)

    print("Writing theme files...")

    write_json(
        THEME_DIR / "dark_vs.json",
        dark_vs,
    )

    write_json(
        THEME_DIR / "dark_plus.json",
        dark_plus,
    )

    write_json(
        THEME_DIR / "xoria256-color-theme.json",
        dark_modern,
    )

    print("Writing package.json...")

    write_json(
        EXTENSION_DIR / "package.json",
        package_json,
    )

    print("Writing README...")

    (EXTENSION_DIR / "README.md").write_text(
        readme,
        encoding="utf-8",
    )

    print("Creating VSIX...")

    with zipfile.ZipFile(
        vsix_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:

        for path in EXTENSION_DIR.rglob("*"):
            if not path.is_file():
                continue

            archive_name = (
                Path("extension") /
                path.relative_to(EXTENSION_DIR)
            )

            archive.write(path, archive_name)

    print("Verifying VSIX...")

    with zipfile.ZipFile(vsix_path, "r") as archive:
        names = set(archive.namelist())

        required_files = {
            "extension/package.json",
            "extension/README.md",
            "extension/themes/dark_vs.json",
            "extension/themes/dark_plus.json",
            "extension/themes/xoria256-color-theme.json",
        }

        missing = required_files - names

        if missing:
            raise RuntimeError(
                f"VSIX is missing required files: {sorted(missing)}"
            )

    print()
    print(f"Successfully created: {vsix_path}")
    print()
    print("Install with:")
    print(f"    code --install-extension {vsix_path}")
    print()


if __name__ == "__main__":
    build()
