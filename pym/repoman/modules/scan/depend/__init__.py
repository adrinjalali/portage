# Copyright 2015-2016 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

doc = """Depend plug-in module for repoman.
Performs Dependency checks on ebuilds."""
__doc__ = doc[:]


module_spec = {
	'name': 'depend',
	'description': doc,
	'provides':{
		'depend-module': {
			'name': "depend",
			'sourcefile': "depend",
			'class': "DependChecks",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['qatracker', 'portdb'
			],
			'func_kwargs': {'ebuild': None, 'pkg': None, 'unknown_pkgs': 'set',
				'type_list': 'list', 'badlicsyntax': 'Future',
				'baddepsyntax': 'Future',
			},
		},
		'profile-module': {
			'name': "profile",
			'sourcefile': "profile",
			'class': "ProfileDependsChecks",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['qatracker', 'portdb', 'profiles', 'options',
				'repo_settings', 'include_arches', 'caches',
				'repoman_incrementals', 'env', 'have', 'dev_keywords'
			],
			'func_kwargs': {'arches': None, 'ebuild': None, 'pkg': None,
				'unknown_pkgs': None, 'baddepsyntax': None,
			},
		},
		'unknown-module': {
			'name': "unknown",
			'sourcefile': "unknown",
			'class': "DependUnknown",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['qatracker',
			],
			'func_kwargs': {'ebuild': None, 'unknown_pkgs': 'set',
				'baddepsyntax': None,
			},
		},
	}
}

